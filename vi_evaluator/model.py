"""A shared sentence encoder plus explicit proxy heads and an uncalibrated rank head."""
import torch
from torch import nn
from torch.nn import functional as F
class Evaluator(nn.Module):
 def __init__(self,encoder):
  super().__init__();self.encoder=encoder;h=encoder.config.hidden_size
  self.trunk=nn.Sequential(nn.Linear(4*h,h),nn.GELU(),nn.Dropout(.1))
  self.heads=nn.Linear(h,3)
 def embed(self,batch):
  hidden=self.encoder(**batch).last_hidden_state
  mask=batch['attention_mask'].unsqueeze(-1)
  pooled=(hidden*mask).sum(1)/mask.sum(1).clamp(min=1)
  return F.normalize(pooled.float(),dim=-1)
 def forward(self,a,b):
  u,v=self.embed(a),self.embed(b)
  y=self.heads(self.trunk(torch.cat([u,v,(u-v).abs(),u*v],-1)))
  return dict(rank=y[:,0],fluency=y[:,1],semantic=torch.tanh(y[:,2]))
def contrastive(a,b,groups,temperature=.05):
 scores=a.float()@b.float().T/temperature
 positive=groups[:,None].eq(groups[None,:])
 def loss(x,m):return (torch.logsumexp(x,-1)-torch.logsumexp(x.masked_fill(~m,-torch.inf),-1)).mean()
 return .5*(loss(scores,positive)+loss(scores.T,positive.T))
def proxy_losses(preferred,alternative,labels):
 rank=F.softplus(alternative['rank']-preferred['rank']).mean()
 parts={}
 for key,target in [('fluency','fluency_target'),('semantic','semantic_target')]:
  values=[]
  for output,lab in [(preferred,labels[0]),(alternative,labels[1])]:
   y=lab[target];mask=torch.isfinite(y)
   if mask.any():values.append(F.smooth_l1_loss(output[key][mask],y[mask]) if key=='fluency' else F.mse_loss(output[key][mask],y[mask]))
  parts[key]=sum(values)/len(values) if values else rank*0
 return .5*rank+.25*parts['fluency']+.25*parts['semantic']
