import json, re
NAME="Infinitum Corporation"
ST="1629 K Street NW, Suite 300"; CITY="Washington"; REG="DC"; ZIP="20006"
PHONE_D="202-729-9509"; PHONE_E="+1-202-729-9509"
EMAIL="info@theinfinitumcorporation.com"
SITE="https://www.theinfinitumcorporation.com"
X="https://x.com/infinitumceo"; TG="https://t.me/infinitumcorporation"; DC="https://discord.gg/QVT7dWHUQa"
UF="https://ukrainianfiles.blogspot.com/"; WP="https://infinitumwhitepapers.blogspot.com/"
WHOP="https://whop.com/infinitum-corporation/"; GH="https://github.com/InfinitumCorp"
SERV=["Cybersecurity consulting","Network security and network defense","Ethical hacking and vulnerability assessment","IT and security consulting","AI applications for security operations","Strategic risk assessment","Defense technology advisory"]
out={}
# --- NAP json
nap={"name":NAME,"legal_display":"INFINITUM CORPORATION (use 'Infinitum Corporation' in prose; ALL CAPS only where a registry requires it)","address":{"street":ST,"city":CITY,"state":REG,"zip":ZIP,"country":"US"},"phone_display":PHONE_D,"phone_e164":PHONE_E,"email":EMAIL,"website":SITE,"hours":"Mon–Fri 9:00 AM–9:00 PM; closed Sat–Sun","founder":"William Aaron Turner","headquarters":"Washington, DC (Moscow is an operating location only)","profiles":{"x":X,"telegram":TG,"discord":DC,"whitepapers_blog":WP,"ukraine_files_blog":UF,"whop":WHOP,"github":GH},"legacy_numbers_seen_live":{"(202) 681-0120":"website footer, tel: links and LocalBusiness JSON-LD (2026-10-26)","(202) 980-9300":"/workspace/infinitum_directories.md 'canonical' NAP and Google Business Profile draft","(614) 216-2724":"website builder data (whatsapp_number_national) - not seen as visible text"}}
json.dump(nap,open('nap-canonical.json','w'),indent=2)
# --- JSON-LD website
sameas=[X,TG,DC,WP,UF,WHOP,GH]
ld={"@context":"https://schema.org","@graph":[
 {"@type":["Organization","ProfessionalService"],"@id":SITE+"/#organization","name":NAME,"legalName":"INFINITUM CORPORATION","url":SITE,"logo":SITE+"/logo.png","image":"https://img77.uenicdn.com/image/upload/v1712089276/business/452aa430-3f31-4de7-a343-b0043af83a58.jpg",
  "description":"Technology and security consulting firm headquartered in Washington, DC, with Moscow as an operating location. Cybersecurity, network defense, ethical hacking and vulnerability assessment, AI for security operations, and defense technology advisory. Open Mon–Fri 9 AM–9 PM.",
  "email":EMAIL,"telephone":PHONE_E,"slogan":"We protect what matters most.",
  "address":{"@type":"PostalAddress","streetAddress":ST,"addressLocality":CITY,"addressRegion":REG,"postalCode":ZIP,"addressCountry":"US"},
  "geo":{"@type":"GeoCoordinates","latitude":38.9029022,"longitude":-77.0378701},
  "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens": "09:00","closes": "21:00"}],
  "areaServed":"Worldwide","founder":{"@id":SITE+"/#william-aaron-turner"},
  "contactPoint":[{"@type":"ContactPoint","contactType":"customer service","telephone":PHONE_E,"email":EMAIL,"availableLanguage":["English","Russian"],"hoursAvailable":{"@type":"OpeningHoursSpecification","dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens": "09:00","closes": "21:00"}}],
  "knowsAbout":["Cybersecurity consulting","Network defense","Ethical hacking","Vulnerability assessment","Artificial intelligence for security operations","Strategic risk assessment","Defense technology advisory"],
  "sameAs":sameas},
 {"@type":"Person","@id":SITE+"/#william-aaron-turner","name":"William Aaron Turner","jobTitle":"Founder and President","worksFor":{"@id":SITE+"/#organization"},"sameAs":[X,"https://linkedin.com/in/william-aaron-t-726076244"]},
 {"@type":"WebSite","@id":SITE+"/#website","url":SITE,"name":NAME,"publisher":{"@id":SITE+"/#organization"},"inLanguage":"en-US"}]}
