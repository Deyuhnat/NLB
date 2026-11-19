"""Recreate proxy labels from pinned teachers. Never called human annotation."""
import argparse,math
from common import *
import numpy as np
import torch
from transformers import AutoTokenizer,AutoModel,AutoModelForCausalLM
LM='NlpHUST/gpt2-vietnamese'
LM_REV='65818d14816b42be09e2201933bf07106d9a2647'
class Teacher:
 def __init__(self,device=None):
  self.device=device or ('cuda:0' if torch.cuda.is_available() else 'cpu');c=config()
  self.tokenizer=AutoTokenizer.from_pretrained(c['encoder'],revision=c['encoder_revision'])
  self.encoder=AutoModel.from_pretrained(c['encoder'],revision=c['encoder_revision'],add_pooling_layer=False).to(self.device).eval()
  self.ltok=AutoTokenizer.from_pretrained(LM,revision=LM_REV);self.lm=AutoModelForCausalLM.from_pretrained(LM,revision=LM_REV).to(self.device).eval()
  self.path=ROOT/'private/teacher_cache.jsonl';self.cache={r['text_sha256']:r for r in read(self.path)} if self.path.exists() else {}
 def text(self,t):
  t=norm(t);key=digest(t)
  if key in self.cache:return self.cache[key]
  # Historical semantic teacher used its documented 128-token sentence limit.
  x=self.tokenizer(t,return_tensors='pt',truncation=True,max_length=128)
  x={k:v.to(self.device) for k,v in x.items()}
  with torch.inference_mode():
   h=self.encoder(**x).last_hidden_state;m=x['attention_mask'].unsqueeze(-1);v=(h*m).sum(1)/m.sum(1);v=torch.nn.functional.normalize(v,dim=-1)[0]
   z=self.ltok(t,return_tensors='pt',truncation=False);n=z['input_ids'].shape[1];nll=None
   if 2<=n<=getattr(self.lm.config,'n_positions',1024):
    z={k:v.to(self.device) for k,v in z.items()};nll=float(self.lm(**z,labels=z['input_ids']).loss)
    if not math.isfinite(nll):nll=None
  r=dict(text_sha256=key,vector=v.cpu().tolist(),nll=nll,lm_tokens=n,semantic_truncated=x['input_ids'].shape[1]>=128)
  self.cache[key]=r;self.path.parent.mkdir(parents=True,exist_ok=True)
  with self.path.open('a',encoding='utf-8') as f:f.write(json.dumps(r)+'\n')
  return r
 def pair(self,a,b):
  u=self.text(a);v=self.text(b)
  return dict(fluency_target=u['nll']-v['nll'] if u['nll'] is not None and v['nll'] is not None else None,semantic_target=float(np.dot(u['vector'],v['vector'])),label_origin='automatic_proxy',human_validated=False)
def main():
 p=argparse.ArgumentParser();p.add_argument('--splits',nargs='+',default=['train','dev']);a=p.parse_args();teacher=Teacher()
 for split in a.splits:
  result=[]
  for s in read(ROOT/f'data/team_{split}.jsonl'):
   for c in s['candidates']:result.append(dict(sample_id=s['sample_id'],candidate_id=c['candidate_id'],input_vi=s['input_vi'],candidate_vi=c['text'],**teacher.pair(s['input_vi'],c['text'])))
  # Separate recreation outputs: preserved original cached policy labels stay immutable.
  write(ROOT/f'data/team_labels_{split}_recreated.jsonl',result);print(split,len(result),flush=True)
if __name__=='__main__':main()
