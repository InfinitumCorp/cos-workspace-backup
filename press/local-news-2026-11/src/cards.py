import json,re
OUT='/workspace/press/local-news-2026-11'
d=json.load(open(OUT+'/src/_rows.json'))
cards=[];skipped=[]
for e in d['emails']:
    reg,n,name,to,subj,att,slug,kind=e
    m=re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+',to)
    if not m: skipped.append((name,'no published email address')); continue
    addr=m[0]
    md=open(f'{OUT}/drafts/{slug}.md').read().split('---\n',1)[1].strip()
    body=md
    head=''
    if body.startswith('# '):
        head,body=body.split('\n',1);head=head[2:].strip();body=body.strip()
    k=kind.lower()
    img=att!='none'
    note="A high-resolution image is available on request." if img else ""
    if 'op-ed' in k or k.startswith('article'):
        excl=name.split(' (')[0]
        wcount=len(re.findall(r"\b[\w'’-]+\b",body.split('\n---\n')[0].split('\nSources:')[0]))
        intro=f"Dear Editors,\n\nPlease consider the following original {'op-ed' if 'op-ed' in k else 'article'} ({wcount} words), submitted exclusively to {excl}." + (" "+note if img else "")
        body=intro+"\n\n"+head+"\n\n"+body.replace('\n---\n','\n')
    elif 'press release' in k or 'article' in k:
        intro="Hello,\n\nPlease find below a press release for your consideration."+(" "+note if img else "")
        body=intro+"\n\n"+head+"\n\n"+body
    else:
        if img: body=body.replace("\n\nReach me at","\n\n"+note+"\n\nReach me at") if "Reach me at" in body else body+"\n\n"+note
    body=re.sub(r'\n{3,}','\n\n',body).strip()
    cards.append({"platform":"email","providerIdentifier":"user-Gmail","to":[addr],"subject":subj,"body":body,"proposedRule":f"Emails to {addr}","_outlet":f"{name} ({reg} #{n})"})
json.dump({"cards":cards,"skipped":skipped},open(OUT+'/cards.json','w'),indent=1,ensure_ascii=False)
print(len(cards),skipped)
for c in cards: print(c['to'][0],'|',c['subject'][:70])
