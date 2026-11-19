"""Join source and generation by ID; never call fallback an improvement."""
import argparse,json
from pathlib import Path
def read(p):
 return [json.loads(s) for s in Path(p).read_text(encoding="utf-8").splitlines() if s.strip()]
def join(sources,predictions):
 src={r["sample_id"]:r for r in sources}
 if len(src)!=len(sources):raise ValueError("Duplicate input IDs")
 ids=[r["sample_id"] for r in predictions]
 if len(ids)!=len(set(ids)) or set(ids)!=set(src):raise ValueError("Prediction IDs must match input IDs exactly")
 rows=[]
 for p in predictions:
  a=src[p["sample_id"]]["input_vi"];b=p["output_vi"]
  if not isinstance(a,str) or not isinstance(b,str) or not a.strip() or not b.strip():raise ValueError("Empty/non-string sentence")
  rows.append(dict(sample_id=p["sample_id"],source=a,candidate=b,generation_status=p.get("status"),generation_fallback=p.get("fallback")))
 return rows
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--input",required=True);ap.add_argument("--predictions",required=True);ap.add_argument("--output",required=True);args=ap.parse_args()
 rows=join(read(args.input),read(args.predictions))
 with Path(args.output).open("x",encoding="utf-8") as f:
  for r in rows:f.write(json.dumps(r,ensure_ascii=False)+"\n")
 print("Prepared",len(rows),"source-candidate pairs")
if __name__=="__main__":main()
