import base64, html, json, mimetypes, pathlib

BASE = pathlib.Path(__file__).parent
ASSETS = BASE / "assets"

# ------------------------------------------------------------------ CONTENT
P = dict(
    name="Srijan Srivastav",
    role="Data Analyst",
    roles=["Data Analyst", "Business Analyst", "Python Developer", "Web Developer"],
    tagline="Python • SQL • Excel • Data Visualization",
    location="Jaunpur, Uttar Pradesh, India",
    email="srivastav.srijan@ieee.org",
    phone="8853942888",
    whatsapp="918853942888",   # 91 = India country code
    linkedin="https://linkedin.com/in/srijansrivastav29",
    github="https://github.com/SrijanSrivastav29",
    summary=("B.Tech CSE student (graduating June 2027) seeking a Data Analyst or "
             "Business Analyst internship or entry-level role. Skilled in Python, SQL, "
             "Excel and data visualization, with Forage simulations from Deloitte, "
             "Tata and British Airways, plus leadership as IEEE Student Branch Chairperson."),
)

# key, display name, initials, colours (for placeholder icon)
# clicking these companies opens their websites
URLS = {"sricore": "https://sricore.com", "auralinq": "https://auralinqpr.com"}

COMPANIES = [
    ("sricore", "Sricore IT Services", "SR", ("#6366f1", "#22d3ee")),
    ("auralinq", "Auralinq PR India", "AL", ("#f43f5e", "#fb923c")),
    ("ieee", "IEEE Student Branch", "IEEE", ("#0ea5e9", "#2563eb")),
    ("cognizance", "IIT Roorkee · Cognizance", "CG", ("#a855f7", "#ec4899")),
    ("technohacks", "TechnoHacks EduTech", "TH", ("#10b981", "#84cc16")),
]

SKILLS = {
    "Analytics": ["Python", "SQL", "MySQL", "SQLite", "Excel (Pivot Tables)", "Streamlit",
                  "Data Cleaning", "Data Visualization", "Reporting", "Google Analytics"],
    "Development": ["JavaScript", "React.js", "Next.js", "Node.js", "HTML5", "CSS3",
                    "REST APIs", "MongoDB", "Git/GitHub"],
    "Other": ["Machine Learning", "Prompt Design (Vertex AI)", "Workflow Automation",
              "Figma", "Canva"],
}

PROJECTS = [
    ("Application Activity Analytics Dashboard", "Oct 2026", ["Python", "Streamlit", "SQLite"],
     "Interactive dashboard to monitor, filter and visualise application usage and user "
     "activity. Activity logs stored in SQLite surface usage patterns for decision-making."),
    ("Spam Email Detection Using ML", "Aug – Sep 2025",
     ["TF-IDF", "Naive Bayes", "Logistic Regression", "Random Forest"],
     "Android spam-detection app built on TF-IDF and Count Vectorization features, "
     "comparing three classifiers."),
    ("Billing Software", "Jun – Jul 2025", ["Python", "ReportLab"],
     "Billing app with automated PDF invoices, tax calculation and sales tracking."),
]

# company key, role, org, period, bullets
EXPERIENCE = [
    ("sricore", "CEO & Founder", "Sricore IT Services (MSME Registered)", "Jan 2026 – Present",
     ["Founded an MSME-registered IT services company delivering web and software solutions; "
      "manage operations, clients and delivery."]),
    ("ieee", "Chairperson, IEEE Student Branch", "UNS Institute of Engineering and Technology",
     "Mar 2026 – Present",
     ["Organised 10+ technical events and workshops engaging 100+ students; grew participation "
      "by 20+ members.", "Promoted from Vice Chair (Mar 2025 – Mar 2026)."]),
    ("auralinq", "Web Developer", "Auralinq PR India Private Limited", "Jan 2026 – Oct 2026",
     ["Developed 4+ production websites and web apps using JavaScript, Python and Node.js.",
      "Used Python for data processing and validation; integrated APIs for structured data."]),
    ("cognizance", "Campus Ambassador", "IIT Roorkee (Cognizance 2025)", "Dec 2024 – Mar 2025",
     ["Reached 500+ students through outreach and digital promotion; drove 10+ registrations."]),
    ("technohacks", "Web Development Intern", "TechnoHacks EduTech", "Jul 2024 – Aug 2024",
     ["Built 3 responsive pages (Landing, Registration, Login) with HTML5, CSS3 and JavaScript."]),
]

