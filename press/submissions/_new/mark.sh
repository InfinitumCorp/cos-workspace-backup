#!/bin/bash
# usage: mark.sh NN msgid
python3 - "$1" "$2" <<'P'
import sys,re,datetime
n,mid=sys.argv[1],sys.argv[2]; p='/workspace/press/submissions/index.md'; L=open(p).read().split('\n')
ts=datetime.datetime.now().strftime('%d %b %Y %H:%M MSK')
i=max(k for k,l in enumerate(L) if l.startswith(f'| {n} |'))
L[i]=L[i].replace('| pending-send | — |',f'| SENT {ts} | {mid} |'); open(p,'w').write('\n'.join(L))
P
