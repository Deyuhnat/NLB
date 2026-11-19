"""Full ViSP fine-tuning; no adapters, no database access, fixed work-wise splits."""
from __future__ import annotations
import argparse
from collections import Counter
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import random
import time
import unicodedata

PREFIX='sentence-paraphrase: '
MODEL_ID='ngwgsang/vit5-base-visp-s1'
CONFIG=dict(seed=42,learning_rates=[1e-5,3e-5],epochs=6,patience=2,batch_size=2,
            accumulation=8,epoch_draws=952,max_tokens=512,weight_decay=.01,warmup_ratio=.1,
            num_beams=5,max_new_tokens=512,precision='float32',method='full_finetune')

def norm(x): return ' '.join(unicodedata.normalize('NFC',x or '').split())
def read(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def dump(p,x):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
def lines(p): return [json.loads(s) for s in Path(p).read_text(encoding='utf-8').splitlines() if s.strip()]
def write_lines(p,rs):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rs),encoding='utf-8')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def prepare(source,destination):
    source=Path(source);destination=Path(destination)
    export=read(source/'data/export_manifest.json')
    assert sha(source/'data/snapshot.json')==export['snapshot_sha256']
    records=lines(source/'data/records.jsonl'); result=[];excluded=[]
    for r in records:
        if r['split']=='pilot' or r['source_uncertainty']:
            excluded.append(dict(sample_id=r['sample_id'],reason='pilot' if r['split']=='pilot' else r['source_uncertainty']));continue
        input_text=norm(r['input_vi']);target=norm(r['review']['output_vi'])
        if not input_text or not target: raise ValueError('Empty pair: '+r['sample_id'])
        result.append(dict(sample_id=r['sample_id'],work_id=r['work_id'],group_id=r['group_id'],split=r['split'],
            input_vi=input_text,target_vi=target,input_raw=r['input_vi'],target_raw=r['review']['output_vi'],
            context_vi=r['context_vi'],changed=input_text!=target,review_origin=r['review_origin']))
    if len({r['sample_id'] for r in result})!=len(result):raise ValueError('Duplicate IDs')
    for a in ['train','dev','test']:
        for b in ['train','dev','test']:
            if a!=b: assert not ({r['group_id'] for r in result if r['split']==a}&{r['group_id'] for r in result if r['split']==b})
    for split in ['train','dev','test']:write_lines(destination/f'{split}.jsonl',[r for r in result if r['split']==split])
    dump(destination/'excluded.json',excluded)
    manifest=dict(snapshot_sha256=export['snapshot_sha256'],source_split_sha256=sha(source/'data/split_manifest.json'),
        counts={split:dict(n=sum(r['split']==split for r in result),changed=sum(r['split']==split and r['changed'] for r in result)) for split in ['train','dev','test']},
        files={f'{s}.jsonl':sha(destination/f'{s}.jsonl') for s in ['train','dev','test']},config=CONFIG)
    dump(destination/'manifest.json',manifest);print(json.dumps(manifest,indent=2))

def deps():
    os.environ.setdefault('USE_TF','0')
    import torch
    from transformers import AutoTokenizer,AutoModelForSeq2SeqLM
    return torch,AutoTokenizer,AutoModelForSeq2SeqLM

def set_seed(seed):
    torch,_,_=deps();random.seed(seed)
    import numpy as np
    np.random.seed(seed);torch.manual_seed(seed)
    if torch.cuda.is_available():torch.cuda.manual_seed_all(seed)

def encode(rows,tokenizer,limit=512):
    valid=[];bad=[]
    for r in rows:
        ids=tokenizer(PREFIX+r['input_vi'],truncation=False)['input_ids']
        labels=tokenizer(text_target=r['target_vi'],truncation=False)['input_ids']
        if max(len(ids),len(labels))>limit:
            bad.append(dict(sample_id=r['sample_id'],input_tokens=len(ids),target_tokens=len(labels)));continue
        valid.append(dict(r,input_ids=ids,labels=labels))
    return valid,bad

