"""Conservative edit scoring: do not turn unreviewed edits into judgments."""
from collections import Counter,defaultdict
import argparse,json
from pathlib import Path

def score(rows):
    counts=defaultdict(Counter);seen=set()
    for r in rows:
        identity=(r['sample_id'],r['system_id'],tuple(r['input_span']),tuple(r['output_span']))
        if identity in seen:raise ValueError('Duplicate edit judgment')
        seen.add(identity);c=counts[r['system_id']];c['performed']+=1
        value=r.get('judgment')
        if value not in [None,'accepted','rejected','uncertain']:raise ValueError('Invalid judgment')
        if r.get('review_status')=='confirmed' and value in ['accepted','rejected']:c[value]+=1
        elif value=='uncertain' or r.get('review_status')=='uncertain':c['uncertain']+=1
        else:c['pending']+=1
    result={}
    for system,c in counts.items():
        known=c['accepted']+c['rejected']
        result[system]=dict(c,confirmed_precision=c['accepted']/known if known else None,
            edit_precision=c['accepted']/c['performed'] if c['performed'] and not c['pending'] and not c['uncertain'] else None)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--judgments',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    rows=[json.loads(x) for x in Path(a.judgments).read_text(encoding='utf-8').splitlines() if x.strip()]
    Path(a.output).write_text(json.dumps(score(rows),ensure_ascii=False,indent=2),encoding='utf-8')