s=json.dumps(ld,indent=2)
open('website-jsonld.html','w').write("<!-- Infinitum Corporation: site-wide JSON-LD. Paste once in the site builder's custom <head>/code-injection box (Ueni: verify it allows scripts). REMOVE the builder's existing LocalBusiness block if it cannot be edited: it lists phone +12026810120, sameAs x.com/infinitumusa and instagram. If the builder's primary domain is non-www, replace https://www.theinfinitumcorporation.com with https://theinfinitumcorporation.com everywhere in this file. Logo URL below is a placeholder: swap for the real logo asset URL once uploaded. -->\n<script type=\"application/ld+json\">\n"+s+"\n</script>\n")
# --- website meta copy
pages=[("Home","/","Cybersecurity Consulting in Washington, DC | Infinitum","Infinitum Corporation: cybersecurity, ethical hacking, network defense and defense technology advisory. HQ Washington, DC. Open Mon–Fri 9 AM–9 PM. 202-729-9509."),
("About","/about-us/private-intelligence-and-security-consultant-6343230","About Infinitum Corporation | Washington, DC Security Firm","Washington, DC security and technology consulting firm led by founder William Aaron Turner. Cybersecurity, risk and defense technology advisory. Open Mon–Fri 9 AM–9 PM."),
("Our services","/about-us/our-services-6343231","Security and IT Consulting Services | Infinitum Corp","Cybersecurity consulting, network defense, ethical hacking, AI for security operations and strategic risk assessment from Washington, DC. Open Mon–Fri 9 AM–9 PM."),
("Experts in IT","/about-us/experts-in-it-6343232","IT and Security Experts, Washington, DC | Infinitum","Meet the IT and security experts at Infinitum Corporation: network defense, vulnerability assessment and secure systems for government and business."),
("IT consulting","/services/consulting-services/information-technology-consulting-150186338","IT Consulting in Washington, DC | Infinitum Corporation","IT consulting for government and business from Washington, DC: systems design, secure architecture and AI-assisted operations. Call 202-729-9509."),
("Security consulting","/services/consulting-services/security-consulting-150186339","Security Consulting in Washington, DC | Infinitum Corp","Security consulting from Washington, DC: risk assessment, network defense and secure systems for government and business. Open Mon–Fri 9 AM–9 PM. 202-729-9509."),
("Ethical hacking","/services/consulting-services/ethical-hacking-150186341","Ethical Hacking and Pen Testing, Washington DC | Infinitum","Ethical hacking and vulnerability assessment: we find your system's failure points and report how to fix them. Washington, DC. Open Mon–Fri 9 AM–9 PM."),
("Computer engineering","/services/consulting-services/computer-engineering-150186340","Computer Engineering Consulting | Infinitum Corporation","One-to-one computer engineering consulting: we define your challenges and build achievable plans. Washington, DC. Open Mon–Fri 9 AM–9 PM. 202-729-9509."),
("Reviews","/reviews","Client Reviews | Infinitum Corporation, Washington, DC","Read client reviews of Infinitum Corporation, a Washington, DC cybersecurity and technology consulting firm. Open Mon–Fri 9 AM–9 PM. Call 202-729-9509."),
("Booking","/booking","Book a Security Consultation | Infinitum Corporation","Book a consultation with Infinitum Corporation in Washington, DC. Cybersecurity, IT and defense technology advisory. Open Mon–Fri 9 AM–9 PM. 202-729-9509.")]
L=["# Website title and meta description copy (theinfinitumcorporation.com)\n","Counts are computed (title <= 60 chars so Google rarely truncates; description <= 160). Apply in the site builder (needs CTO TechBot / William login). Page paths are from the live sitemap.xml (fetched 2026-10-26). Current live title on every page ends with 'IT Consultant in Washington, D.C.'; current descriptions lead with 'Searching for IT Consultancy in Washington, D.C.?'.\n","| Page | Path | Title | chars | Meta description | chars |","|---|---|---|---|---|---|"]
bad=[]
for n,p,t,d in pages:
    L.append(f"| {n} | `{p}` | {t} | {len(t)} | {d} | {len(d)} |")
    if len(t)>60 or len(d)>160: bad.append((n,len(t),len(d)))
