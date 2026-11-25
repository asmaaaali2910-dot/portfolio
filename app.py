"""
Asmaa Adel Ali — Portfolio (Streamlit)

How to run:
    pip install streamlit
    streamlit run app.py

Folder layout (same on your PC and on GitHub):
    app.py
    requirements.txt
    images/
        profile.jpeg
        snake.png
        scraping.jpeg
        paddle.png
        oracle_certificate.jpg
"""

import base64
import html
import mimetypes
from pathlib import Path

import streamlit as st

BASE = Path(__file__).parent

# =====================================================================
# 1) YOUR DATA — edit here only
# =====================================================================
GITHUB_USERNAME = "asmaaaali2910-dot"
GITHUB_URL = f"https://github.com/{GITHUB_USERNAME}"
REPO_IMAGES = f"{GITHUB_URL}/portfolio/blob/main/images"

PROFILE = {
    "name": "Asmaa Adel Ali",
    "title": "Python & Data Developer",
    "location": "El-Mandra, Alexandria, Egypt",
    "email": "Asmaa.a.ali2910@gmail.com",
    "phone": "01274046640",
    "linkedin": "https://www.linkedin.com/in/asma-aly",
    "photo": "images/profile.jpeg",
    "about": (
        "Python & Data Developer with a solid foundation in Python, SQL, Machine "
        "Learning, and ETL Pipelines, backed by hands-on projects in web scraping, "
        "data cleaning, and game development. Seeking an entry-level opportunity "
        "to build efficient data and AI solutions that drive business value."
    ),
}

PROJECTS = [
    {
        "name": "Snake Game",
        "url": f"{GITHUB_URL}/snake-game",
        "image": "images/snake.png",
        "description": (
            "Classic 2D Snake arcade game built with Python using Object-Oriented "
            "Programming: custom collision detection, real-time score tracking, "
            "and smooth keyboard controls."
        ),
        "tools": ["Python", "Turtle", "OOP", "VS Code"],
    },
    {
        "name": "Hatla2ee Car Market — Scraping & Data Structuring",
        "url": f"{GITHUB_URL}/hatla2ee-car-market",
        "image": "images/scraping.jpeg",
        "description": (
            "End-to-end Python pipeline that scrapes about 4,300 used-car listings "
            "from Hatla2ee Egypt, then cleans and structures the raw data into a "
            "consistent table and analyzes the used-car market. The clean "
            "dataset is exported to Excel, CSV, JSON, and a SQLite database, ready "
            "for reporting or further analysis."
        ),
        "tools": ["Python", "Web Scraping", "Pandas", "Data Cleaning", "SQLite", "Excel / CSV / JSON"],
    },
    {
        "name": "Paddle Game",
        "url": f"{GITHUB_URL}/paddle-game",
        "image": "images/paddle.png",
        "description": (
            "Classic 2D Paddle (Pong-style) arcade game built with Python using "
            "Object-Oriented Programming: ball physics with custom collision "
            "detection against paddles and walls, real-time score tracking, and "
            "responsive keyboard controls."
        ),
        "tools": ["Python", "Turtle", "OOP", "VS Code"],
    },
    # Next project goes here, same shape:
    # {
    #     "name": "...",
    #     "url": f"{GITHUB_URL}/...",
    #     "image": "images/my-project.png",
    #     "description": "...",
    #     "tools": ["Python"],
    # },
]

EDUCATION = [
    {
        "degree": "B.Sc. in Accounting",
        "place": "Faculty of Commerce, Damanhur University",
        "years": "2022 – 2026",
    }
]

CERTIFICATES = [
    {
        "name": "AI Engineering Training Program",
        "org": "Digital Egypt Pioneers Initiative (DEPI) – MCIT",
        "date": "July 2026",
        "points": [
            "Intensive AI Engineering track focusing on Python, Machine Learning, and SQL.",
            "Applied practical techniques for data preparation, ETL pipelines, and data analysis.",
            "Developed soft skills: career planning, personal branding, client communication.",
        ],
    },
    {
        "name": "AI for You: Training and Assessment",
        "org": "Oracle University",
        "date": "Aug 2026",
        "image": "images/oracle_certificate.jpg",
        "points": [
            "Learning path covering foundational AI concepts and technologies.",
            "Insights into machine learning principles, AI applications, and cloud-based AI.",
        ],
    },
]

