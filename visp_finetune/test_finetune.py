import tempfile
from pathlib import Path
import unittest
import full_finetune as f

class DataTests(unittest.TestCase):
    def test_balanced_sampling_reproducible(self):
        rows=[dict(changed=True)]*2+[dict(changed=False)]*5
        a=f.sample_indices(rows,42,952)
        self.assertEqual(a,f.sample_indices(rows,42,952))
        self.assertEqual(sum(rows[i]['changed'] for i in a),476)
        self.assertNotEqual(a,f.sample_indices(rows,43,952))

    def test_no_missing_group_silently_sampled(self):
        with self.assertRaises(ValueError):f.sample_indices([dict(changed=True)],42,10)

    def test_token_limit_no_truncation(self):
        class Tokenizer:
            def __call__(self,text=None,text_target=None,**kwargs):
                assert kwargs.get('truncation') is False
                return {'input_ids':list(range(len(text or text_target)))}
        rows=[dict(sample_id='a',input_vi='a',target_vi='a'),dict(sample_id='b',input_vi='a'*600,target_vi='b')]
        good,bad=f.encode(rows,Tokenizer())
        self.assertEqual([r['sample_id'] for r in good],['a'])
        self.assertEqual(bad[0]['sample_id'],'b')

    def test_automatic_metrics_not_quality_judgments(self):
        rows=[dict(sample_id='a',changed=True,input_vi='câu cũ',target_vi='câu mới')]
        p=[dict(sample_id='a',output_vi='câu mới',status='ok')]
        m=f.metrics(rows,p)
        self.assertEqual(m['all']['exact_match'],1)
        self.assertEqual(m['identity']['n'],0)
        self.assertIsNone(m['quality_judgments']['harm'])

    def test_frozen_data(self):
        base=Path(__file__).resolve().parent/'data'
        manifest=f.read(base/'manifest.json')
        groups={};ids=set()
        for split in ['train','dev','test']:
            self.assertEqual(f.sha(base/f'{split}.jsonl'),manifest['files'][f'{split}.jsonl'])
            for r in f.lines(base/f'{split}.jsonl'):
                self.assertNotIn(r['sample_id'],ids);ids.add(r['sample_id'])
                self.assertEqual(groups.setdefault(r['group_id'],split),split)
                self.assertEqual(r['changed'],f.norm(r['input_vi'])!=f.norm(r['target_vi']))

    def test_real_optimizer_reload_and_resume(self):
        with tempfile.TemporaryDirectory() as folder:
            f.smoke(folder)
            result=f.read(Path(folder)/'smoke_result.json')
            self.assertTrue(result['all_parameters_trainable'])
            self.assertTrue(result['resume_next_step_equal'])
            self.assertEqual(result['parameter_tensors'],result['gradient_tensors'])

    def test_full_epoch_loop_with_warmup(self):
        import torch
        from transformers import T5Config,T5ForConditionalGeneration
        from unittest.mock import patch
        class Tokenizer:
            def pad(self,rows,**kwargs):
                ids=torch.tensor([r['input_ids'] for r in rows])
                return dict(input_ids=ids,attention_mask=torch.ones_like(ids))
            def save_pretrained(self,path):return None
        config=dict(f.CONFIG,epoch_draws=16,epochs=2)
        rows=[dict(sample_id=str(i),input_ids=[2,3,1],labels=[4,5,1],changed=bool(i%2)) for i in range(4)]
        model=T5ForConditionalGeneration(T5Config(vocab_size=64,d_model=32,d_ff=64,num_layers=1,num_decoder_layers=1,num_heads=2,decoder_start_token_id=0,pad_token_id=0,eos_token_id=1,dropout_rate=0))
        with tempfile.TemporaryDirectory() as folder,patch.dict(f.CONFIG,config):
            result=f.train_run(model,Tokenizer(),rows,rows,'cpu',folder,1e-4,'fixture')
            self.assertEqual(len(result['history']),2)
            proof=f.read(Path(folder)/'full_training_proof.json')
            self.assertGreater(proof['changed_sentinels'],0)
            again=f.train_run(model,Tokenizer(),rows,rows,'cpu',folder,1e-4,'fixture')
            self.assertEqual(result['history'],again['history'])

if __name__=='__main__':unittest.main()