L.append("\nLeave the other builder pages (commercial construction, facility management, logistics, healthcare IT, procurement, advanced surveillance, policies) for a second pass: the wording of 'advanced surveillance' should be reviewed by William before it is optimized (directories note: avoid weapons/surveillance-heavy wording on listings).\n")
L.append("Home H1 currently 'INFINITUM CORPORATION'; H2 'A Washington, D.C. Based Private Intelligence and Security Contractor, Powered by AI.' Suggested H1: 'Infinitum Corporation: Cybersecurity and Technology Consulting in Washington, DC'. Add one visible line in the footer: '1629 K Street NW, Suite 300, Washington, DC 20006 | 202-729-9509 | Mon–Fri 9–9 | info@theinfinitumcorporation.com' plus links to Telegram, X, Discord.\n")
open('website-meta-copy.md','w').write("\n".join(L))
print("website meta over limit:",bad)
# --- llms.txt
llms=f"""# {NAME}

> Technology and security consulting firm headquartered in Washington, DC (1629 K Street NW, Suite 300, Washington, DC 20006). Moscow is an operating location only. Open Mon–Fri 9 AM–9 PM. Phone {PHONE_D}. Email {EMAIL}. Founder and President: William Aaron Turner.

Services: cybersecurity consulting; network security and network defense; ethical hacking and vulnerability assessment; IT and security consulting; AI applications for security operations; strategic risk assessment; defense technology advisory.

## Official properties
- [Website]({SITE}): services, about, booking
- [Whitepapers blog]({WP}): free security and technology whitepapers
- [The Ukraine Files blog]({UF}): sourced analysis by William Aaron Turner
- [Telegram channel]({TG}): announcements and briefings
- [X]({X}): William Aaron Turner, CEO
- [Discord community]({DC})
- [Whop store]({WHOP}): playbooks and handbooks (educational and analytical content only)
- [GitHub]({GH})

## Contact
- Phone: {PHONE_D}
- Email: {EMAIL}
- Address: {ST}, {CITY}, {REG} {ZIP}
- Hours: Mon–Fri 9:00 AM–9:00 PM; closed Sat–Sun
"""
open('llms.txt','w').write(llms)
# --- profile copy
def cnt(s): return len(s)
tgdesc=f"Infinitum Corporation: cybersecurity & defense-technology consulting. HQ Washington, DC. Open Mon–Fri 9 AM–9 PM. Briefings on cyber, counter-UAS, geopolitics. theinfinitumcorporation.com | X @infinitumceo | 202-729-9509"
tgtitle="Infinitum Corporation | Cybersecurity, Defense Tech & Geopolitics"
xbio="CEO, Infinitum Corporation. Cybersecurity & defense technology consulting. HQ Washington, DC (also operating in Moscow). Open Mon–Fri 9 AM–9 PM. 202-729-9509"
xbio2="CEO @ Infinitum Corporation | Cybersecurity & defense tech consulting | HQ Washington, DC | Mon–Fri 9–9 | t.me/infinitumcorporation"
disc=f"Official Infinitum Corporation community: cybersecurity, defense technology and AI for security operations. HQ Washington, DC. Open Mon–Fri 9 AM–9 PM. Website: theinfinitumcorporation.com | Telegram: t.me/infinitumcorporation"
gbp=("Infinitum Corporation is a technology and security consulting firm headquartered in Washington, DC at 1629 K Street NW, Suite 300. We provide cybersecurity consulting, network defense, ethical hacking and vulnerability assessment, IT consulting, AI applications for security operations, strategic risk assessment and defense technology advisory for government agencies and businesses. Founded by William Aaron Turner. Mon–Fri 9:00 AM–9:00 PM; closed Sat–Sun. Call 202-729-9509 or email info@theinfinitumcorporation.com.")
li_tag="Cybersecurity and defense technology consulting | Washington, DC | Mon–Fri 9 AM–9 PM"
li_about=("Infinitum Corporation is a technology and security consulting firm headquartered in Washington, DC (1629 K Street NW, Suite 300), with Moscow as an operating location. We work with government agencies and businesses on cybersecurity consulting, network security and defense, ethical hacking and vulnerability assessment, IT consulting, AI applications for security operations, strategic risk assessment and defense technology advisory.\n\nFounded by William Aaron Turner. Open Mon–Fri 9 AM–9 PM.\nPhone: 202-729-9509 | Email: info@theinfinitumcorporation.com\nWebsite: https://www.theinfinitumcorporation.com\nTelegram: https://t.me/infinitumcorporation | X: https://x.com/infinitumceo | Discord: https://discord.gg/QVT7dWHUQa\nWhitepapers: https://infinitumwhitepapers.blogspot.com/")
li_head="CEO and Founder, Infinitum Corporation | Cybersecurity and Defense Technology Consulting | Washington, DC"
whop=("Infinitum Corporation is a technology and security consulting firm headquartered in Washington, DC, with Moscow as an operating location. Open Mon–Fri 9 AM–9 PM. Our playbooks, handbooks and templates cover cybersecurity, network defense, ethical hacking, AI for security operations, strategic risk assessment and defense technology analysis. Practical, integrated security thinking for professionals, analysts and builders. Educational and analytical content only. Questions: info@theinfinitumcorporation.com or 202-729-9509. Website: theinfinitumcorporation.com | Telegram: t.me/infinitumcorporation")
yt=("Infinitum Corporation: cybersecurity and defense-technology consulting, headquartered in Washington, DC. Open Mon–Fri 9 AM–9 PM.\n\nWebsite: https://www.theinfinitumcorporation.com\nTelegram: https://t.me/infinitumcorporation\nX: https://x.com/infinitumceo\nDiscord: https://discord.gg/QVT7dWHUQa\nWhitepapers: https://infinitumwhitepapers.blogspot.com/\nContact: info@theinfinitumcorporation.com | 202-729-9509\n\nWilliam Aaron Turner, Founder and President.")
descs={"50":"Cybersecurity and defense tech consulting, DC","160":"Infinitum Corporation: cybersecurity, ethical hacking, network defense and defense technology consulting. HQ Washington, DC. Open Mon–Fri 9 AM–9 PM. 202-729-9509.","250":"Infinitum Corporation is a Washington, DC technology and security consulting firm: cybersecurity, network defense, ethical hacking, AI for security operations and defense technology advisory. Open Mon–Fri 9 AM–9 PM. 202-729-9509. theinfinitumcorporation.com","750":gbp}
checks={"Telegram description (max 255)":(tgdesc,255),"Telegram title (max 128)":(tgtitle,128),"X bio A (max 160)":(xbio,160),"X bio B (max 160)":(xbio2,160),"Discord server description long (soft 300)":(disc,300),"Discord Community-discovery description (max 120)":("Infinitum Corporation: cybersecurity and defense tech consulting. HQ Washington, DC. Open Mon–Fri 9 AM–9 PM.",120),"GBP description (max 750)":(gbp,750),"LinkedIn tagline (max 120)":(li_tag,120),"LinkedIn personal headline (max 220)":(li_head,220),"LinkedIn company About (max 2000)":(li_about,2000),"Whop description (soft 1000)":(whop,1000),"YouTube description (max 1000 channel)":(yt,1000),"Dir 50":(descs['50'],50),"Dir 160":(descs['160'],160),"Dir 250":(descs['250'],250),"Dir 750":(descs['750'],750)}
for k,(v,m) in checks.items():
    print(k,len(v),"OK" if len(v)<=m else "OVER")