SKILLS = {
    "Programming & Core Tech": ["Python", "SQL", "Machine Learning", "ETL Pipelines", "Pandas"],
    "Tools": ["VS Code", "Supermaven", "Google Colab", "Git & GitHub", "Excel", "Word"],
    "Business & Domain": ["Accounting Fundamentals", "Financial Reporting", "Business Administration"],
    "Soft Skills": ["Problem Solving", "Teamwork", "Time Management", "Presentation"],
    "Languages": ["Arabic — Native", "English — Good"],
}

NAV = [
    ("about", "About"),
    ("projects", "Projects"),
    ("skills", "Skills"),
    ("education", "Education"),
    ("contact", "Contact"),
]


# =====================================================================
# 2) HELPERS
# =====================================================================
@st.cache_data
def img_src(rel_path: str) -> str:
    """Embed a local image as a data URI so it can live inside custom HTML."""
    path = BASE / rel_path
    if not path.exists():
        return ""
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    data = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{data}"


def esc(text: str) -> str:
    return html.escape(str(text))


def show(markup: str) -> None:
    # Collapse to one line so Markdown never treats indented HTML as a code block.
    st.markdown(" ".join(line.strip() for line in markup.splitlines()), unsafe_allow_html=True)


def tags(items) -> str:
    return "".join(f'<span class="tag">{esc(i)}</span>' for i in items)


# =====================================================================
# 3) STYLE
# =====================================================================
photo = img_src(PROFILE["photo"])
st.set_page_config(
    page_title=f"{PROFILE['name']} | Portfolio",
    page_icon=str(BASE / PROFILE["photo"]) if photo else None,
    layout="wide",
    initial_sidebar_state="collapsed",
)

