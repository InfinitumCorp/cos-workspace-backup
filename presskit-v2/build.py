import html, os, sys, datetime, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data2; D = data2.D
E = html.escape
def a(url, text=None): return f'<a href="{E(url)}">{E(text or url)}</a>'
def fmt_date(d):
    if len(d) == 7: return datetime.date(int(d[:4]), int(d[5:]), 1).strftime('%b %Y')
    return datetime.date(*map(int, d.split('-'))).strftime('%b %-d, %Y')
def linkify(t):
    out = ''
    for part in re.split(r'(https?://[^\s|]+|\S+@\S+\.com)', t):
        if part.startswith('http'): out += a(part)
        elif '@' in part: out += a('mailto:' + part, part)
        else: out += E(part)
    return out
def kv(rows):
    def v(k, x):
        if k == 'Phone': return a('tel:+1' + x.replace('-', ''), x)
        if '@' in x and ' ' not in x: return a('mailto:' + x, x)
        if x.startswith('http'): return a(x)
        return E(x)
    return '<table class="kv">' + ''.join(f'<tr><th>{E(k)}</th><td>{v(k, x)}</td></tr>' for k, x in rows) + '</table>'
def grid(head, rows, cls=''):
    h = ''.join(f'<th>{E(x)}</th>' for x in head)
    return f'<table class="grid {cls}"><thead><tr>{h}</tr></thead><tbody>' + ''.join('<tr>' + ''.join(rows_td(r)) + '</tr>' for r in rows) + '</tbody></table>'
def rows_td(r):
    for i, x in enumerate(r):
        if isinstance(x, str) and x.startswith('http'): yield f'<td class="url">{a(x)}</td>'
        elif i == 2 and re.match(r'\w{3} \d', x or ''): yield f'<td class="nw">{E(x)}</td>'
        else: yield f'<td>{E(x)}</td>'

S = []
def sec(i, t, b): S.append((i, t, b))
sec('facts', 'Fast facts', kv(D.FAST_FACTS))
sec('about', 'About Infinitum Corporation', f'<p class="lead">{linkify(D.BOILERPLATE)}</p><p class="small">Official boilerplate.</p>')
bio = ''.join(f'<p>{E(p)}</p>' for p in D.BIO)
bio = f'''<div class="bio"><figure><img src="assets/william-headshot.jpg" alt="William Aaron Turner"><figcaption>William Aaron Turner, Founder and President, Infinitum Corporation</figcaption></figure>
<div class="biotext">{bio}<blockquote class="pull"><p>\u201cI\u2019m not a journalist. I\u2019m a businessman.\u201d</p><cite>William Aaron Turner</cite></blockquote></div></div>
<h3>Sources</h3><ul class="src">''' + ''.join(f'<li>{E(n)}: {a(u)}</li>' for n, u in D.BIO_SOURCES) + '</ul>'
sec('bio', 'Founder: William Aaron Turner', bio)
s = '<h3>Practice areas</h3><ul class="cards">' + ''.join(f'<li>{E(x)}</li>' for x in D.SERVICES_CORE) + '</ul>'
s += '<h3>Core competencies</h3><ul class="cols">' + ''.join(f'<li>{E(x)}</li>' for x in D.SERVICES_COMPETENCIES) + '</ul>'
s += f'<p class="small">Source: {E(D.SERVICES_SOURCE[0])}: {a(D.SERVICES_SOURCE[1])}</p>'
sec('services', 'Services', s)
sec('contact', 'Media contact', kv(D.CONTACT))
sec('channels', 'Official channels', grid(['Platform', 'Account', 'Link', 'Note'], D.CHANNELS, 'ch'))
p = '<h3>Blogs</h3><ul class="src">' + ''.join(f'<li>{E(n)}: {a(u)}</li>' for n, u in D.BLOG_HOMES) + '</ul>'
p += grid(['Title', 'Outlet', 'Date', 'Link'], [(t, o, fmt_date(d), u) for t, o, d, u in D.PUBLICATIONS])
p += '<p class="small">Blog dates are the publication dates shown in each blog\u2019s feed.</p>'
sec('publications', 'Publications, whitepapers and articles', p)
sec('releases', 'Press releases', grid(['Title', 'Outlet', 'Date', 'Link'], [(t, o, fmt_date(d), u) for t, o, d, u in D.RELEASES]) + '<p class="small">Dates as shown on each outlet\u2019s page. Links checked Nov 2, 2026.</p>')
m = '<h3>Syndicated pickups</h3>' + grid(['Title', 'Outlet', 'Date', 'Link'], [(t, o, fmt_date(d), u) for t, o, d, u in D.COVERAGE])
m += f'<p>{E(D.COVERAGE_NOTE)}</p><h3>Russian media</h3><p>{E(D.RUSSIAN_MEDIA_NOTE)}</p>'
sec('coverage', 'Media coverage', m)
q = ''.join(f'<blockquote><p>\u201c{E(t)}\u201d</p><cite>William Aaron Turner, {E(st)}, {E(o)}, {fmt_date(d)}. {a(u)}</cite></blockquote>' for t, st, o, d, u, _ in D.QUOTES)
q += '<h3>From company press releases</h3>' + ''.join(f'<blockquote><p>\u201c{E(t)}\u201d</p><cite>William Aaron Turner, {E(st)}, {E(o)}, {fmt_date(d)}. {a(u)}</cite></blockquote>' for t, st, o, d, u in D.RELEASE_QUOTES)
sec('quotes', 'Quotes', q)
s2 = grid(['Asset', 'File', 'Public source'], [(n, f, u or 'Included with this kit') for n, f, u in D.ASSETS], 'assets')
s2 += '<div class="swatch"><div class="blk"><img src="assets/infinitum-logo-stacked-white.png" alt="Infinitum logo, white"></div><div class="wht"><img src="assets/infinitum-logo-stacked-black.png" alt="Infinitum logo, black"></div></div>'
s2 += f'<p>{E(D.ASSETS_NOTE)}</p>'
sec('assets', 'Downloadable assets', s2)

CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'style.css')).read()
hdr = '<div class="hdr"><img src="assets/infinitum-logo-horizontal-white.png" alt="Infinitum Corporation"></div>'
ftr = f'<div class="ftr"><img src="assets/infinitum-wordmark-white.png" alt="INFINITUM"><span>Press Kit 2026 \u00b7 {E(D.WEB.replace("https://", ""))} \u00b7 {E(D.PHONE)}</span></div>'
cover = f'''<div class="cover">
<img class="clogo" src="assets/infinitum-logo-horizontal-white.png" alt="Infinitum Corporation">
<div class="cphoto"><img src="assets/cover-photo.jpg" alt="William Aaron Turner"></div>
<div class="ctext"><div class="kick">Press Kit \u00b7 November 2026</div>
<h1>William Aaron<br>Turner</h1>
<p class="role">Founder and President, Infinitum Corporation</p>
<p class="tag">Technology and security consulting, including Corporate Cognitive Warfare. Headquartered in Washington, DC.</p></div>
<div class="cfoot"><div class="crule"></div>
<div class="cmeta"><div>{E(D.ADDRESS)}<br>{E(data2.HOURS)}</div>
<div class="r">{a("tel:+12027299509", D.PHONE)}<br>{a("mailto:" + D.EMAIL, D.EMAIL)}<br>{a(D.WEB, D.WEB.replace("https://", ""))}</div></div></div></div>'''
toc = '<div class="toc"><div class="num">Contents</div><h2>Contents</h2><div class="rule"></div><ol>' + ''.join(f'<li><a href="#{i}">{E(t)}</a></li>' for i, t, _ in S) + '</ol></div>'
body = ''.join(f'<section id="{i}"><div class="num">Section {n + 2:02d}</div><h2>{E(t)}</h2><div class="rule"></div>{h}</section>' for n, (i, t, h) in enumerate(S))
doc = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Infinitum Corporation Press Kit 2026: William Aaron Turner</title><style>{CSS}</style></head><body>{hdr}{ftr}{cover}{toc}{body}</body></html>'
open('Infinitum-Press-Kit-2026.html', 'w').write(doc)
import weasyprint
weasyprint.HTML('Infinitum-Press-Kit-2026.html', base_url='.').write_pdf('Infinitum-Press-Kit-2026.pdf')
print('ok')
