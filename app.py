"""
Asmaa Adel Ali — Portfolio (Streamlit)

How to run:
    pip install streamlit
    streamlit run app.py

Folder layout (same on your PC and on GitHub):
    app.py
    requirements.txt
    images/
        snake.png
        scraping.jpeg
        paddle.png
"""

from pathlib import Path

import urllib.parse
import streamlit as st

# =====================================================================
# 1) EDIT HERE ONLY
# =====================================================================
GITHUB_USERNAME = "asmaaaali2910-dot"

# ---------------------------------------------------------------------
# PROJECTS: each project = name + GitHub link + screenshot + description.
# Images live in the images/ folder next to app.py.
# ---------------------------------------------------------------------
PROJECTS = [
    {
        "name": "Snake Game",
        "url": "https://github.com/asmaaaali2910-dot/snake-game",
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
        "url": "https://github.com/asmaaaali2910-dot/hatla2ee-car-market",
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
        "url": "https://github.com/asmaaaali2910-dot/paddle-game",
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
    #     "url": "https://github.com/asmaaaali2910-dot/...",
    #     "image": "images/my-project.png",
    #     "description": "...",
    #     "tools": ["Python"],
    # },
]

BASE = Path(__file__).parent
# Optional: put a photo at images/profile.jpeg to show it. If it's missing, the page simply shows no photo.
PROFILE_PHOTO = BASE / "images" / "profile.jpeg"

PROFILE = {
    "name": "Asmaa Adel Ali",
    "title": "Python & Data Developer",
    "location": "El-Mandra, Alexandria, Egypt",
    "email": "Asmaa.a.ali2910@gmail.com",
    "phone": "01274046640",
    "linkedin": "https://www.linkedin.com/in/asma-aly",
    "about": (
        "Python & Data Developer with a solid foundation in Python, SQL, Machine "
        "Learning, and ETL Pipelines, backed by hands-on projects in web scraping, "
        "data cleaning, and game development. Seeking an entry-level opportunity "
        "to build efficient data and AI solutions that drive business value."
    ),
}

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

# =====================================================================
# 2) PAGE STYLE
# =====================================================================
st.set_page_config(page_title=f"{PROFILE['name']} | Portfolio", page_icon="✨", layout="wide")

st.markdown(
    """
    <style>
      .block-container {padding-top: 2rem; max-width: 1150px;}
      .hero-name {font-size: 2.6rem; font-weight: 800; margin-bottom: 0;}
      .hero-title {font-size: 1.2rem; color: #7c5cff; font-weight: 600; margin-top: 0;}
      .chip {display:inline-block; padding:4px 12px; margin:3px; border-radius:999px;
             background:rgba(124,92,255,.12); color:#7c5cff; font-size:.85rem; font-weight:500;}
      .card {border:1px solid rgba(128,128,128,.25); border-radius:14px; padding:18px;
             margin-bottom:16px; background:rgba(128,128,128,.04);}
      .muted {color: gray; font-size: .9rem;}
      .section {font-size:1.6rem; font-weight:700; margin-top:1.5rem;
                border-left:5px solid #7c5cff; padding-left:10px;}
      img {border-radius: 10px;}
      html {scroll-behavior: smooth;}
      .anchor {position: relative; top: -70px; visibility: hidden;}
      .nav-btn {display:block; text-decoration:none !important; text-align:left;
                padding:10px 14px; margin:6px 0; border-radius:10px; font-weight:600;
                color:#7c5cff !important; background:rgba(124,92,255,.10);
                border:1px solid rgba(124,92,255,.25); transition:all .15s;}
      .nav-btn:hover {background:#7c5cff; color:white !important;}
    </style>
    """,
    unsafe_allow_html=True,
)


def chips(items):
    st.markdown("".join(f'<span class="chip">{i}</span>' for i in items), unsafe_allow_html=True)


def section(title, anchor=None):
    if anchor:
        st.markdown(f'<div id="{anchor}" class="anchor"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section">{title}</div>', unsafe_allow_html=True)
    st.write("")


NAV = [
    ("home", "🏠 Home"),
    ("projects", "💻 Projects"),
    ("skills", "🛠️ Skills"),
    ("education", "🎓 Education & Certificates"),
    ("contact", "📬 Contact"),
]


# =====================================================================
# 4) SIDEBAR
# =====================================================================
with st.sidebar:
    if PROFILE_PHOTO.exists():
        st.image(str(PROFILE_PHOTO), use_container_width=True)
    st.markdown(f"### {PROFILE['name']}")
    st.caption(PROFILE["title"])
    st.markdown(f"📍 {PROFILE['location']}")
    st.markdown(f"✉️ [{PROFILE['email']}](mailto:{PROFILE['email']})")
    st.markdown(f"📞 {PROFILE['phone']}")
    st.markdown(f"🔗 [LinkedIn]({PROFILE['linkedin']})")
    if GITHUB_USERNAME != "YOUR_GITHUB_USERNAME":
        st.markdown(f"💻 [GitHub](https://github.com/{GITHUB_USERNAME})")
    st.divider()
    st.markdown(
        "".join(f'<a class="nav-btn" href="#{a}" target="_self">{label}</a>' for a, label in NAV),
        unsafe_allow_html=True,
    )

# =====================================================================
# 5) ONE PAGE — all sections, top to bottom
# =====================================================================
# ---------- Home ----------
with st.container():
    st.markdown('<div id="home" class="anchor"></div>', unsafe_allow_html=True)
    if PROFILE_PHOTO.exists():
        c1, c2 = st.columns([1, 2.2], gap="large")
        c1.image(str(PROFILE_PHOTO), use_container_width=True)
    else:
        c2 = st.container()
    with c2:
        st.markdown(f'<p class="hero-name">Hi, I\'m {PROFILE["name"]} 👋</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-title">{PROFILE["title"]}</p>', unsafe_allow_html=True)
        st.write(PROFILE["about"])
        chips(["Python", "SQL", "Machine Learning", "ETL Pipelines"])
        st.write("")
        b1, b2, b3 = st.columns(3)
        b1.link_button("LinkedIn", PROFILE["linkedin"], use_container_width=True)
        if GITHUB_USERNAME != "YOUR_GITHUB_USERNAME":
            b2.link_button("GitHub", f"https://github.com/{GITHUB_USERNAME}", use_container_width=True)
        b3.link_button("Email me", f"mailto:{PROFILE['email']}", use_container_width=True)


st.divider()

# ---------- Projects ----------
with st.container():
    section("💻 Projects", "projects")
    for p in PROJECTS:
        box = st.container(border=True)
        img_col, info_col = box.columns([1.2, 1], gap="large")
        with img_col:
            img = p["image"] if str(p["image"]).startswith("http") else BASE / p["image"]
            if str(img).startswith("http") or Path(img).exists():
                st.image(str(img), use_container_width=True)
            else:
                st.info(f"Image not found:\n{p['image']}")
        with info_col:
            st.markdown(f"### [{p['name']}]({p['url']})")
            st.write(p["description"])
            chips(p["tools"])
            st.write("")
            st.link_button("View on GitHub", p["url"], use_container_width=True)
        st.write("")

st.divider()

# ---------- Skills ----------
with st.container():
    section("🛠️ Skills", "skills")
    for group, items in SKILLS.items():
        st.markdown(f"**{group}**")
        chips(items)
        st.write("")

st.divider()

# ---------- Education & Certificates ----------
with st.container():
    section("🎓 Education", "education")
    for e in EDUCATION:
        st.markdown(
            f'<div class="card"><b>{e["degree"]}</b><br>{e["place"]}<br>'
            f'<span class="muted">{e["years"]}</span></div>',
            unsafe_allow_html=True,
        )

    section("📜 Courses & Certificates")
    for c in CERTIFICATES:
        with st.expander(f"{c['name']} — {c['org']} ({c['date']})", expanded=True):
            img = BASE / c["image"] if c.get("image") else None
            if img and img.exists():
                txt_col, img_col = st.columns([1.3, 1], gap="large")
                with txt_col:
                    for p in c["points"]:
                        st.markdown(f"- {p}")
                img_col.image(str(img), caption=c["name"], use_container_width=True)
            else:
                for p in c["points"]:
                    st.markdown(f"- {p}")

st.divider()

# ---------- Contact ----------
with st.container():
    section("📬 Get in touch", "contact")
    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown(f"**Email:** [{PROFILE['email']}](mailto:{PROFILE['email']})")
        st.markdown(f"**Phone:** {PROFILE['phone']}")
        st.markdown(f"**LinkedIn:** [{PROFILE['linkedin']}]({PROFILE['linkedin']})")
        st.markdown(f"**Location:** {PROFILE['location']}")
    with c2:
        with st.form("contact"):
            name = st.text_input("Your name")
            email = st.text_input("Your email")
            msg = st.text_area("Message")
            if st.form_submit_button("Send"):
                if name and email and msg:
                    subject = urllib.parse.quote(f"Portfolio message from {name}")
                    body = urllib.parse.quote(f"{msg}\n\nFrom: {name} <{email}>")
                    st.success("Thanks! Click below to send it from your email app.")
                    st.link_button("Open email", f"mailto:{PROFILE['email']}?subject={subject}&body={body}")
                else:
                    st.warning("Please fill in all fields.")

st.divider()
st.caption(f"© 2026 {PROFILE['name']} · Built with Streamlit")