show(
    """
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{
  --ink:#1C2541;      
  --ink-2:#2A3558;
  --rose:#C9415E;     
  --rose-soft:#F6DDE3;
  --paper:#FFFFFF;
  --cream:#F7F3EF;    
  --muted:#5C6378;
  --line:#E4DDD6;
}
html{scroll-behavior:smooth;}
.stApp{background:var(--cream);}
header[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],
[data-testid="stSidebar"],[data-testid="collapsedControl"],#MainMenu,footer{display:none !important;}
.block-container,[data-testid="stMainBlockContainer"]{max-width:1100px;padding-top:0 !important;padding-bottom:0 !important;}
.stApp, .stApp p, .stApp li, .stApp span, .stApp a, .stApp div{font-family:'DM Sans',sans-serif;}
.stMarkdown p{margin:0;}
.hero h1,.sec h2,.proj h3,.contact h2,.topbar .brand{font-family:'Fraunces',Georgia,serif !important;}
.hero h1,.sec h2,.proj h3,.cert h3,.contact h2{padding:0 !important;}


.topbar{position:fixed;top:0;left:0;right:0;z-index:999;background:var(--ink);}
.topbar .in{max-width:1100px;margin:auto;padding:0 24px;height:60px;display:flex;
  align-items:center;justify-content:space-between;}
.topbar .brand{font-family:'Fraunces',serif;font-size:20px;color:#fff;font-weight:700;letter-spacing:.01em;}
.topbar .brand b{color:var(--rose);}
.topbar nav{display:flex;gap:26px;}
.topbar nav a{color:#D5D9E5 !important;text-decoration:none;font-size:15px;font-weight:500;}
.topbar nav a:hover{color:#fff !important;}
.anchor{display:block;position:relative;top:-80px;visibility:hidden;}


.hero{margin-top:84px;background:var(--ink);border-radius:22px;overflow:hidden;
  display:grid;grid-template-columns:1.25fr 1fr;align-items:stretch;min-height:480px;}
.hero .txt{padding:56px 48px;display:flex;flex-direction:column;justify-content:center;}
.hero .kicker{color:var(--rose);font-weight:700;font-size:14px;letter-spacing:.14em;text-transform:uppercase;}
.hero h1{font-family:'Fraunces',serif;color:#fff;font-size:clamp(40px,6vw,66px);
  line-height:1.05;margin:14px 0 6px;font-weight:700;}
.hero .role{color:#AEB6CC;font-size:20px;font-weight:500;}
.hero .about{color:#D5D9E5;margin-top:20px;line-height:1.75;font-size:16.5px;max-width:34em;}
.btns{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px;}
.btn{padding:11px 24px;border-radius:8px;font-weight:700;font-size:15px;text-decoration:none !important;}
.btn.main{background:var(--rose);color:#fff !important;}
.btn.main:hover{background:#B3344F;}
.btn.ghost{border:1.5px solid #5A6585;color:#fff !important;}
.btn.ghost:hover{border-color:#fff;}
.hero .pic{background:radial-gradient(circle at 50% 60%, #3B4A75 0%, var(--ink) 72%);
  display:flex;align-items:flex-end;justify-content:center;}
.hero .pic img{width:100%;height:100%;max-height:520px;object-fit:cover;object-position:center top;}


.sec{padding:72px 0 8px;}
.sec h2{font-family:'Fraunces',serif;color:var(--ink);font-size:38px;font-weight:700;margin:0;}
.sec .lead{color:var(--muted);margin:8px 0 30px;font-size:16.5px;}
.bar{width:56px;height:4px;background:var(--rose);border-radius:4px;margin-top:12px;}

.tag{display:inline-block;padding:4px 12px;margin:4px 6px 0 0;border-radius:999px;
  background:var(--rose-soft);color:#8E2A41;font-size:13.5px;font-weight:500;}


.proj{background:var(--paper);border:1px solid var(--line);border-radius:16px;overflow:hidden;
  display:grid;grid-template-columns:1.1fr 1fr;margin-bottom:26px;}
.proj:nth-child(even){grid-template-columns:1fr 1.1fr;}
.proj:nth-child(even) .shot{order:2;}
.proj .shot{background:#EDE7E1;display:flex;align-items:center;justify-content:center;min-height:260px;}
.proj .shot img{width:100%;height:100%;object-fit:cover;}
.proj .body{padding:30px 32px;display:flex;flex-direction:column;gap:10px;}
.proj .num{color:var(--rose);font-weight:700;font-size:13px;letter-spacing:.14em;}
.proj h3{font-family:'Fraunces',serif;color:var(--ink);font-size:24px;line-height:1.25;margin:0;}
.proj p{color:var(--muted);line-height:1.7;font-size:15.5px;}
.link{margin-top:auto;padding-top:8px;color:var(--rose) !important;font-weight:700;text-decoration:none !important;}
.link:hover{text-decoration:underline !important;}


.skills{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px;}
.skill{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:22px 24px;}
.skill h4{color:var(--ink);font-size:16px;margin:0 0 8px;font-weight:700;}


.edu{background:var(--paper);border-left:5px solid var(--rose);border-radius:12px;padding:22px 26px;margin-bottom:28px;}
.edu b{color:var(--ink);font-size:18px;}
.edu div{color:var(--muted);}
.certs{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:20px;}
.cert{background:var(--paper);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column;}
.cert img{width:100%;aspect-ratio:4/3;object-fit:cover;object-position:top;border-bottom:1px solid var(--line);}
.cert .body{padding:20px 24px;display:flex;flex-direction:column;gap:6px;flex:1;}
.cert h3{color:var(--ink);font-size:18px;margin:0;font-weight:700;}
.cert small{color:var(--muted);font-size:14px;}
.cert ul{margin:6px 0 0 18px;padding:0;color:var(--muted);font-size:15px;line-height:1.65;}


.contact{margin:72px 0 40px;background:var(--ink);border-radius:22px;padding:52px 48px;
  display:grid;grid-template-columns:1.1fr 1fr;gap:30px;align-items:center;}
.contact h2{font-family:'Fraunces',serif;color:#fff;font-size:36px;margin:0;}
.contact p{color:#AEB6CC;margin-top:10px;line-height:1.7;}
.contact dl{margin:0;}
.contact dt{color:#8C95AE;font-size:13px;letter-spacing:.1em;text-transform:uppercase;margin-top:14px;}
.contact dd{margin:2px 0 0;color:#fff;font-weight:500;font-size:16px;}
.contact dd a{color:#fff !important;text-decoration:none;border-bottom:1px solid var(--rose);}

@media (max-width:820px){
  .topbar nav{gap:14px;}
  .topbar nav a{font-size:13px;}
  .topbar .brand{display:none;}
  .topbar .in{justify-content:center;}
  .hero,.proj,.proj:nth-child(even),.contact{grid-template-columns:1fr;}
  .proj:nth-child(even) .shot{order:0;}
  .hero .pic{order:-1;max-height:380px;}
  .hero .txt,.contact{padding:34px 26px;}
}
</style>
"""
)

# =====================================================================
# 4) PAGE
# =====================================================================
first, last = PROFILE["name"].split(" ", 1)

# ---------- top bar ----------
show(
    f"""
<div class="topbar"><div class="in">
  <span class="brand">{esc(first)} <b>{esc(last)}</b></span>
  <nav>{"".join(f'<a href="#{a}" target="_self">{label}</a>' for a, label in NAV)}</nav>
</div></div>
"""
)