P=["# Profile and directory copy, ready to paste (nothing here has been applied or posted)\n","All copy: DC headquarters, Moscow as an operating location only (only where it is already public on that profile), open Mon–Fri 9 AM–9 PM, phone 202-729-9509. Character counts computed by script. Anything marked APPROVAL needs William's yes before it goes live. No new public offers appear in this file.\n"]
for k,(v,m) in checks.items():
    P.append(f"## {k}: {len(v)} chars\n```\n{v}\n```\n")
P.append("## Directory categories and services (use identically everywhere)\n- Primary category: IT security service / Computer security service. Secondary: Information technology consultant, Management consultant (only if the directory requires one more).\n- Services: "+"; ".join(SERV)+".\n- Hours: Mon–Fri 09:00–21:00; Sat–Sun closed (schedule fields).\n- Year/founder: William Aaron Turner. Keep wording to cybersecurity, risk, IT security and defense technology advisory. Do NOT use CQB, training, weapons or surveillance wording on listings (moderation risk, per infinitum_directories.md section 7).\n")
P.append("## Telegram pinned-post text (APPROVAL for positioning change)\n```\nInfinitum Corporation: cybersecurity and defense-technology consulting. HQ: 1629 K Street NW, Suite 300, Washington, DC 20006. Open Mon–Fri 9 AM–9 PM. 202-729-9509.\nWebsite: https://www.theinfinitumcorporation.com\nX: https://x.com/infinitumceo | Discord: https://discord.gg/QVT7dWHUQa\nWhitepapers: https://infinitumwhitepapers.blogspot.com/\n```\n")
P.append("## GBP Q&A seed (Google lets the owner post and answer; only if approved)\n- Q: What are Infinitum Corporation's hours? A: Monday to Friday, 9 AM to 9 PM ET; closed Saturday and Sunday. Call 202-729-9509.\n- Q: What services do you provide? A: Cybersecurity consulting, network defense, ethical hacking and vulnerability assessment, IT consulting, AI for security operations, strategic risk assessment and defense technology advisory.\n- Q: Where are you headquartered? A: 1629 K Street NW, Suite 300, Washington, DC 20006.\n")
open('profile-and-directory-copy.md','w').write("\n".join(P))
# --- UTM
u=["# UTM link table (GA4 / Search Console friendly; lowercase, no spaces)\n","Use one link per placement so GA4 (website) can attribute visits. Only the website accepts UTMs for measurement; do not add UTMs to t.me or discord.gg links (they ignore them).\n","| Placement | Link |","|---|---|"]
for src,med in [("telegram","social"),("x","social"),("linkedin","social"),("discord","social"),("whop","referral"),("youtube","social"),("press","pr"),("email","email"),("blog-whitepapers","referral"),("blog-ukrainefiles","referral"),("gbp","organic"),("bing-places","organic")]:
    u.append(f"| {src} | {SITE}/?utm_source={src}&utm_medium={med}&utm_campaign=seo-oct2026 |")
open('utm-links.md','w').write("\n".join(u)+"\n")
# validate JSON-LD
re.sub(r'<[^>]+>','',open('website-jsonld.html').read())
json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',open('website-jsonld.html').read(),re.S).group(1)); print("jsonld parses")
