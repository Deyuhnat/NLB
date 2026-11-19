from pathlib import Path
import base64,hashlib,io,json,zipfile
import nbformat

ROOT=Path(__file__).resolve().parent
requirements='transformers==4.57.3\nsentencepiece==0.2.1\nsacrebleu==2.5.1\n'
(ROOT/'requirements.txt').write_text(requirements,encoding='utf-8')
buffer=io.BytesIO()
files=['full_finetune.py','test_finetune.py','requirements.txt','score_judgments.py',
       'data/train.jsonl','data/dev.jsonl','data/test.jsonl','data/manifest.json','data/excluded.json']
with zipfile.ZipFile(buffer,'w',zipfile.ZIP_DEFLATED) as z:
    for name in files:
        if (ROOT/name).exists():z.write(ROOT/name,name)
payload=buffer.getvalue();(ROOT/'visp_full_bundle.zip').write_bytes(payload)
encoded=base64.b64encode(payload).decode()
nb=nbformat.v4.new_notebook()
md=nbformat.v4.new_markdown_cell;c=nbformat.v4.new_code_cell
bootstrap=f'''from pathlib import Path
import os,sys,subprocess,zipfile,io,base64,hashlib,json
os.environ['USE_TF']='0'
payload=base64.b64decode({encoded!r})
assert hashlib.sha256(payload).hexdigest()=={hashlib.sha256(payload).hexdigest()!r}
work=Path('/kaggle/working/visp_full') if Path('/kaggle/working').exists() else Path.cwd()/'notebook_work'
work.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(io.BytesIO(payload)) as z:
    assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist())
    z.extractall(work)
print('Workspace:',work)
def run(*args):
    process=subprocess.Popen([sys.executable,'-u','-X','utf8',*args],cwd=work,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    for line in process.stdout: print(line,end='',flush=True)
    if process.wait(): raise RuntimeError('Command failed: '+' '.join(args))
run('-m','pip','install','--quiet','-r','requirements.txt')
print(json.loads((work/'data/manifest.json').read_text(encoding='utf-8'))['counts'])
'''
nb.cells=[md('''# ViSP — Full fine-tune trên dữ liệu đã review

**Bộ dữ liệu gồm 1.050 câu đã được nhóm review**

697 cặp train, 141 dev, 150 test sau khi tách pilot và nguồn mơ hồ. Cập nhật toàn bộ trọng số ViSP, không dùng LoRA. JFLEG/SEEDA là cơ sở đánh giá, không phải hai model được train.

Notebook chứa corpus riêng tư của nhóm, không có credentials database. Bật GPU T4 và Internet. Không công bố notebook/dữ liệu khi chưa kiểm tra quyền nguồn. Các bước train/test phía dưới thực thi thật, không dùng số liệu giả định.'''),
md('## 1. Khôi phục mã nguồn và dữ liệu đã khóa'),c(bootstrap),
md('## 2. Kiểm tra phần cứng và smoke test\nSmoke test tiny T5 kiểm tra optimizer và resume; không phải kết quả ViSP.'),
c("import torch\nprint('Torch:',torch.__version__)\nassert torch.cuda.is_available(), 'Bật Kaggle GPU trước khi training'\nprint(torch.cuda.get_device_name(0))\nrun('-m','unittest','-v','test_finetune')"),
md('## 3. Full fine-tune\nHai learning rate, chọn checkpoint trên dev. Batch giảm 2→1 nếu OOM; effective batch giữ 16. Checkpoint resume ở cuối mỗi epoch.'),
c("run('full_finetune.py','train','--data','data','--output','runs')"),
md('## 4. So ViSP gốc và ViSP sau fine-tune\nCùng beam search 5, không sampling. Chỉ mở test sau khi khóa checkpoint bằng dev.'),
c("run('full_finetune.py','evaluate','--data','data','--output','runs')\nprint((work/'runs/test_metrics.json').read_text(encoding='utf-8'))"),
md('## 5. Log và checkpoint\nModel đã train nằm trong `runs/lr_*/best`; xem `selected_model.json` để biết model được chọn. Chưa có judgments người đọc thì các metric harm/fluency để pending.'),
c("import matplotlib.pyplot as plt\nselection=json.loads((work/'runs/selected_model.json').read_text(encoding='utf-8'))\nfor result in selection['runs']:\n    history=result['history']\n    plt.plot([r['epoch'] for r in history],[r['dev']['balanced'] for r in history],label=str(result['lr']))\nplt.xlabel('Epoch');plt.ylabel('Balanced dev token loss');plt.legend();plt.show()\nprint('Chosen model:',selection['winner']['model_dir'])\nprint('Reload verification:',(work/'runs/reload_verification.json').read_text())")]
nb.metadata=dict(kernelspec=dict(display_name='Python 3',language='python',name='python3'),language_info=dict(name='python'),
    kaggle=dict(isGpuEnabled=True,isInternetEnabled=True,accelerator='gpu'))
nbformat.validate(nb)
nbformat.write(nb,ROOT/'ViSP_Full_Finetune_Kaggle.ipynb')
print('Built notebook and bundle',len(payload),'compressed bytes')