EDU = ("B.Tech, Computer Science and Engineering", "Jul 2023 – Jun 2027 (Expected)",
       "UNS Institute of Engineering and Technology, Veer Bahadur Singh Purvanchal University, Jaunpur")

CERTS = ["Deloitte Australia Data Analytics Simulation", "Tata GenAI Powered Data Analytics Simulation",
         "British Airways Data Science Simulation", "Prompt Design in Vertex AI (Google Skill Badge)",
         "TechnoHacks Web Development Internship"]

# ------------------------------------------------------------------ HELPERS
e = html.escape

def data_uri(path):
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()

IMG_EXT = (".png", ".jpg", ".jpeg", ".webp", ".svg", ".jfif")

def find(folder, stem, any_image=False):
    """Case-insensitive search. Matches photo.jpg, Photo.PNG, photo.jpg.jpg, my photo.jpeg ..."""
    if not folder.exists():
        return None
    files = [f for f in sorted(folder.iterdir()) if f.is_file() and f.suffix.lower() in IMG_EXT]
    for f in files:
        if f.name.lower().startswith(stem.lower()):
            return f
    return files[0] if (any_image and files) else None

def photo_html():
    # look in assets/ first, then next to portfolio.py; use any image if "photo" isn't found
    f = find(ASSETS, "photo") or find(BASE, "photo") or find(ASSETS, "", any_image=True)
    if f:
        print("Using photo:", f)
        return f'<img src="{data_uri(f)}" alt="{e(P["name"])}">'
    print("PHOTO NOT FOUND. Looked in:", ASSETS, "and", BASE)
    print("Copy your photo into the assets folder and run again.")
    return '<div class="ph">SS</div>'

def icon_html(key, size=48):
    f = find(ASSETS / "logos", key)
    if f:
        return f'<span class="ico" style="width:{size}px;height:{size}px"><img src="{data_uri(f)}" alt=""></span>'
    _, _, ini, (c1, c2) = next(c for c in COMPANIES if c[0] == key)
    fs = size * (0.26 if len(ini) > 2 else 0.36)
    return (f'<span class="ico" style="width:{size}px;height:{size}px;'
            f'background:linear-gradient(135deg,{c1},{c2});font-size:{fs:.0f}px">{ini}</span>')

def chips(items):
    return "".join(f'<span class="chip">{e(i)}</span>' for i in items)

# ------------------------------------------------------------------ SECTIONS

