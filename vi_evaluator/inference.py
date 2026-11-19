"""Reference-free Vietnamese quality proxy. Scores are not human-calibrated ratings."""
import argparse,json,time
from common import *
import torch
from transformers import AutoModel,AutoTokenizer
from model import Evaluator

class VietnameseEvaluator:
 def __init__(self,checkpoint,device=None):
  self.path=Path(checkpoint);self.device=device or ('cuda:0' if torch.cuda.is_available() else 'cpu')
  self.card=json.loads((self.path/'model_card.json').read_text(encoding='utf-8'))
  self.version=sha(self.path/'model_card.json')[:16]
  try:tokenizer_path=os.path.relpath(self.path/'encoder',Path.cwd())
  except ValueError:tokenizer_path=str((self.path/'encoder').resolve())
  self.tokenizer=AutoTokenizer.from_pretrained(tokenizer_path,local_files_only=True)
  self.model=Evaluator(AutoModel.from_pretrained(self.path/'encoder',local_files_only=True,add_pooling_layer=False))
  heads=torch.load(self.path/'heads.pt',map_location='cpu',weights_only=True)
  self.model.trunk.load_state_dict(heads['trunk']);self.model.heads.load_state_dict(heads['heads'])
  self.model.to(self.device).eval();self.max_tokens=self.card.get('token_limit',512)
 def score_many(self,pairs,batch_size=16):
  results=[]
  for start in range(0,len(pairs),batch_size):
   batch=pairs[start:start+batch_size];texts=[]
   for pair in batch:
    a,b=norm(pair['source']),norm(pair['candidate'])
    if not a or not b:raise ValueError('source and candidate must be nonempty strings')
    texts.append((a,b))
   tokens=[self.tokenizer([t[i] for t in texts],truncation=False) for i in range(2)]
   if any(len(ids)>self.max_tokens for t in tokens for ids in t['input_ids']):
    raise ValueError('Input exceeds token limit; split into sentences. No silent truncation.')
   packed=[{k:v.to(self.device) for k,v in self.tokenizer.pad(t,padding=True,return_tensors='pt').items() if k in ['input_ids','attention_mask','token_type_ids']} for t in tokens]
   if str(self.device).startswith('cuda'):torch.cuda.synchronize(self.device)
   begin=time.perf_counter()
   with torch.inference_mode():output=self.model(*packed)
   if str(self.device).startswith('cuda'):torch.cuda.synchronize(self.device)
   elapsed=time.perf_counter()-begin
   for i,pair in enumerate(batch):
    results.append(dict(rank_score=float(output['rank'][i]),fluency_delta_proxy=float(output['fluency'][i]),semantic_preservation_proxy=float(output['semantic'][i]),
     grammar_score=None,evaluator_version=self.version,context_used=False,human_validated=False,label_origin=self.card.get('label_origin','automatic_proxy_and_legacy_inferred_preference'),
     score_contract='raw rank; fluency=NLL(source)-NLL(candidate) proxy; semantic=frozen teacher cosine proxy; no 0-100 human calibration',
     latency_seconds_per_pair=elapsed/len(batch),latency_scope='model_forward_excludes_tokenization'))
  return results
 def score(self,source,candidate):return self.score_many([dict(source=source,candidate=candidate)])[0]

def main():
 p=argparse.ArgumentParser();p.add_argument('--checkpoint',required=True);p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--device');a=p.parse_args()
 rows=read(a.input);scorer=VietnameseEvaluator(a.checkpoint,a.device);scores=scorer.score_many(rows)
 write(a.output,[dict(**r,evaluation=s) for r,s in zip(rows,scores)])
 print('Scored',len(rows),'pairs; automatic proxy, not independent human ratings')
if __name__=='__main__':main()
