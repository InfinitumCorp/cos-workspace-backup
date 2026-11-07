import requests,sys,json
qs=[l.strip() for l in open(sys.argv[1]) if l.strip()]
out=[]
for q in qs:
    try:
        r=requests.get('https://api.crossref.org/works',params={'query.bibliographic':q,'rows':2,'mailto':'theinfinitumcorp@gmail.com'},timeout=30).json()
        for it in r['message']['items'][:1]:
            a='; '.join(f"{x.get('family','')}, {x.get('given','')}" for x in it.get('author',[]))
            y=(it.get('issued',{}).get('date-parts',[[None]])[0][0])
            print(f"Q: {q}\n  -> {a} ({y}) {it.get('title',[''])[0]} | {(it.get('container-title') or [''])[0]} {it.get('volume','')}({it.get('issue','')}) pp.{it.get('page','')} doi:{it.get('DOI')} type:{it.get('type')}\n")
    except Exception as e: print('ERR',q,e)
