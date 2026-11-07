import sys;from common import *
s=requests.Session();s.headers.update(UA)
url=sys.argv[1]; slug=sys.argv[2] if len(sys.argv)>2 else None
x=s.get(url,timeout=30)
t=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style).*?</\1>','',x.text,flags=re.S)))
print(x.status_code,x.url); i=t.find('ONE'); print(t[:100], '...', re.search(r'<h1[^>]*>(.*?)</h1>',x.text,re.S) and re.sub('<[^>]+>','',re.search(r'<h1[^>]*>(.*?)</h1>',x.text,re.S).group(1)))
for f in re.findall(r'<form.*?</form>',x.text,re.S):
    print(re.search(r'<form[^>]*>',f).group(0))
    for m in re.finditer(r'<(?:input|textarea|select|button)[^>]*>',f): print('  ',m.group(0)[:160])
i=t.find('Headline'); print(t[i-500:i+700])