def collate(rows,tokenizer,device):
    torch,_,_=deps()
    x=tokenizer.pad([dict(input_ids=r['input_ids']) for r in rows],return_tensors='pt')
    labels=torch.full((len(rows),max(len(r['labels']) for r in rows)),-100,dtype=torch.long)
    for i,r in enumerate(rows):labels[i,:len(r['labels'])]=torch.tensor(r['labels'])
    return {k:v.to(device) for k,v in dict(x,labels=labels).items()}

def sample_indices(rows,seed,draws):
    import numpy as np
    changed=[i for i,r in enumerate(rows) if r['changed']];identity=[i for i,r in enumerate(rows) if not r['changed']]
    if not changed or not identity:raise ValueError('Both changed and identity groups are required')
    rng=np.random.default_rng(seed)
    # Exact 50/50 counts, replacement sampling within each group.
    ids=np.r_[rng.choice(changed,draws//2),rng.choice(identity,draws-draws//2)]
    rng.shuffle(ids);return ids.tolist()

def dev_loss(model,rows,tokenizer,device,batch=2):
    torch,_,_=deps();model.eval();groups={True:[],False:[]}
    with torch.inference_mode():
        for start in range(0,len(rows),batch):
            rs=rows[start:start+batch];inputs=collate(rs,tokenizer,device)
            output=model(**inputs)
            token_loss=torch.nn.functional.cross_entropy(output.logits.transpose(1,2),inputs['labels'],ignore_index=-100,reduction='none')
            per_sample=token_loss.sum(1)/(inputs['labels']!=-100).sum(1).clamp_min(1)
            for r,value in zip(rs,per_sample.tolist()):groups[r['changed']].append(value)
    means={str(k):sum(v)/len(v) if v else None for k,v in groups.items()}
    if any(v is None for v in means.values()):raise ValueError('Dev lacks one label group')
    return dict(changed=means['True'],identity=means['False'],balanced=(means['True']+means['False'])/2)

def full_step(model,inputs,optimizer):
    """Used by the real smoke test: verify unfreezing, gradients and weight change."""
    torch,_,_=deps()
    model.train();optimizer.zero_grad(set_to_none=True)
    parameters=list(model.parameters());assert all(p.requires_grad for p in parameters)
    before=[p.detach().flatten()[:32].cpu().clone() for p in parameters]
    loss=model(**inputs).loss
    if not torch.isfinite(loss):raise RuntimeError('Non-finite smoke loss')
    loss.backward()
    grad_count=sum(p.grad is not None for p in parameters)
    if grad_count<len(parameters)*.95:raise RuntimeError('Too many model parameters have no gradients')
    torch.nn.utils.clip_grad_norm_(parameters,1.0);optimizer.step()
    changed=sum(not torch.equal(a,p.detach().flatten()[:32].cpu()) for a,p in zip(before,parameters))
    if not changed:raise RuntimeError('No parameter changes after optimizer step')
    return dict(loss=float(loss),parameter_tensors=len(parameters),gradient_tensors=grad_count,changed_sentinels=changed,
                trainable_parameters=sum(p.numel() for p in parameters),all_parameters_trainable=True)

def save_latest(path,model,optimizer,scheduler,state):
    torch,_,_=deps();import numpy as np
    state=dict(state,model=model.state_dict(),optimizer=optimizer.state_dict(),scheduler=scheduler.state_dict(),
               rng_cpu=torch.get_rng_state(),rng_cuda=torch.cuda.get_rng_state_all() if torch.cuda.is_available() else [],
               rng_python=random.getstate(),rng_numpy=np.random.get_state())
    path=Path(path);tmp=path.with_suffix('.tmp');torch.save(state,tmp);os.replace(tmp,path)

def load_latest(path,model,optimizer,scheduler,device,expected):
    torch,_,_=deps();import numpy as np
    # Only load a checkpoint generated by this run; never untrusted pickle.
    state=torch.load(path,map_location='cpu',weights_only=False)
    for key,value in expected.items():
        if state[key]!=value:raise ValueError('Resume mismatch: '+key)
    model.load_state_dict(state['model']);optimizer.load_state_dict(state['optimizer']);scheduler.load_state_dict(state['scheduler'])
    for values in optimizer.state.values():
        for k,v in values.items():
            if isinstance(v,torch.Tensor):values[k]=v.to(device)
    torch.set_rng_state(state['rng_cpu']);random.setstate(state['rng_python']);np.random.set_state(state['rng_numpy'])
    if device.startswith('cuda') and state['rng_cuda']:torch.cuda.set_rng_state_all(state['rng_cuda'])
    return state

def train_run(model,tokenizer,train,dev,device,output,lr,manifest_hash,batch=2,accum=8,resume=True):
    torch,_,_=deps()
    from transformers import get_linear_schedule_with_warmup
    output=Path(output);output.mkdir(parents=True,exist_ok=True);set_seed(CONFIG['seed'])
    for p in model.parameters():p.requires_grad_(True)
    model.config.use_cache=False;model.gradient_checkpointing_enable()
    optimizer=torch.optim.AdamW(model.parameters(),lr=lr,weight_decay=CONFIG['weight_decay'])
    steps_per_epoch=math.ceil(math.ceil(CONFIG['epoch_draws']/batch)/accum)
    total=steps_per_epoch*CONFIG['epochs']
    scheduler=get_linear_schedule_with_warmup(optimizer,math.ceil(total*CONFIG['warmup_ratio']),total)
    expected=dict(manifest_hash=manifest_hash,lr=lr,batch=batch,accum=accum,config=CONFIG)
    start=0;best=float('inf');bad_epochs=0;history=[];smoke=None
    latest=output/'latest.pt'
    if resume and latest.exists():
        state=load_latest(latest,model,optimizer,scheduler,device,expected)
        start=state['next_epoch'];best=state['best'];bad_epochs=state['bad_epochs'];history=state['history'];smoke=state['smoke']
    if bad_epochs>=CONFIG['patience']:return read(output/'run_result.json')
    for epoch in range(start,CONFIG['epochs']):
        model.train();draws=sample_indices(train,CONFIG['seed']+epoch,CONFIG['epoch_draws'])
        batches=[draws[i:i+batch] for i in range(0,len(draws),batch)];losses=[];started=time.perf_counter()
        optimizer.zero_grad(set_to_none=True)
        for step,ids in enumerate(batches):
            x=collate([train[i] for i in ids],tokenizer,device)
            loss=model(**x).loss
            if not torch.isfinite(loss):raise RuntimeError('Non-finite training loss')
            # A final partial accumulation window receives the correct scale.
            window=min(accum,len(batches)-(step//accum)*accum)
            (loss/window).backward();losses.append(float(loss.detach()))
            if (step+1)%accum==0 or step+1==len(batches):
                if smoke is None and optimizer.param_groups[0]['lr']>0:
                    ps=list(model.parameters());before=[p.detach().flatten()[:32].cpu().clone() for p in ps]
                    smoke=dict(all_parameters_trainable=all(p.requires_grad for p in ps),
                        total_parameters=sum(p.numel() for p in ps),gradient_tensors=sum(p.grad is not None for p in ps),parameter_tensors=len(ps))
                    assert smoke['all_parameters_trainable'] and smoke['gradient_tensors']>=.95*len(ps)
                torch.nn.utils.clip_grad_norm_(model.parameters(),1.0);optimizer.step();scheduler.step()
                if 'before' in locals():
                    smoke['changed_sentinels']=sum(not torch.equal(a,p.detach().flatten()[:32].cpu()) for a,p in zip(before,ps))
                    assert smoke['changed_sentinels']>0;del before
                    dump(output/'full_training_proof.json',smoke)
                optimizer.zero_grad(set_to_none=True)
            if (step+1)%40==0: print(f'lr={lr} epoch={epoch+1} batch={step+1}/{len(batches)} loss={losses[-1]:.4f}',flush=True)
        validation=dev_loss(model,dev,tokenizer,device)
        row=dict(epoch=epoch+1,train_loss=sum(losses)/len(losses),dev=validation,seconds=time.perf_counter()-started)
        history.append(row)
        if validation['balanced']<best:
            best=validation['balanced'];bad_epochs=0
            model.save_pretrained(output/'best',safe_serialization=True);tokenizer.save_pretrained(output/'best')
            dump(output/'best_epoch.json',row)
        else:bad_epochs+=1
        result=dict(lr=lr,best_dev_loss=best,best_epoch=read(output/'best_epoch.json')['epoch'],history=history,
                    batch=batch,accum=accum,method='full_finetune',model_dir=str(output/'best'))
        dump(output/'run_result.json',result)
        save_latest(latest,model,optimizer,scheduler,dict(expected,next_epoch=epoch+1,best=best,bad_epochs=bad_epochs,history=history,smoke=smoke))
        print(json.dumps(row),flush=True)
        if bad_epochs>=CONFIG['patience']:break
    return read(output/'run_result.json')

def train(data,output):
    torch,AutoTokenizer,AutoModel=deps()
    if not torch.cuda.is_available():raise RuntimeError('Full fine-tune requires Kaggle GPU; CPU execution is intentionally blocked')
    data=Path(data);output=Path(output);output.mkdir(parents=True,exist_ok=True)
    manifest=read(data/'manifest.json')
    for file,expected in manifest['files'].items():assert sha(data/file)==expected
    from huggingface_hub import HfApi
    resolved=output/'base_revision.json'
    if resolved.exists():revision=read(resolved)['revision']
    else:
        revision=HfApi().model_info(MODEL_ID,revision='ff75dba118e7').sha
        dump(resolved,dict(model_id=MODEL_ID,revision=revision))
    tokenizer=AutoTokenizer.from_pretrained(MODEL_ID,revision=revision)
    train,bad_train=encode(lines(data/'train.jsonl'),tokenizer)
    dev,bad_dev=encode(lines(data/'dev.jsonl'),tokenizer)
    # Audit test lengths without using targets for training/model selection.
    _,bad_test=encode(lines(data/'test.jsonl'),tokenizer)
    dump(output/'token_audit.json',dict(train_excluded=bad_train,dev_excluded=bad_dev,test_excluded=bad_test))
    if not train or not dev:raise RuntimeError('No usable train/dev pairs')
    import platform,importlib.metadata
    dump(output/'environment.json',dict(platform=platform.platform(),gpu=torch.cuda.get_device_name(0),
        vram_bytes=torch.cuda.get_device_properties(0).total_memory,torch=torch.__version__,
        transformers=importlib.metadata.version('transformers'),config=CONFIG,revision=revision))
    runs=[]
    for lr in CONFIG['learning_rates']:
        directory=output/f'lr_{lr:.0e}'
        # Each learning rate starts from the same base checkpoint and seed.
        set_seed(CONFIG['seed']);model=AutoModel.from_pretrained(MODEL_ID,revision=revision,torch_dtype=torch.float32).to('cuda:0')
        try:
            try:result=train_run(model,tokenizer,train,dev,'cuda:0',directory,lr,sha(data/'manifest.json'))
            except torch.cuda.OutOfMemoryError:
                del model;torch.cuda.empty_cache()
                if (directory/'latest.pt').exists():
                    # Completed epochs keep the original effective batch and schedule.
                    state=torch.load(directory/'latest.pt',map_location='cpu',weights_only=False)
                    state['batch']=1;state['accum']=16
                    torch.save(state,directory/'latest.pt');del state
                set_seed(CONFIG['seed']);model=AutoModel.from_pretrained(MODEL_ID,revision=revision,torch_dtype=torch.float32).to('cuda:0')
                result=train_run(model,tokenizer,train,dev,'cuda:0',directory,lr,sha(data/'manifest.json'),batch=1,accum=16)
        finally:
            if 'model' in locals():del model
            torch.cuda.empty_cache()
        runs.append(result)
    winner=min(runs,key=lambda r:(r['best_dev_loss'],r['lr'],r['best_epoch']))
    dump(output/'selected_model.json',dict(winner=winner,runs=runs,manifest_sha256=sha(data/'manifest.json'),
        revision=revision,selection='balanced dev token loss; no test tuning'))
    print('Selected',winner['model_dir'],flush=True)

def generate(model,tokenizer,rows,device,system):
    torch,_,_=deps();model.eval();model.config.use_cache=True;result=[]
    for r in rows:
        t=time.perf_counter();error=None;raw='';truncated=False
        try:
            encoded=tokenizer(PREFIX+r['input_vi'],return_tensors='pt',truncation=False)
            if encoded['input_ids'].shape[1]>512:raise ValueError('Input too long')
            with torch.inference_mode():
                ids=model.generate(**{k:v.to(device) for k,v in encoded.items()},num_beams=5,do_sample=False,max_new_tokens=512,num_return_sequences=1)
            raw=tokenizer.decode(ids[0],skip_special_tokens=True)
            truncated=tokenizer.eos_token_id not in ids[0].tolist()[1:]
        except (RuntimeError,ValueError) as e:error=str(e)
        result.append(dict(sample_id=r['sample_id'],work_id=r['work_id'],system_id=system,raw_output=raw,
            output_vi=raw if norm(raw) and not error and not truncated else r['input_vi'],
            status='error' if error else 'truncated' if truncated else 'empty' if not norm(raw) else 'ok',
            fallback=bool(error or truncated or not norm(raw)),error=error,latency_ms=(time.perf_counter()-t)*1000))
    return result

def metrics(rows,predictions):
    from sacrebleu.metrics import CHRF
    lookup={r['sample_id']:r for r in rows};metric=CHRF(word_order=2)
    result={}
    for name in ['all','changed','identity']:
        subset=[p for p in predictions if name=='all' or lookup[p['sample_id']]['changed']==(name=='changed')]
        if not subset:result[name]=dict(n=0,chrf_pp=None,exact_match=None);continue
        refs=[lookup[p['sample_id']]['target_vi'] for p in subset];outputs=[p['output_vi'] for p in subset]
        result[name]=dict(n=len(subset),chrf_pp=metric.corpus_score(outputs,[refs]).score,
            exact_n=sum(norm(a)==norm(b) for a,b in zip(outputs,refs)),
            exact_match=sum(norm(a)==norm(b) for a,b in zip(outputs,refs))/len(subset),
            intervention=sum(norm(p['output_vi'])!=norm(lookup[p['sample_id']]['input_vi']) for p in subset)/len(subset),
            generation_failures=sum(p.get('status','ok')!='ok' for p in subset))
    result['chrf_signature']=str(metric.get_signature())
    result['quality_judgments']=dict(safe_improvement=None,harm=None,clean_harm=None,status='pending')
    return result

def evaluate(data,output):
    torch,AutoTokenizer,AutoModel=deps();data=Path(data);output=Path(output)
    selection=read(output/'selected_model.json')
    assert selection['manifest_sha256']==sha(data/'manifest.json')
    rows=lines(data/'test.jsonl');device='cuda:0' if torch.cuda.is_available() else 'cpu'
    predictions=[dict(sample_id=r['sample_id'],work_id=r['work_id'],system_id='identity',output_vi=r['input_vi'],status='ok',latency_ms=0) for r in rows]
    for system,source,revision in [('visp_base',MODEL_ID,selection['revision']),('visp_full',selection['winner']['model_dir'],None)]:
        tokenizer=AutoTokenizer.from_pretrained(source,revision=revision)
        model=AutoModel.from_pretrained(source,revision=revision,torch_dtype=torch.float32).to(device)
        for _ in range(2):generate(model,tokenizer,rows[:1],device,system)
        predictions.extend(generate(model,tokenizer,rows,device,system))
        if system=='visp_full':
            before=generate(model,tokenizer,rows[:3],device,system)
            # Load the saved weights a second time and compare real generation.
            del model;torch.cuda.empty_cache()
            model=AutoModel.from_pretrained(source,torch_dtype=torch.float32).to(device)
            after=generate(model,tokenizer,rows[:3],device,system)
            assert [p['raw_output'] for p in before]==[p['raw_output'] for p in after]
            dump(output/'reload_verification.json',dict(same_three_outputs=True,full_model=True,adapter_used=False))
        del model;torch.cuda.empty_cache()
    write_lines(output/'test_predictions.jsonl',predictions)
    scores={system:metrics(rows,[p for p in predictions if p['system_id']==system]) for system in ['identity','visp_base','visp_full']}
    dump(output/'test_metrics.json',scores)
    forms=[];key=[];rng=random.Random(42);byid={r['sample_id']:r for r in rows}
    for p in predictions:
        if p['system_id']=='identity':continue
        r=byid[p['sample_id']];form_id=f'{rng.getrandbits(128):032x}';out_side=rng.choice(['A','B'])
        texts={out_side:p['output_vi'], 'B' if out_side=='A' else 'A':r['input_vi']}
        forms.append(dict(form_id=form_id,sample_id=r['sample_id'],input_vi=r['input_vi'],context_vi=r['context_vi'],
            **texts,needs_edit=None,naturalness_A=None,naturalness_B=None,preservation_A=None,preservation_B=None,
            harm_A=None,harm_B=None,preference=None,reviewer_id=None,review_status='pending'))
        key.append(dict(form_id=form_id,system_id=p['system_id'],output_side=out_side))
    rng.shuffle(forms);write_lines(output/'evaluation/review_sheet.jsonl',forms);dump(output/'evaluation/private_key.json',key)
    import difflib
    edits=[]
    for p in predictions:
        if p['system_id']=='identity':continue
        a=byid[p['sample_id']]['input_vi'];b=p['output_vi'];matcher=difflib.SequenceMatcher(None,a,b,autojunk=False)
        for tag,i,j,k,l in matcher.get_opcodes():
            if tag!='equal':edits.append(dict(sample_id=p['sample_id'],system_id=p['system_id'],kind=tag,
                input_span=[i,j],output_span=[k,l],before=a[i:j],after=b[k:l],judgment=None,review_status='pending'))
    write_lines(output/'evaluation/edit_sheet.jsonl',edits)
    print(json.dumps(scores,indent=2))

def smoke(output):
    """Real tiny-T5 optimizer/checkpoint test, explicitly not a trained ViSP result."""
    torch,_,_=deps()
    from transformers import T5Config,T5ForConditionalGeneration,get_linear_schedule_with_warmup
    output=Path(output);output.mkdir(parents=True,exist_ok=True);torch.set_num_threads(2);set_seed(42)
    cfg=T5Config(vocab_size=64,d_model=32,d_ff=64,num_layers=1,num_decoder_layers=1,num_heads=2,decoder_start_token_id=0,pad_token_id=0,eos_token_id=1,dropout_rate=0)
    model=T5ForConditionalGeneration(cfg)
    batch=dict(input_ids=torch.tensor([[2,3,4,1],[5,6,1,0]]),attention_mask=torch.tensor([[1,1,1,1],[1,1,1,0]]),labels=torch.tensor([[7,8,1,-100],[9,1,-100,-100]]))
    opt=torch.optim.AdamW(model.parameters(),lr=1e-3);scheduler=get_linear_schedule_with_warmup(opt,0,3)
    proof=full_step(model,batch,opt);scheduler.step()
    model.save_pretrained(output/'tiny_model',safe_serialization=True)
    reloaded=T5ForConditionalGeneration.from_pretrained(output/'tiny_model');model.eval();reloaded.eval()
    with torch.no_grad():assert torch.allclose(model(**batch).logits,reloaded(**batch).logits)
    expected={'manifest_hash':'synthetic-smoke'}
    save_latest(output/'resume.pt',model,opt,scheduler,dict(expected,next_epoch=1))
    clone=T5ForConditionalGeneration(cfg);opt2=torch.optim.AdamW(clone.parameters(),lr=1e-3);sch2=get_linear_schedule_with_warmup(opt2,0,3)
    load_latest(output/'resume.pt',clone,opt2,sch2,'cpu',expected)
    assert sch2.last_epoch==scheduler.last_epoch
    for a,b in zip(model.parameters(),clone.parameters()):assert torch.equal(a,b)
    # One more step after restore must reproduce the uninterrupted run.
    full_step(model,batch,opt);full_step(clone,batch,opt2)
    for a,b in zip(model.parameters(),clone.parameters()):assert torch.equal(a,b)
    dump(output/'smoke_result.json',dict(proof,reload_logits_equal=True,resume_next_step_equal=True,
        scope='synthetic tiny T5 only; not ViSP training',device='cpu'))
    print(json.dumps(read(output/'smoke_result.json'),indent=2))

def main():
    p=argparse.ArgumentParser();p.add_argument('command',choices=['prepare','train','evaluate','smoke']);p.add_argument('--source');p.add_argument('--data',default='data');p.add_argument('--output',default='runs')
    a=p.parse_args()
    if a.command=='prepare':prepare(a.source,a.data)
    elif a.command=='smoke':smoke(a.output)
    else:globals()[a.command](a.data,a.output)

if __name__=='__main__':main()