def build():
    def brand(k, n):
        inner = f'{icon_html(k, 44)}<span>{e(n)}</span>'
        if k in URLS:
            return (f'<a class="brand link" href="{URLS[k]}" target="_blank" rel="noopener" '
                    f'title="Visit {URLS[k].split("//")[1]}">{inner}<i>&#8599;</i></a>')
        return f'<div class="brand">{inner}</div>'
    logos = "".join(brand(k, n) for k, n, *_ in COMPANIES)
    skills = "".join(f'<div class="card"><h3>{e(g)}</h3>{chips(s)}</div>' for g, s in SKILLS.items())
    projects = "".join(
        f'<div class="card proj"><div class="meta">{e(d)}</div><h3>{e(n)}</h3>'
        f'<p>{e(t)}</p><div>{chips(s)}</div></div>' for n, d, s, t in PROJECTS)
    def link(k, inner):
        return f'<a href="{URLS[k]}" target="_blank" rel="noopener">{inner}</a>' if k in URLS else inner
    def site(k):
        if k not in URLS:
            return ""
        return f' · <a class="site" href="{URLS[k]}" target="_blank" rel="noopener">{URLS[k].split("//")[1]} &#8599;</a>'
    exp = "".join(
        f'<div class="tl"><div class="dot"></div><div class="card">'
        f'<div class="row">{link(k, icon_html(k, 52))}<div><h3>{e(r)}</h3>'
        f'<div class="org">{e(o)}{site(k)}</div><div class="meta">{e(p)}</div></div></div>'
        f'<ul>{"".join(f"<li>{e(b)}</li>" for b in bl)}</ul></div></div>'
        for k, r, o, p, bl in EXPERIENCE)
    certs = "".join(f"<li>{e(c)}</li>" for c in CERTS)

    page = TEMPLATE
    for k, v in {
        "NAME": e(P["name"]), "ROLE": e(P["role"]), "WORDS": html.escape(json.dumps(P["roles"]), quote=True), "TAG": e(P["tagline"]),
        "LOC": e(P["location"]), "SUMMARY": e(P["summary"]), "EMAIL": e(P["email"]), "PHONE": e(P["phone"]), "WA": e(P["whatsapp"]),
        "LINKEDIN": e(P["linkedin"]), "GITHUB": e(P["github"]), "PHOTO": photo_html(),
        "LOGOS": logos, "SKILLS": skills, "PROJECTS": projects,
        "EXP": exp, "CERTS": certs, "EDU_T": e(EDU[0]), "EDU_P": e(EDU[1]), "EDU_S": e(EDU[2]),
        "YEAR": "2026",
    }.items():
        page = page.replace("{{" + k + "}}", v)
    return page

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{NAME}} | Portfolio</title>
<style>
:root{--bg:#0b1020;--card:#131a33;--line:#222c52;--tx:#e8ecff;--mu:#97a0c8;--a:#6366f1;--b:#22d3ee}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{font-family:Inter,Segoe UI,system-ui,sans-serif;background:var(--bg);color:var(--tx);line-height:1.6}
body:before{content:"";position:fixed;inset:0;z-index:-1;background:
radial-gradient(600px 400px at 85% -5%,rgba(99,102,241,.35),transparent),
radial-gradient(500px 400px at 0% 40%,rgba(34,211,238,.15),transparent)}
a{color:inherit;text-decoration:none}.wrap{max-width:1080px;margin:auto;padding:0 24px}
nav{position:sticky;top:0;z-index:9;backdrop-filter:blur(14px);background:rgba(11,16,32,.7);border-bottom:1px solid var(--line)}
nav .wrap{display:flex;justify-content:space-between;align-items:center;height:62px}
nav b{font-size:1.1rem}nav div a{margin-left:22px;color:var(--mu);font-size:.92rem}nav div a:hover{color:#fff}
.hero{display:grid;grid-template-columns:1.3fr 1fr;gap:48px;align-items:center;padding:80px 0 50px}
.pill{display:inline-block;padding:5px 14px;border:1px solid var(--line);border-radius:99px;color:var(--b);font-size:.82rem;background:rgba(34,211,238,.08)}
h1{font-size:3.3rem;line-height:1.1;margin:18px 0 8px}
.grad{background:linear-gradient(90deg,var(--a),var(--b));-webkit-background-clip:text;background-clip:text;color:transparent}
.tag{color:var(--mu);font-size:1.1rem;margin-bottom:16px}.hero p.s{color:var(--mu);max-width:540px}
.btns{margin-top:28px;display:flex;gap:12px;flex-wrap:wrap}
.btn{padding:12px 24px;border-radius:12px;font-weight:600;border:1px solid var(--line);transition:.25s}
.btn.p{background:linear-gradient(90deg,var(--a),var(--b));border:0;color:#fff}.btn:hover{transform:translateY(-3px);box-shadow:0 10px 30px rgba(99,102,241,.35)}
.photo{position:relative;width:min(340px,80%);aspect-ratio:1;margin:auto}
.photo:before{content:"";position:absolute;inset:-10px;border-radius:50%;background:conic-gradient(var(--a),var(--b),#ec4899,var(--a));animation:spin 8s linear infinite;filter:blur(2px)}
.photo>img,.photo .ph{position:absolute;inset:0;width:100%;height:100%;border-radius:50%;object-fit:cover;border:6px solid var(--bg)}
.ph{display:flex;align-items:center;justify-content:center;font-size:6rem;font-weight:800;background:linear-gradient(135deg,#1b2350,#2a3470)}
@keyframes spin{to{transform:rotate(360deg)}}
.brands{display:flex;flex-wrap:wrap;gap:14px;justify-content:center;padding:26px 0;border-block:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:10px;padding:8px 16px 8px 8px;border-radius:14px;background:var(--card);border:1px solid var(--line);font-size:.88rem;color:var(--mu)}
.ico{display:inline-flex;align-items:center;justify-content:center;border-radius:12px;font-weight:800;color:#fff;overflow:hidden;flex:none;background:#fff}
.ico img{width:100%;height:100%;object-fit:contain;padding:4px}
section{padding:60px 0}h2{font-size:2rem;margin-bottom:28px}h2:after{content:"";display:block;width:56px;height:4px;border-radius:4px;margin-top:8px;background:linear-gradient(90deg,var(--a),var(--b))}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:20px}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:24px;transition:.3s}
.card:hover{transform:translateY(-5px);border-color:var(--a);box-shadow:0 14px 40px rgba(0,0,0,.35)}
.card h3{margin-bottom:10px}.chip{display:inline-block;margin:4px 6px 4px 0;padding:4px 12px;border-radius:99px;font-size:.8rem;background:rgba(99,102,241,.14);color:#aab1ff;border:1px solid rgba(99,102,241,.3)}
.meta{color:var(--b);font-size:.82rem;font-weight:600}.proj p{color:var(--mu);margin:8px 0 12px;font-size:.93rem}
.timeline{position:relative;padding-left:34px}.timeline:before{content:"";position:absolute;left:9px;top:6px;bottom:6px;width:2px;background:var(--line)}
.tl{position:relative;margin-bottom:22px}.dot{position:absolute;left:-33px;top:28px;width:14px;height:14px;border-radius:50%;background:var(--b);box-shadow:0 0 0 5px rgba(34,211,238,.18)}
.row{display:flex;gap:16px;align-items:center;margin-bottom:10px}.org{color:var(--mu);font-size:.92rem}
.tl ul{padding-left:20px;color:var(--mu);font-size:.93rem}.tl li{margin:4px 0}
.edu ul{padding-left:20px;color:var(--mu);margin-top:8px}
.contact{text-align:center}.contact p{color:var(--mu);margin-bottom:24px}.contact h2:after{margin-inline:auto}
footer{text-align:center;padding:30px;color:var(--mu);border-top:1px solid var(--line);font-size:.85rem}
.fade{opacity:0;transform:translateY(24px);transition:.8s}.fade.in{opacity:1;transform:none}
@media(max-width:800px){.hero{grid-template-columns:1fr;text-align:center;padding-top:40px}.hero p.s{margin:auto}.btns{justify-content:center}
h1{font-size:2.5rem}.stats{grid-template-columns:repeat(2,1fr)}nav div a:nth-child(n+4){display:none}.photo{order:-1;width:240px}}

/* ---------- contact buttons & links ---------- */
.brand.link{cursor:pointer;position:relative}.brand.link i{font-style:normal;color:var(--b);margin-left:2px}
.brand.link:hover{transform:translateY(-6px) scale(1.04);box-shadow:0 10px 30px rgba(34,211,238,.25)}
.site{color:var(--b);font-weight:600}.site:hover{text-decoration:underline}
/* ---------- animations & motion ---------- */
#bar{position:fixed;top:0;left:0;height:3px;width:0;z-index:99;background:linear-gradient(90deg,var(--a),var(--b),#ec4899)}
.blob{position:fixed;z-index:-1;border-radius:50%;filter:blur(90px);opacity:.35;pointer-events:none}
.b1{width:380px;height:380px;background:#6366f1;top:8%;left:-6%;animation:drift 18s ease-in-out infinite alternate}
.b2{width:320px;height:320px;background:#22d3ee;bottom:5%;right:-5%;animation:drift 22s ease-in-out infinite alternate-reverse}
@keyframes drift{0%{transform:translate(0,0) scale(1)}50%{transform:translate(90px,-60px) scale(1.2)}100%{transform:translate(-40px,80px) scale(.9)}}
#glow{position:fixed;width:420px;height:420px;border-radius:50%;pointer-events:none;z-index:-1;left:0;top:0;
background:radial-gradient(circle,rgba(99,102,241,.18),transparent 65%);transform:translate(-50%,-50%);transition:opacity .3s}
@keyframes up{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:none}}
.hero>div:first-child>*{opacity:0;animation:up .8s cubic-bezier(.2,.7,.2,1) forwards}
.hero>div:first-child>*:nth-child(1){animation-delay:.1s}.hero>div:first-child>*:nth-child(2){animation-delay:.25s}
.hero>div:first-child>*:nth-child(3){animation-delay:.4s}.hero>div:first-child>*:nth-child(4){animation-delay:.55s}
.hero>div:first-child>*:nth-child(5){animation-delay:.7s}
.photo{animation:float 5s ease-in-out infinite,pop 1s cubic-bezier(.2,.9,.3,1.3) both}
@keyframes float{50%{transform:translateY(-16px)}}@keyframes pop{from{opacity:0;transform:scale(.6) rotate(-8deg)}}
.photo:after{content:"";position:absolute;inset:-26px;border-radius:50%;border:2px dashed rgba(34,211,238,.4);animation:spin 24s linear infinite reverse}
.pill{animation:pulse 2.4s ease-in-out infinite}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(34,211,238,.45)}50%{box-shadow:0 0 0 10px rgba(34,211,238,0)}}
.caret{display:inline-block;width:2px;height:1.1em;margin-left:3px;vertical-align:text-bottom;background:var(--b);animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.grad{background-size:200% auto;animation:shine 5s linear infinite}@keyframes shine{to{background-position:200% center}}
.brand{animation:bob 4s ease-in-out infinite}.brand:nth-child(2n){animation-delay:-1.3s}.brand:nth-child(3n){animation-delay:-2.6s}
@keyframes bob{50%{transform:translateY(-7px)}}.brand:hover{color:#fff;border-color:var(--b)}
.btn{position:relative;overflow:hidden}
.btn:after{content:"";position:absolute;top:0;left:-80%;width:50%;height:100%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.35),transparent);transform:skewX(-20deg)}
.btn:hover:after{left:130%;transition:.7s}
.chip{transition:.25s}.chip:hover{transform:translateY(-3px) scale(1.08);background:rgba(34,211,238,.2);color:#fff}
.card{transform-style:preserve-3d;will-change:transform}
.dot{animation:ping 2.4s ease-out infinite}@keyframes ping{70%{box-shadow:0 0 0 12px rgba(34,211,238,0)}}
.timeline:before{background:linear-gradient(var(--a),var(--b),transparent)}
.fade{transform:translateY(40px) scale(.98);transition:opacity .9s,transform .9s cubic-bezier(.2,.7,.2,1)}
.fade.in{transform:none}
.item{opacity:0;transform:translateY(30px);transition:opacity .7s,transform .7s cubic-bezier(.2,.7,.2,1)}
.item.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.fade,.item,.hero>div:first-child>*{opacity:1!important;transform:none!important}}
</style></head><body>
<div id="bar"></div><div class="blob b1"></div><div class="blob b2"></div><div id="glow"></div>
<nav><div class="wrap"><b class="grad">{{NAME}}</b><div>
<a href="#about">About</a><a href="#skills">Skills</a><a href="#projects">Projects</a><a href="#experience">Experience</a><a href="#contact">Contact</a></div></div></nav>
<div class="wrap">
<header class="hero" id="about"><div>
<span class="pill">● Open to internships &amp; entry-level roles</span>
<h1>Hi, I'm <span class="grad">{{NAME}}</span></h1>
<div class="tag"><b id="typed" data-words="{{WORDS}}">{{ROLE}}</b><span class="caret"></span> &nbsp;|&nbsp; {{TAG}}</div>
<p class="s">{{SUMMARY}}</p>
<div class="btns"><a class="btn p" href="#contact">Contact</a><a class="btn" href="{{GITHUB}}" target="_blank">GitHub</a><a class="btn" href="{{LINKEDIN}}" target="_blank">LinkedIn</a></div>
</div><div class="photo">{{PHOTO}}</div></header>
<div class="brands">{{LOGOS}}</div>
<section id="skills" class="fade"><h2>Skills</h2><div class="grid">{{SKILLS}}</div></section>
<section id="projects" class="fade"><h2>Projects</h2><div class="grid">{{PROJECTS}}</div></section>
<section id="experience" class="fade"><h2>Experience</h2><div class="timeline">{{EXP}}</div></section>
<section class="fade"><h2>Education &amp; Certifications</h2><div class="grid">
<div class="card edu"><h3>{{EDU_T}}</h3><div class="meta">{{EDU_P}}</div><p style="color:var(--mu);margin-top:8px">{{EDU_S}}</p></div>
<div class="card edu"><h3>Certifications</h3><ul>{{CERTS}}</ul></div></div></section>
<section id="contact" class="contact fade"><h2>Let's work together</h2>
<p>{{LOC}} · Find me on LinkedIn or GitHub</p>
<div class="btns" style="justify-content:center"><a class="btn" href="{{LINKEDIN}}" target="_blank">LinkedIn</a><a class="btn" href="{{GITHUB}}" target="_blank">GitHub</a></div></section>
</div><footer>© {{YEAR}} {{NAME}} ·</footer>
<script>
const $=(q,c=document)=>[...c.querySelectorAll(q)];
/* scroll reveal with stagger */
const io=new IntersectionObserver(es=>es.forEach(x=>{if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}}),{threshold:.12});
$('.fade').forEach(el=>io.observe(el));
$('.grid,.timeline').forEach(g=>$('.card,.tl',g).forEach((c,i)=>{c.classList.add('item');c.style.transitionDelay=(i*120)+'ms';io.observe(c)}));
/* scroll progress bar */
const bar=document.getElementById('bar');
addEventListener('scroll',()=>{const h=document.documentElement;bar.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+'%'});
/* typing effect */
const t=document.getElementById('typed'),words=JSON.parse(t.dataset.words);let w=0,c=0,del=false;
(function type(){const word=words[w];t.textContent=word.slice(0,c);
 if(!del&&c===word.length){del=true;return setTimeout(type,1600)}
 if(del&&c===0){del=false;w=(w+1)%words.length}
 c+=del?-1:1;setTimeout(type,del?45:90)})();
/* cursor glow */
const glow=document.getElementById('glow');
addEventListener('mousemove',e=>{glow.style.left=e.clientX+'px';glow.style.top=e.clientY+'px'});
/* 3D tilt on cards */
$('.card').forEach(c=>{
 c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
  c.style.transform=`perspective(800px) rotateY(${x*8}deg) rotateX(${-y*8}deg) translateY(-5px)`;c.style.transitionDelay='0ms'});
 c.addEventListener('mouseleave',()=>{c.style.transform=''})});
/* photo parallax */
const ph=document.querySelector('.photo');
addEventListener('mousemove',e=>{if(!ph)return;const x=(e.clientX/innerWidth-.5)*14,y=(e.clientY/innerHeight-.5)*14;ph.style.translate=`${x}px ${y}px`});
</script></body></html>"""

if __name__ == "__main__":
    # create the assets folders automatically if they don't exist
    (ASSETS / "logos").mkdir(parents=True, exist_ok=True)
    out = BASE / "index.html"
    out.write_text(build(), encoding="utf-8")
    print(f"Portfolio created: {out}")
    try:
        import webbrowser
        webbrowser.open(out.as_uri())
    except Exception:
        pass