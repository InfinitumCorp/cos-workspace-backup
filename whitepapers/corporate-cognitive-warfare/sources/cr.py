import sys,json,urllib.request,urllib.parse
for d in sys.argv[1:]:
    try:
        r=urllib.request.urlopen(urllib.request.Request("https://api.crossref.org/works/"+urllib.parse.quote(d),headers={'User-Agent':'mailto:info@theinfinitumcorporation.com'}),timeout=25)
        m=json.load(r)['message']
        print("OK",d,'|',m.get('title'),'|',[a.get('given','')+' '+a.get('family','') for a in m.get('author',[])][:6],'|',m.get('container-title'),m.get('volume'),m.get('issue'),m.get('page'),m.get('issued',{}).get('date-parts'))
    except Exception as e: print("FAIL",d,e)
