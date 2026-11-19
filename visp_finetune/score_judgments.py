"""Score adjudicated output judgments; preference decisions are not substituted."""
import argparse
from collections import Counter,defaultdict
import json
from pathlib import Path

def score(rows, key):
    mapping={r['form_id']:r for r in key}
    systems=defaultdict(Counter)
    seen=set()
    for r in rows:
        if r['form_id'] not in mapping: raise ValueError('Unknown form_id')
        if r['form_id'] in seen: raise ValueError('Supply one adjudicated judgment per form, keep raw ratings separately')
        seen.add(r['form_id']); k=mapping[r['form_id']]; c=systems[k['system_id']]; c['total']+=1
        out=k['output_side']; original='B' if out=='A' else 'A'
        if r.get('review_status')=='uncertain' or r.get('preservation_'+out)=='uncertain':
            c['uncertain']+=1; continue
        required=['needs_edit','naturalness_'+out,'naturalness_'+original,'preservation_'+out,'harm_'+out,'preference']
        if r.get('review_status')!='confirmed' or any(r.get(f) is None for f in required):
            c['missing_or_pending']+=1; continue
        if not isinstance(r['needs_edit'],bool) or not isinstance(r['harm_'+out],bool): raise ValueError('needs_edit/harm must be booleans')
        for side in ['A','B']:
            v=r['naturalness_'+side]
            if isinstance(v,bool) or not isinstance(v,(int,float)) or not 1<=v<=5: raise ValueError('Naturalness must be 1..5')
        if r['preservation_'+out] not in ['preserved','minor_change','major_change']: raise ValueError('Invalid preservation')
        if r['preference'] not in ['A','B','tie']: raise ValueError('Invalid preference')
        c['eligible']+=1
        harm=r['harm_'+out] or r['naturalness_'+out]<r['naturalness_'+original]
        safe=r['naturalness_'+out]>r['naturalness_'+original] and r['preservation_'+out]=='preserved' and not harm
        c['harm_n']+=harm
        if r['needs_edit']: c['needs_edit_n']+=1; c['safe_improvement_n']+=safe
        else: c['clean_n']+=1; c['clean_harm_n']+=harm
        c['tie' if r['preference']=='tie' else 'win' if r['preference']==out else 'loss']+=1
    result={}
    for name,c in systems.items():
        result[name]=dict(c)
        for metric,n,d in [('safe_improvement','safe_improvement_n','needs_edit_n'),('harm','harm_n','eligible'),('clean_harm','clean_harm_n','clean_n')]:
            result[name][metric]=c[n]/c[d] if c[d] else None
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--judgments',required=True); p.add_argument('--key',required=True); p.add_argument('--output',required=True)
    a=p.parse_args()
    rows=[json.loads(x) for x in Path(a.judgments).read_text(encoding='utf-8').splitlines() if x.strip()]
    key=json.loads(Path(a.key).read_text(encoding='utf-8'))
    result=score(rows,key)
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
