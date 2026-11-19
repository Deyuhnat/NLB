"""Contracts and provenance shared by data, training, inference and reports."""
import os,sys,json,hashlib,unicodedata,random
from pathlib import Path
os.environ.setdefault('USE_TF','0');os.environ.setdefault('USE_FLAX','0')
if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parent
def norm(s):return ' '.join(unicodedata.normalize('NFC',s or '').split())
def digest(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
 return h.hexdigest()
def read(path):return [json.loads(s) for s in Path(path).read_text(encoding='utf-8-sig').splitlines() if s.strip()]
def write(path,rows):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w',encoding='utf-8',newline='\n') as f:
  for r in rows:f.write(json.dumps(r,ensure_ascii=False,allow_nan=False)+'\n')
def save(path,obj):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8')
def config():return json.loads((ROOT/'config.json').read_text(encoding='utf-8'))
def seed_all(seed=42):
 import numpy as np,torch
 random.seed(seed);np.random.seed(seed);torch.manual_seed(seed)
 if torch.cuda.is_available():torch.cuda.manual_seed_all(seed)
def verify(path):
 m=json.loads(Path(path).read_text(encoding='utf-8'))
 for p,h in m['files'].items():
  if sha(ROOT/p)!=h:raise ValueError('Frozen file changed: '+p)
 return m