# ---------- hero ----------
pic_html = f'<div class="pic"><img src="{photo}" alt="{esc(PROFILE["name"])}"></div>' if photo else ""
show(
    f"""
<div><span class="anchor" id="about"></span>
<div class="hero" style="{'' if photo else 'grid-template-columns:1fr;'}">
  <div class="txt">
    <span class="kicker">Portfolio</span>
    <h1>{esc(PROFILE["name"])}</h1>
    <div class="role">{esc(PROFILE["title"])}</div>
    <p class="about">{esc(PROFILE["about"])}</p>
    <div class="btns">
      <a class="btn main" href="#projects" target="_self">View my projects</a>
      <a class="btn ghost" href="{GITHUB_URL}" target="_blank">GitHub</a>
      <a class="btn ghost" href="{PROFILE["linkedin"]}" target="_blank">LinkedIn</a>
    </div>
  </div>
  {pic_html}
</div></div>
"""
)

# ---------- projects ----------
cards = []
for i, p in enumerate(PROJECTS, start=1):
    src = img_src(p["image"]) if not str(p["image"]).startswith("http") else p["image"]
    shot = f'<img src="{src}" alt="{esc(p["name"])} screenshot">' if src else ""
    cards.append(
        f"""
<div class="proj">
  <div class="shot">{shot}</div>
  <div class="body">
    <span class="num">PROJECT {i:02d}</span>
    <h3>{esc(p["name"])}</h3>
    <p>{esc(p["description"])}</p>
    <div>{tags(p["tools"])}</div>
    <a class="link" href="{p["url"]}" target="_blank">View code on GitHub &rarr;</a>
  </div>
</div>
"""
    )
show(
    f"""
<div class="sec"><span class="anchor" id="projects"></span>
  <h2>Projects</h2><div class="bar"></div>
  <p class="lead">Hands-on work in Python, from data pipelines to interactive games.</p>
  <div>{"".join(cards)}</div>
</div>
"""
)

# ---------- skills ----------
skill_cards = "".join(
    f'<div class="skill"><h4>{esc(group)}</h4>{tags(items)}</div>' for group, items in SKILLS.items()
)
show(
    f"""
<div class="sec"><span class="anchor" id="skills"></span>
  <h2>Skills</h2><div class="bar"></div>
  <p class="lead">Technical foundations backed by a business and accounting background.</p>
  <div class="skills">{skill_cards}</div>
</div>
"""
)

# ---------- education & certificates ----------
edu_html = "".join(
    f'<div class="edu"><b>{esc(e["degree"])}</b><div>{esc(e["place"])} · {esc(e["years"])}</div></div>'
    for e in EDUCATION
)
cert_cards = []
for c in CERTIFICATES:
    src = img_src(c["image"]) if c.get("image") else ""
    top = f'<img src="{src}" alt="{esc(c["name"])} certificate">' if src else ""
    view = (
        f'<a class="link" href="{REPO_IMAGES}/{Path(c["image"]).name}" target="_blank">View certificate &rarr;</a>'
        if src
        else ""
    )
    points = "".join(f"<li>{esc(pt)}</li>" for pt in c["points"])
    cert_cards.append(
        f"""
<div class="cert">{top}
  <div class="body">
    <h3>{esc(c["name"])}</h3>
    <small>{esc(c["org"])} · {esc(c["date"])}</small>
    <ul>{points}</ul>
    {view}
  </div>
</div>
"""
    )
show(
    f"""
<div class="sec"><span class="anchor" id="education"></span>
  <h2>Education &amp; Certificates</h2><div class="bar"></div>
  <p class="lead">Formal education and professional training.</p>
  {edu_html}
  <div class="certs">{"".join(cert_cards)}</div>
</div>
"""
)

# ---------- contact ----------
show(
    f"""
<div><span class="anchor" id="contact"></span>
<div class="contact">
  <div>
    <h2>Let's work together</h2>
    <p>I'm open to entry-level roles in Python and data. The fastest way to reach me is by email.</p>
    <div class="btns"><a class="btn main" href="mailto:{PROFILE["email"]}">Email me</a></div>
  </div>
  <dl>
    <dt>Email</dt><dd><a href="mailto:{PROFILE["email"]}">{esc(PROFILE["email"])}</a></dd>
    <dt>Phone</dt><dd>{esc(PROFILE["phone"])}</dd>
    <dt>LinkedIn</dt><dd><a href="{PROFILE["linkedin"]}" target="_blank">linkedin.com/in/asma-aly</a></dd>
    <dt>GitHub</dt><dd><a href="{GITHUB_URL}" target="_blank">github.com/{GITHUB_USERNAME}</a></dd>
    <dt>Location</dt><dd>{esc(PROFILE["location"])}</dd>
  </dl>
</div></div>
"""
)
