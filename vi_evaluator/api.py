"""Optional application adapter: pip install fastapi uvicorn; set VI_EVALUATOR_CHECKPOINT."""
import os
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from inference import VietnameseEvaluator
app=FastAPI(title='Vietnamese Evaluator - automatic proxy')
scorer=None
class Request(BaseModel):
 source:str
 candidate:str
@app.post('/score')
def score(req:Request):
 global scorer
 if scorer is None:
  path=os.environ.get('VI_EVALUATOR_CHECKPOINT')
  if not path:raise HTTPException(503,'VI_EVALUATOR_CHECKPOINT not configured')
  scorer=VietnameseEvaluator(path)
 try:return scorer.score(req.source,req.candidate)
 except ValueError as e:raise HTTPException(422,str(e))
