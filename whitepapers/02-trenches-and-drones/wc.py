import re,glob,html,markdown,sys
src="\n\n".join(open(p).read() for p in sorted(glob.glob("/workspace/whitepapers/02-trenches-and-drones/src-final/0*.md")))
if "<!-- BODY-START -->" in src and "<!-- BODY-END -->" in src: body=src.split("<!-- BODY-START -->")[1].split("<!-- BODY-END -->")[0]
else: body=src.split("<!-- BODY-START -->")[1]
h=markdown.markdown(body,extensions=["extra","sane_lists"])
text=html.unescape(re.sub(r"<[^>]+>"," ",h)).replace("☐"," ")
toks=[t for t in re.findall(r"\S+",text) if re.search(r"[A-Za-z0-9]",t)]
print("body words:",len(toks))
for p in sorted(glob.glob("/workspace/whitepapers/02-trenches-and-drones/src-final/0*.md")):
    t=open(p).read().replace("<!-- BODY-START -->","").replace("<!-- BODY-END -->","")
    h=markdown.markdown(t,extensions=["extra","sane_lists"])
    x=html.unescape(re.sub(r"<[^>]+>"," ",h))
    print(" ",p.split('/')[-1],len([q for q in re.findall(r"\S+",x) if re.search(r"[A-Za-z0-9]",q)]))
