"""Run the saved full model on new Vietnamese sentences (no database required)."""
import argparse
from pathlib import Path
import full_finetune as f

def main():
    p=argparse.ArgumentParser();p.add_argument('--model',default='runs/lr_1e-05/best');p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--device',default='auto');a=p.parse_args()
    if Path(a.output).exists():raise FileExistsError('Choose a new output path')
    torch,Tokenizer,Model=f.deps()
    device=('cuda:0' if torch.cuda.is_available() else 'cpu') if a.device=='auto' else a.device
    if device=='cpu':torch.set_num_threads(4)
    rows=f.lines(a.input)
    if len({r['sample_id'] for r in rows})!=len(rows):raise ValueError('Duplicate sample IDs')
    for r in rows:
        if not f.norm(r.get('input_vi')):raise ValueError('Empty input')
        r.setdefault('work_id','new_input')
    tokenizer=Tokenizer.from_pretrained(a.model);model=Model.from_pretrained(a.model,torch_dtype=torch.float32).to(device)
    f.write_lines(a.output,f.generate(model,tokenizer,rows,device,'visp_full'))

if __name__=='__main__':main()
