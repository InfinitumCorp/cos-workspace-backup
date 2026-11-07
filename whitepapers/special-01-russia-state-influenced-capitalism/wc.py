import re,glob,html,markdown
d="/workspace/whitepapers/special-01-russia-state-influenced-capitalism/src-final/"
src="\n\n".join(open(p).read() for p in sorted(glob.glob(d+"0*.md")))
body=src.split("<!-- BODY-START -->")[1].split("<!-- BODY-END -->")[0]
h=markdown.markdown(body,extensions=["extra","sane_lists"])
text=html.unescape(re.sub(r"<[^>]+>"," ",h))
toks=[t for t in re.findall(r"\S+",text) if re.search(r"[A-Za-z0-9]",t)]
print("body words:",len(toks))
