#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for Md. Shariful Islam's personal portfolio site.
Produces 8 fully-formed, dependency-free HTML files (no build step needed
at deploy time). Run: python3 build.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE_NAME = "Md. Shariful Islam"
DOMAIN = "https://sharifulcuts.com"
EMAIL = "sharifshahin.jhu@gmail.com"
UPWORK_URL = "https://www.upwork.com/freelancers/~01e389eef945cdf1aa?mp_source=share"
GOVIDCO_URL = "https://govidco.com"
TAGLINE = "Video Editor &middot; Founder, GoVidCo &middot; Creator, Shariful Reflection"

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("cuts.html", "Portfolio"),
    ("shop.html", "Shop"),
    ("reflection.html", "Reflection"),
    ("sop.html", "SOP"),
    ("contact.html", "Contact"),
]

# ---------------------------------------------------------------------------
# Shared fragments
# ---------------------------------------------------------------------------

def head(title, description, page_file, og_image="assets/img/og-image.jpg"):
    canonical = f"{DOMAIN}/{page_file}" if page_file != "index.html" else f"{DOMAIN}/"
    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{DOMAIN}/{og_image}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{SITE_NAME}">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{DOMAIN}/{og_image}">

<!-- Favicons -->
<link rel="icon" href="assets/img/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="assets/img/mark-192.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="assets/site.webmanifest">
<meta name="theme-color" content="#07090a">

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600;700&family=Hind+Siliguri:wght@400;500;600;700&display=swap" rel="stylesheet">

<!-- Icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pv3l4mCWMcE0MP9DXQZKKtSKfQ==" crossorigin="anonymous" referrerpolicy="no-referrer">

<!-- Styles -->
<link rel="stylesheet" href="assets/css/style.css">

<!-- Structured data -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Md. Shariful Islam",
  "url": "{DOMAIN}/",
  "image": "{DOMAIN}/assets/img/profile-hero.jpg",
  "jobTitle": "Video Editor & Founder",
  "email": "mailto:{EMAIL}",
  "sameAs": ["{UPWORK_URL}", "{GOVIDCO_URL}"],
  "worksFor": {{
    "@type": "Organization",
    "name": "GoVidCo",
    "url": "{GOVIDCO_URL}"
  }}
}}
</script>
</head>
"""

def nav(active_file):
    links = []
    for href, label in NAV_ITEMS:
        cls = "nav-link-active" if href == active_file else "nav-link"
        links.append(f'<a href="{href}" class="{cls}">{label}</a>')
    links_html = "\n        ".join(links)

    mobile_links = []
    for href, label in NAV_ITEMS:
        cls = "block px-4 py-3 rounded-lg text-ink-100 hover:bg-ink-800 font-medium" if href != active_file else "block px-4 py-3 rounded-lg bg-ink-800 text-brand-400 font-semibold"
        mobile_links.append(f'<a href="{href}" class="{cls}">{label}</a>')
    mobile_links_html = "\n          ".join(mobile_links)

    return f"""<header class="sticky top-0 z-50 border-b border-ink-800/80 bg-ink-950/85 backdrop-blur">
  <nav class="container-page flex items-center justify-between py-4">
    <a href="index.html" class="flex items-center gap-3 group">
      <img src="assets/img/mark-nav.png" alt="{SITE_NAME} mark" class="h-9 w-9 rounded-full ring-1 ring-ink-700 group-hover:ring-brand-400 transition">
      <span class="font-display font-bold text-lg text-white tracking-tight">{SITE_NAME}</span>
    </a>
    <div class="hidden md:flex items-center gap-8">
        {links_html}
    </div>
    <div class="hidden md:flex items-center gap-3">
      <a href="{UPWORK_URL}" target="_blank" rel="noopener noreferrer" class="btn-outline !px-4 !py-2 text-xs">
        <i class="fa-brands fa-upwork"></i> Upwork
      </a>
      <a href="contact.html" class="btn-primary !px-4 !py-2 text-xs">Start a Project</a>
    </div>
    <button id="menu-toggle" type="button" aria-label="Toggle navigation menu" aria-expanded="false" class="md:hidden inline-flex items-center justify-center h-10 w-10 rounded-lg border border-ink-700 text-ink-200 hover:text-white hover:border-brand-400 transition">
      <i class="fa-solid fa-bars" id="menu-icon-open"></i>
      <i class="fa-solid fa-xmark hidden" id="menu-icon-close"></i>
    </button>
  </nav>
  <div id="mobile-menu" class="hidden md:hidden border-t border-ink-800 bg-ink-950 px-4 pb-4 pt-2 space-y-1">
          {mobile_links_html}
    <a href="{UPWORK_URL}" target="_blank" rel="noopener noreferrer" class="block px-4 py-3 rounded-lg text-ink-100 hover:bg-ink-800 font-medium"><i class="fa-brands fa-upwork mr-2"></i>Upwork Profile</a>
  </div>
</header>
"""

def footer():
    return f"""<footer class="border-t border-ink-800 bg-ink-900/60">
  <div class="container-page section-pad !py-16">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-12">
      <div class="md:col-span-1">
        <a href="index.html" class="flex items-center gap-3 mb-4">
          <img src="assets/img/mark-nav.png" alt="{SITE_NAME} mark" class="h-10 w-10 rounded-full ring-1 ring-ink-700">
          <span class="font-display font-bold text-lg text-white">{SITE_NAME}</span>
        </a>
        <p class="text-sm text-ink-400 leading-relaxed">Video editor, founder of GoVidCo, and creator of Shariful Reflection &mdash; a multilingual motivational &amp; music channel in Bangla, Hindi, and English.</p>
      </div>
      <div>
        <h4 class="text-sm font-semibold text-white tracking-wide uppercase mb-4">Explore</h4>
        <ul class="space-y-3 text-sm text-ink-400">
          <li><a href="index.html" class="hover:text-brand-400 transition">Home</a></li>
          <li><a href="about.html" class="hover:text-brand-400 transition">About</a></li>
          <li><a href="cuts.html" class="hover:text-brand-400 transition">Portfolio</a></li>
          <li><a href="shop.html" class="hover:text-brand-400 transition">Shop &amp; Packages</a></li>
          <li><a href="reflection.html" class="hover:text-brand-400 transition">Shariful Reflection</a></li>
          <li><a href="sop.html" class="hover:text-brand-400 transition">SOP &amp; Standards</a></li>
          <li><a href="contact.html" class="hover:text-brand-400 transition">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-sm font-semibold text-white tracking-wide uppercase mb-4">Work With Me</h4>
        <ul class="space-y-3 text-sm text-ink-400">
          <li><a href="{GOVIDCO_URL}" target="_blank" rel="noopener noreferrer" class="hover:text-crimson-400 transition flex items-center gap-2"><i class="fa-solid fa-video w-4"></i>GoVidCo &mdash; Agency Site</a></li>
          <li><a href="{UPWORK_URL}" target="_blank" rel="noopener noreferrer" class="hover:text-brand-400 transition flex items-center gap-2"><i class="fa-brands fa-upwork w-4"></i>Upwork &mdash; Individual Contracts</a></li>
          <li><a href="mailto:{EMAIL}" class="hover:text-brand-400 transition flex items-center gap-2"><i class="fa-solid fa-envelope w-4"></i>{EMAIL}</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-sm font-semibold text-white tracking-wide uppercase mb-4">Shariful Reflection</h4>
        <ul class="space-y-3 text-sm text-ink-400">
          <li class="flex items-center gap-2"><i class="fa-solid fa-language w-4 text-gold-400"></i>Bangla &middot; Hindi &middot; English</li>
          <li><a href="reflection.html" class="hover:text-gold-400 transition">Visit the Reflection Hub &rarr;</a></li>
        </ul>
      </div>
    </div>
    <div class="mt-14 pt-8 border-t border-ink-800 flex flex-col sm:flex-row items-center justify-between gap-4">
      <p class="text-xs text-ink-500">&copy; <span id="year">2026</span> {SITE_NAME}. All rights reserved.</p>
      <div class="flex items-center gap-4 text-ink-500">
        <span class="text-xs">GoVidCo is the official production &amp; growth agency &middot; Upwork hosts individual client contracts</span>
      </div>
      <button id="back-to-top" type="button" aria-label="Back to top" class="h-9 w-9 rounded-full border border-ink-700 flex items-center justify-center text-ink-300 hover:text-brand-400 hover:border-brand-400 transition">
        <i class="fa-solid fa-arrow-up text-xs"></i>
      </button>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
"""

def page(title, description, page_file, main_html, body_class="", extra_head=""):
    h = head(title, description, page_file)
    if extra_head:
        h = h.replace("</head>", extra_head + "\n</head>")
    return f"""{h}<body class="{body_class}">
{nav(page_file)}
<main>
{main_html}
</main>
{footer()}
</body>
</html>
"""

# ---------------------------------------------------------------------------
# Shared data
# ---------------------------------------------------------------------------

CATEGORIES = [
    {
        "id": "brand-guardian",
        "title": "The Brand Guardian",
        "img": "thumb-brand-guardian.jpg",
        "tag": "Channel Consistency",
        "desc": "Long-form, recurring channel content edited to a strict style guide &mdash; consistent pacing, graphics, and tone across every episode so a brand's identity never wavers, no matter who's behind the camera.",
    },
    {
        "id": "authority",
        "title": "The Authority",
        "img": "thumb-authority.jpg",
        "tag": "Thought Leadership",
        "desc": "Talking-head and expert-interview edits built to establish credibility &mdash; clean cuts, subtle motion graphics, and pacing that keeps attention on the message, not the edit.",
    },
    {
        "id": "viral-engine",
        "title": "The Viral Engine",
        "img": "thumb-viral-engine.jpg",
        "tag": "Short-Form Reach",
        "desc": "Vertical, short-form content engineered for Reels, TikTok, and Shorts &mdash; fast hooks, punchy captions, and retention-first pacing designed to move through the algorithm.",
    },
    {
        "id": "converter",
        "title": "The Converter",
        "img": "thumb-converter.jpg",
        "tag": "Sales &amp; Conversion",
        "desc": "Video sales letters, product demos, and ad creative cut with a single goal &mdash; turning a viewer into a customer, backed by direct-response pacing and clear calls to action.",
    },
    {
        "id": "flagship",
        "title": "The Flagship",
        "img": "thumb-flagship.jpg",
        "tag": "Signature Long-Form",
        "desc": "Documentary-style, hero long-form videos &mdash; the flagship piece a brand or creator is proudest of, edited with cinematic color, sound design, and pacing built for a sit-down watch.",
    },
    {
        "id": "automation-engine",
        "title": "The Automation Engine",
        "img": "thumb-automation-engine.jpg",
        "tag": "Scalable Workflows",
        "desc": "Systemized, AI-assisted editing pipelines built for high-volume channels &mdash; templated projects and repeatable workflows that let a team ship daily without sacrificing quality.",
    },
]

LANGUAGES = [
    {
        "code": "bn",
        "name": "Bangla",
        "native": "বাংলা",
        "accent": "gold",
        "desc": "Reflections on discipline, purpose, and growth &mdash; rooted in the language Shariful grew up thinking in, blending motivational storytelling with original music.",
    },
    {
        "code": "hi",
        "name": "Hindi",
        "native": "हिंदी",
        "accent": "maroon",
        "desc": "Motivational narratives and reflective music for the Hindi-speaking audience, built with the same AI-assisted production quality as the Bangla and English channels.",
    },
    {
        "code": "en",
        "name": "English",
        "native": "English",
        "accent": "brand",
        "desc": "The global voice of the Reflection project &mdash; short-form and long-form pieces on mindset, stillness, and momentum, for a worldwide audience.",
    },
]

def stat_tile(value, label, caption=None, color="brand"):
    cap = f'<p class="text-xs text-ink-500 mt-1">{caption}</p>' if caption else ""
    return f"""<div class="stat-tile">
  <p class="font-display text-3xl sm:text-4xl font-bold text-{color}-400">{value}</p>
  <p class="text-sm text-ink-300 mt-2">{label}</p>
  {cap}
</div>"""

def category_card(cat, expanded=False):
    if expanded:
        return f"""<div id="{cat['id']}" class="card overflow-hidden scroll-mt-28 grid grid-cols-1 lg:grid-cols-2 items-stretch">
  <img src="assets/img/{cat['img']}" alt="{cat['title']} &mdash; video editing style thumbnail" class="w-full h-64 lg:h-full object-cover" loading="lazy">
  <div class="p-8 sm:p-10 flex flex-col justify-center">
    <span class="badge w-fit mb-4">{cat['tag']}</span>
    <h3 class="font-display text-2xl font-bold text-white mb-3">{cat['title']}</h3>
    <p class="text-ink-400 leading-relaxed mb-6">{cat['desc']}</p>
    <a href="contact.html?project={cat['id']}" class="btn-outline w-fit"><i class="fa-solid fa-message"></i> Discuss This Style</a>
  </div>
</div>"""
    else:
        return f"""<a href="cuts.html#{cat['id']}" class="card overflow-hidden group block">
  <div class="overflow-hidden">
    <img src="assets/img/{cat['img']}" alt="{cat['title']}" class="w-full h-44 object-cover group-hover:scale-105 transition duration-300" loading="lazy">
  </div>
  <div class="p-5">
    <span class="badge !py-0.5 !px-2 text-[10px] mb-3">{cat['tag']}</span>
    <h3 class="font-display text-lg font-bold text-white group-hover:text-brand-400 transition">{cat['title']}</h3>
  </div>
</a>"""

def language_card(lang):
    accent = lang["accent"]
    return f"""<div class="card p-8">
  <div class="flex items-center justify-between mb-5">
    <span class="badge">{lang['native']}</span>
    <i class="fa-solid fa-waveform-lines text-{accent}-400"></i>
  </div>
  <h3 class="font-display text-2xl font-bold text-white mb-3">{lang['name']}</h3>
  <p class="text-ink-400 leading-relaxed mb-6 text-sm">{lang['desc']}</p>
  <div class="flex flex-col gap-3">
    <button type="button" disabled aria-disabled="true" title="Channel launching soon" class="btn justify-between border border-ink-700 text-ink-500 cursor-not-allowed opacity-70">
      <span class="flex items-center gap-2"><i class="fa-brands fa-youtube"></i> YouTube</span>
      <span class="text-[10px] uppercase tracking-wide badge !py-0.5 !px-2">Coming Soon</span>
    </button>
    <button type="button" disabled aria-disabled="true" title="Page launching soon" class="btn justify-between border border-ink-700 text-ink-500 cursor-not-allowed opacity-70">
      <span class="flex items-center gap-2"><i class="fa-brands fa-facebook"></i> Facebook</span>
      <span class="text-[10px] uppercase tracking-wide badge !py-0.5 !px-2">Coming Soon</span>
    </button>
  </div>
</div>"""

# ---------------------------------------------------------------------------
# INDEX
# ---------------------------------------------------------------------------

def build_index():
    cat_cards = "\n".join(category_card(c) for c in CATEGORIES[:6])
    main = f"""
<section class="relative overflow-hidden bg-grid-fade">
  <div class="container-page section-pad grid grid-cols-1 lg:grid-cols-2 gap-14 items-center">
    <div class="fade-up">
      <span class="eyebrow"><i class="fa-solid fa-clapperboard"></i> Video Editor &middot; Agency Founder &middot; Multilingual Creator</span>
      <h1 class="font-display text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white mt-5 leading-tight">Md. Shariful Islam</h1>
      <p class="text-lg text-ink-300 mt-5 max-w-xl leading-relaxed">I edit video, build brands, and create in three languages. I founded <span class="text-crimson-400 font-semibold">GoVidCo</span>, an international video-first production and growth agency, work individually with clients through my Top Rated <span class="text-brand-400 font-semibold">Upwork</span> profile, and create <span class="text-gold-400 font-semibold">Shariful Reflection</span> &mdash; a multilingual motivational and music channel in Bangla, Hindi, and English.</p>
      <div class="flex flex-wrap gap-4 mt-8">
        <a href="cuts.html" class="btn-primary"><i class="fa-solid fa-film"></i> View Portfolio</a>
        <a href="reflection.html" class="btn-gold-outline"><i class="fa-solid fa-om"></i> Enter Shariful Reflection</a>
      </div>
    </div>
    <div class="relative fade-up">
      <div class="absolute -inset-6 bg-brand-500/10 blur-3xl rounded-full"></div>
      <img src="assets/img/profile-hero.jpg" alt="Portrait of Md. Shariful Islam" class="relative rounded-3xl border border-ink-700 w-full max-w-md mx-auto object-cover shadow-2xl">
    </div>
  </div>
  <div class="container-page pb-20">
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
      {stat_tile("$20K+", "Earned via Upwork", "Individual client contracts", "brand")}
      {stat_tile("100%", "Job Success Score", "Upwork profile rating", "brand")}
      {stat_tile("Top Rated", "Upwork Status", "Individual freelance profile", "brand")}
      {stat_tile("3", "Languages", "Bangla &middot; Hindi &middot; English", "gold")}
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800">
  <div class="container-page">
    <div class="max-w-2xl mb-14">
      <span class="eyebrow"><i class="fa-solid fa-diagram-project"></i> How It Fits Together</span>
      <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mt-4">One Creative, Two Professional Engines</h2>
      <p class="text-ink-400 mt-4 leading-relaxed">GoVidCo and Upwork are not the same thing &mdash; they're two different doors into working with me, and Shariful Reflection is where the creative work lives outside of client projects.</p>
    </div>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="card p-8 border-crimson-900/60 hover:border-crimson-600/60 transition">
        <div class="h-12 w-12 rounded-xl bg-crimson-950/70 border border-crimson-800 flex items-center justify-center mb-6"><i class="fa-solid fa-building text-crimson-400 text-lg"></i></div>
        <h3 class="font-display text-xl font-bold text-white mb-3">GoVidCo</h3>
        <p class="text-sm text-ink-400 leading-relaxed mb-6">The official, international video-first production and growth agency I founded. GoVidCo is built for brands and creators who need a dedicated team, retainer-based growth partnerships, and scalable, multi-editor production.</p>
        <div class="flex flex-wrap gap-3">
          <a href="{GOVIDCO_URL}" target="_blank" rel="noopener noreferrer" class="btn-crimson-outline !px-4 !py-2 text-xs">Visit GoVidCo</a>
          <a href="cuts.html" class="btn-outline !px-4 !py-2 text-xs">See the Work</a>
        </div>
      </div>
      <div class="card p-8 border-brand-900/60 hover:border-brand-600/60 transition">
        <div class="h-12 w-12 rounded-xl bg-brand-950/70 border border-brand-800 flex items-center justify-center mb-6"><i class="fa-brands fa-upwork text-brand-400 text-lg"></i></div>
        <h3 class="font-display text-xl font-bold text-white mb-3">Upwork</h3>
        <p class="text-sm text-ink-400 leading-relaxed mb-6">My individual freelance profile for direct, one-to-one contracts. This is where clients hire <em>me</em> personally &mdash; not the agency &mdash; for a single project, hourly or fixed-price. Top Rated, 100% job success, $20K+ earned.</p>
        <div class="flex flex-wrap gap-3">
          <a href="{UPWORK_URL}" target="_blank" rel="noopener noreferrer" class="btn-primary !px-4 !py-2 text-xs">View Upwork Profile</a>
        </div>
      </div>
      <div class="card p-8 border-gold-900/60 hover:border-gold-600/60 transition">
        <div class="h-12 w-12 rounded-xl bg-gold-950/70 border border-gold-800 flex items-center justify-center mb-6"><i class="fa-solid fa-feather text-gold-400 text-lg"></i></div>
        <h3 class="font-display text-xl font-bold text-white mb-3">Shariful Reflection</h3>
        <p class="text-sm text-ink-400 leading-relaxed mb-6">A multilingual, AI-assisted motivational and music channel spanning Bangla, Hindi, and English &mdash; exploring reflection, discipline, and growth through short pieces and original sound.</p>
        <div class="flex flex-wrap gap-3">
          <a href="reflection.html" class="btn-gold !px-4 !py-2 text-xs">Enter Reflection</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800 bg-ink-900/30">
  <div class="container-page">
    <div class="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-6 mb-14">
      <div class="max-w-xl">
        <span class="eyebrow"><i class="fa-solid fa-layer-group"></i> Portfolio</span>
        <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mt-4">Six Ways I Edit Video</h2>
        <p class="text-ink-400 mt-4 leading-relaxed">From brand-consistent channel edits to short-form virality &mdash; every style GoVidCo and I produce, organized by purpose.</p>
      </div>
      <a href="cuts.html" class="btn-outline w-fit">Full Portfolio <i class="fa-solid fa-arrow-right"></i></a>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      {cat_cards}
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800">
  <div class="container-page">
    <div class="card overflow-hidden grid grid-cols-1 lg:grid-cols-2">
      <img src="assets/img/logo-reflection-card.jpg" alt="Shariful Reflection" class="w-full h-72 lg:h-full object-cover">
      <div class="p-8 sm:p-12 flex flex-col justify-center">
        <span class="eyebrow text-gold-400"><i class="fa-solid fa-om"></i> Shariful Reflection</span>
        <h2 class="font-display text-2xl sm:text-3xl font-bold text-white mt-4 mb-4">Motivation &amp; Music, in Three Languages</h2>
        <p class="text-ink-400 leading-relaxed mb-6">A creator project built with AI-assisted production, spanning Bangla, Hindi, and English &mdash; separate from client and agency work, this is where reflection and sound come first.</p>
        <div class="flex flex-wrap gap-3 mb-6">
          <span class="badge">বাংলা Bangla</span>
          <span class="badge">हिंदी Hindi</span>
          <span class="badge">English</span>
        </div>
        <a href="reflection.html" class="btn-gold w-fit">Visit the Reflection Hub <i class="fa-solid fa-arrow-right"></i></a>
      </div>
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800">
  <div class="container-page text-center max-w-2xl mx-auto">
    <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mb-4">Have a Project in Mind?</h2>
    <p class="text-ink-400 leading-relaxed mb-8">Whether it's a full agency partnership through GoVidCo, a direct contract on Upwork, or a creative collaboration on Reflection &mdash; let's talk.</p>
    <div class="flex flex-wrap justify-center gap-4">
      <a href="contact.html" class="btn-primary">Get in Touch</a>
      <a href="shop.html" class="btn-outline">See Packages &amp; Pricing</a>
    </div>
  </div>
</section>
"""
    return page(
        title="Md. Shariful Islam &mdash; Video Editor, Founder of GoVidCo &amp; Creator of Shariful Reflection",
        description="Md. Shariful Islam is a video editor and founder of GoVidCo, an international video-first production and growth agency. Top Rated on Upwork for individual contracts, and creator of Shariful Reflection, a multilingual motivational and music channel in Bangla, Hindi, and English.",
        page_file="index.html",
        main_html=main,
    )

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------

def build_about():
    timeline = [
        ("01", "First Cut", "Started as a self-taught video editor, learning Premiere Pro and After Effects by taking on small freelance jobs while studying the craft of pacing, color, and sound."),
        ("02", "Top Rated on Upwork", "Built an individual freelance profile on Upwork from the ground up &mdash; earning $20K+ across contracts with a 100% job success score and Top Rated status."),
        ("03", "Founded GoVidCo", "Turned a growing client base into GoVidCo &mdash; an international video-first production and growth agency built to serve brands and creators who need a full team, not just one editor."),
        ("04", "Launched Shariful Reflection", "Started Shariful Reflection, a multilingual, AI-assisted motivational and music channel in Bangla, Hindi, and English &mdash; a creative outlet separate from client work."),
    ]
    timeline_html = "\n".join(f"""
    <div class="relative pl-10 pb-12 last:pb-0 border-l border-ink-700 last:border-transparent">
      <span class="absolute -left-[15px] top-0 h-7 w-7 rounded-full bg-ink-900 border border-brand-500 text-brand-400 text-xs font-display font-bold flex items-center justify-center">{n}</span>
      <h3 class="font-display text-lg font-bold text-white mb-2">{t}</h3>
      <p class="text-sm text-ink-400 leading-relaxed max-w-xl">{d}</p>
    </div>""" for n, t, d in timeline)

    skills = ["Adobe Premiere Pro", "After Effects", "DaVinci Resolve", "Motion Graphics", "Color Grading", "Sound Design", "YouTube Growth Strategy", "AI-Assisted Production", "Multilingual Scriptwriting (EN/BN/HI)", "Short-Form Editing", "Brand Systems", "Team &amp; Workflow Management"]
    skills_html = "\n".join(f'<span class="badge">{s}</span>' for s in skills)

    main = f"""
<section class="section-pad bg-grid-fade">
  <div class="container-page grid grid-cols-1 lg:grid-cols-2 gap-14 items-center">
    <div class="fade-up order-2 lg:order-1">
      <span class="eyebrow"><i class="fa-solid fa-user"></i> About</span>
      <h1 class="font-display text-4xl sm:text-5xl font-extrabold text-white mt-5 leading-tight">The Person Behind GoVidCo &amp; Shariful Reflection</h1>
      <p class="text-lg text-ink-300 mt-5 leading-relaxed">I'm Md. Shariful Islam &mdash; a video editor first, and everything else grew from there. What started as freelance work on Upwork became an agency, and what started as a personal creative outlet became a multilingual channel with its own audience.</p>
      <p class="text-ink-400 mt-4 leading-relaxed">Today my work runs on three tracks: <span class="text-crimson-400 font-semibold">GoVidCo</span> for agency-scale production, <span class="text-brand-400 font-semibold">Upwork</span> for direct individual contracts, and <span class="text-gold-400 font-semibold">Shariful Reflection</span> for creative, multilingual content. Each has a distinct purpose &mdash; and this page exists to make that distinction clear.</p>
    </div>
    <div class="relative order-1 lg:order-2 fade-up">
      <div class="absolute -inset-6 bg-gold-500/10 blur-3xl rounded-full"></div>
      <img src="assets/img/profile-creator.jpg" alt="Md. Shariful Islam" class="relative rounded-3xl border border-ink-700 w-full max-w-md mx-auto object-cover shadow-2xl">
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800">
  <div class="container-page max-w-3xl">
    <span class="eyebrow"><i class="fa-solid fa-route"></i> Journey</span>
    <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mt-4 mb-12">From Freelance Editor to Agency Founder</h2>
    {timeline_html}
  </div>
</section>

<section class="section-pad border-t border-ink-800 bg-ink-900/30">
  <div class="container-page">
    <div class="max-w-2xl mb-12">
      <span class="eyebrow"><i class="fa-solid fa-circle-question"></i> How I Work</span>
      <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mt-4">GoVidCo vs. Upwork &mdash; What's the Difference?</h2>
      <p class="text-ink-400 mt-4 leading-relaxed">These are two separate ways to work with me, and it's worth being precise about which one fits your project.</p>
      <img src="assets/img/logo-govidco.jpg" alt="GoVidCo logo" class="h-10 mt-6 rounded-lg border border-ink-700">
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="card p-8 border-crimson-900/60">
        <div class="h-12 w-12 rounded-xl bg-crimson-950/70 border border-crimson-800 flex items-center justify-center mb-6"><i class="fa-solid fa-building text-crimson-400 text-lg"></i></div>
        <h3 class="font-display text-xl font-bold text-white mb-3">GoVidCo &mdash; The Agency</h3>
        <p class="text-sm text-ink-400 leading-relaxed mb-4">GoVidCo is the official, international video-first production and growth agency I founded and lead. It's built for brands and creators who want:</p>
        <ul class="space-y-2 text-sm text-ink-300 mb-6">
          <li class="flex gap-2"><i class="fa-solid fa-check text-crimson-400 mt-1"></i>A dedicated production team, not just one editor</li>
          <li class="flex gap-2"><i class="fa-solid fa-check text-crimson-400 mt-1"></i>Retainer-based, ongoing channel growth partnerships</li>
          <li class="flex gap-2"><i class="fa-solid fa-check text-crimson-400 mt-1"></i>Scalable output across multiple platforms</li>
        </ul>
        <a href="{GOVIDCO_URL}" target="_blank" rel="noopener noreferrer" class="btn-crimson-outline !px-4 !py-2 text-xs">Visit govidco.com</a>
      </div>
      <div class="card p-8 border-brand-900/60">
        <div class="h-12 w-12 rounded-xl bg-brand-950/70 border border-brand-800 flex items-center justify-center mb-6"><i class="fa-brands fa-upwork text-brand-400 text-lg"></i></div>
        <h3 class="font-display text-xl font-bold text-white mb-3">Upwork &mdash; Individual Contracts</h3>
        <p class="text-sm text-ink-400 leading-relaxed mb-4">My Upwork profile is my individual freelance presence &mdash; separate from GoVidCo. It's the right fit when a client wants to:</p>
        <ul class="space-y-2 text-sm text-ink-300 mb-6">
          <li class="flex gap-2"><i class="fa-solid fa-check text-brand-400 mt-1"></i>Hire me personally for a single project or short contract</li>
          <li class="flex gap-2"><i class="fa-solid fa-check text-brand-400 mt-1"></i>Work hourly or fixed-price through Upwork's platform</li>
          <li class="flex gap-2"><i class="fa-solid fa-check text-brand-400 mt-1"></i>Rely on a Top Rated, 100% job-success track record</li>
        </ul>
        <a href="{UPWORK_URL}" target="_blank" rel="noopener noreferrer" class="btn-primary !px-4 !py-2 text-xs">View Upwork Profile</a>
      </div>
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800">
  <div class="container-page">
    <span class="eyebrow"><i class="fa-solid fa-toolbox"></i> Toolkit</span>
    <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mt-4 mb-10">Skills &amp; Tools</h2>
    <div class="flex flex-wrap gap-3">
      {skills_html}
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800 bg-ink-900/30">
  <div class="container-page text-center max-w-2xl mx-auto">
    <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mb-4">Let's Work Together</h2>
    <p class="text-ink-400 leading-relaxed mb-8">Tell me about your project and I'll point you to the right door &mdash; GoVidCo or Upwork.</p>
    <a href="contact.html" class="btn-primary">Get in Touch</a>
  </div>
</section>
"""
    return page(
        title="About Md. Shariful Islam &mdash; Video Editor &amp; Founder of GoVidCo",
        description="Learn about Md. Shariful Islam's journey from freelance video editor to founding GoVidCo, and the clear distinction between GoVidCo (agency) and his individual Upwork profile.",
        page_file="about.html",
        main_html=main,
    )

# ---------------------------------------------------------------------------
# CUTS (Portfolio)
# ---------------------------------------------------------------------------

def build_cuts():
    cards = "\n<div class=\"h-6\"></div>\n".join(category_card(c, expanded=True) for c in CATEGORIES)
    quick_nav = "\n".join(f'<a href="#{c["id"]}" class="badge hover:border-brand-400 hover:text-brand-300 transition">{c["title"]}</a>' for c in CATEGORIES)
    main = f"""
<section class="section-pad bg-grid-fade">
  <div class="container-page max-w-3xl">
    <span class="eyebrow"><i class="fa-solid fa-film"></i> Portfolio</span>
    <h1 class="font-display text-4xl sm:text-5xl font-extrabold text-white mt-5 leading-tight">Video Editing Portfolio</h1>
    <p class="text-lg text-ink-300 mt-5 leading-relaxed">Six styles of edit, built across client work through GoVidCo and individual Upwork contracts &mdash; organized by what each one is built to do, not just how it looks.</p>
    <div class="flex flex-wrap gap-2 mt-8">
      {quick_nav}
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800">
  <div class="container-page space-y-6">
    {cards}
  </div>
</section>

<section class="section-pad border-t border-ink-800 bg-ink-900/30">
  <div class="container-page text-center max-w-2xl mx-auto">
    <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mb-4">See Something You Like?</h2>
    <p class="text-ink-400 leading-relaxed mb-8">Check GoVidCo service packages, or reach out directly to scope your project.</p>
    <div class="flex flex-wrap justify-center gap-4">
      <a href="shop.html" class="btn-primary">View Packages &amp; Pricing</a>
      <a href="contact.html" class="btn-outline">Start a Conversation</a>
    </div>
  </div>
</section>
"""
    return page(
        title="Video Editing Portfolio &mdash; Md. Shariful Islam &amp; GoVidCo",
        description="Explore six video editing styles from Md. Shariful Islam and GoVidCo: Brand Guardian, Authority, Viral Engine, Converter, Flagship, and Automation Engine.",
        page_file="cuts.html",
        main_html=main,
    )

# ---------------------------------------------------------------------------
# SHOP
# ---------------------------------------------------------------------------

def build_shop():
    service_tiers = [
        {
            "name": "Starter Cut", "accent": "brand", "price": "From $150", "unit": "/ video",
            "desc": "For solo creators and one-off projects that need a single, polished edit.",
            "features": ["Single video edit (up to 15 min raw footage)", "Standard color grade", "Captions &amp; basic sound design", "2 rounds of revisions", "3&ndash;5 day turnaround"],
            "cta": "Book a Discovery Call",
        },
        {
            "name": "Growth Retainer", "accent": "crimson", "price": "From $1,200", "unit": "/ month", "featured": True,
            "desc": "For channels scaling weekly output, managed through GoVidCo.",
            "features": ["4&ndash;8 videos per month", "Dedicated GoVidCo editor", "Thumbnail design included", "Content calendar sync", "Priority turnaround"],
            "cta": "Talk to GoVidCo",
        },
        {
            "name": "Agency Partnership", "accent": "gold", "price": "Custom Quote", "unit": "",
            "desc": "Full production and growth partnership for established brands.",
            "features": ["Dedicated multi-editor team", "Multi-platform repurposing", "Monthly strategy calls", "Analytics &amp; reporting", "Custom SLAs"],
            "cta": "Request a Proposal",
        },
    ]

    BTN_CLASS = {"brand": "btn-primary", "crimson": "btn-crimson", "gold": "btn-gold"}

    def tier_card(t):
        featured = t.get("featured")
        border = f"border-{t['accent']}-500/70 ring-1 ring-{t['accent']}-500/40" if featured else "border-ink-700/70"
        badge = f'<span class="badge !border-{t["accent"]}-600 !text-{t["accent"]}-300 absolute -top-3 left-8">Most Popular</span>' if featured else ""
        feats = "\n".join(f'<li class="flex gap-2 text-sm text-ink-300"><i class="fa-solid fa-check text-{t["accent"]}-400 mt-1"></i>{f}</li>' for f in t["features"])
        btn_cls = BTN_CLASS[t["accent"]]
        return f"""<div class="relative card p-8 {border} flex flex-col">
      {badge}
      <h3 class="font-display text-xl font-bold text-white mb-2">{t['name']}</h3>
      <p class="text-sm text-ink-400 mb-6">{t['desc']}</p>
      <div class="mb-6">
        <span class="font-display text-3xl font-bold text-white">{t['price']}</span>
        <span class="text-sm text-ink-500">{t['unit']}</span>
      </div>
      <ul class="space-y-3 mb-8 flex-1">{feats}</ul>
      <a href="contact.html?package={t['name'].lower().replace(' ', '-')}" class="{btn_cls} w-full">{t['cta']}</a>
    </div>"""

    tiers_html = "\n".join(tier_card(t) for t in service_tiers)

    products = [
        {"name": "Reflection Music Vol. 1", "price": "$19", "desc": "A royalty-free instrumental pack drawn from the Shariful Reflection score library &mdash; built for creators who want original, motivational underscore for their own videos.", "icon": "fa-music"},
        {"name": "Multilingual Motivational Script Pack", "price": "$29", "desc": "30 ready-to-record reflection scripts across English, Bangla, and Hindi &mdash; the same writing framework used across the Shariful Reflection channels.", "icon": "fa-file-lines"},
        {"name": "Cinematic Color LUT Pack", "price": "$15", "desc": "The exact color LUTs used across GoVidCo's Flagship-style edits, built for DaVinci Resolve and Premiere Pro.", "icon": "fa-palette"},
    ]
    product_cards = "\n".join(f"""<div class="card p-8">
      <div class="h-12 w-12 rounded-xl bg-gold-950/70 border border-gold-800 flex items-center justify-center mb-6"><i class="fa-solid {p['icon']} text-gold-400 text-lg"></i></div>
      <h3 class="font-display text-lg font-bold text-white mb-2">{p['name']}</h3>
      <p class="text-sm text-ink-400 leading-relaxed mb-6">{p['desc']}</p>
      <div class="flex items-center justify-between">
        <span class="font-display text-2xl font-bold text-white">{p['price']}</span>
        <a href="contact.html?product={p['name'].lower().replace(' ', '-')}" class="btn-gold-outline !px-4 !py-2 text-xs">Request Access</a>
      </div>
    </div>""" for p in products)

    main = f"""
<section class="section-pad bg-grid-fade">
  <div class="container-page max-w-3xl">
    <span class="eyebrow"><i class="fa-solid fa-bag-shopping"></i> Shop</span>
    <h1 class="font-display text-4xl sm:text-5xl font-extrabold text-white mt-5 leading-tight">Packages &amp; Digital Products</h1>
    <p class="text-lg text-ink-300 mt-5 leading-relaxed">Video editing service packages for brands and creators, plus digital products from the Shariful Reflection library. Final pricing on service packages depends on project scope &mdash; every number below is a starting point.</p>
  </div>
</section>

<section class="section-pad border-t border-ink-800">
  <div class="container-page">
    <span class="eyebrow"><i class="fa-solid fa-video"></i> Video Editing</span>
    <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mt-4 mb-12">Service Packages</h2>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 items-start">
      {tiers_html}
    </div>
    <p class="text-xs text-ink-500 mt-8">Single-project, direct-hire work is also available through my <a href="{UPWORK_URL}" target="_blank" rel="noopener noreferrer" class="text-brand-400 hover:underline">Upwork profile</a>. Retainer and agency-scale packages are delivered through GoVidCo.</p>
  </div>
</section>

<section class="section-pad border-t border-ink-800 bg-ink-900/30">
  <div class="container-page">
    <span class="eyebrow text-gold-400"><i class="fa-solid fa-om"></i> Shariful Reflection</span>
    <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mt-4 mb-12">Digital Products</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      {product_cards}
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800">
  <div class="container-page text-center max-w-2xl mx-auto">
    <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mb-4">Not Sure Which Fits?</h2>
    <p class="text-ink-400 leading-relaxed mb-8">Send me a quick note about your project and I'll point you to the right package.</p>
    <a href="contact.html" class="btn-primary">Get in Touch</a>
  </div>
</section>
"""
    return page(
        title="Shop &mdash; Video Editing Packages &amp; Reflection Digital Products",
        description="Video editing service packages from Md. Shariful Islam and GoVidCo, plus digital products from the Shariful Reflection library: music, scripts, and color LUTs.",
        page_file="shop.html",
        main_html=main,
    )

# ---------------------------------------------------------------------------
# REFLECTION
# ---------------------------------------------------------------------------

def build_reflection():
    lang_cards = "\n".join(language_card(l) for l in LANGUAGES)
    main = f"""
<section class="section-pad bg-grid-fade">
  <div class="container-page grid grid-cols-1 lg:grid-cols-2 gap-14 items-center">
    <div class="fade-up">
      <span class="eyebrow text-gold-400"><i class="fa-solid fa-om"></i> Shariful Reflection</span>
      <h1 class="font-display text-4xl sm:text-5xl font-extrabold text-white mt-5 leading-tight">Motivation &amp; Music, in Three Languages</h1>
      <p class="text-lg text-ink-300 mt-5 leading-relaxed">Shariful Reflection is a multilingual, AI-assisted creative project &mdash; reflections on discipline, stillness, and growth, paired with original music, across Bangla, Hindi, and English.</p>
      <p class="text-ink-400 mt-4 leading-relaxed">This is separate from GoVidCo client work and Upwork contracts &mdash; it's the creative project that exists on its own terms.</p>
    </div>
    <div class="relative fade-up">
      <div class="absolute -inset-6 bg-gold-500/10 blur-3xl rounded-full"></div>
      <img src="assets/img/logo-reflection-card.jpg" alt="Shariful Reflection" class="relative rounded-3xl border border-ink-700 w-full max-w-md mx-auto object-cover shadow-2xl">
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800">
  <div class="container-page">
    <span class="eyebrow"><i class="fa-solid fa-language"></i> Channels</span>
    <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mt-4 mb-4">One Message, Three Languages</h2>
    <p class="text-ink-400 max-w-2xl mb-12 leading-relaxed">Each language channel is being built out individually. Links go live as each one launches &mdash; check back, or get in touch to be notified.</p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      {lang_cards}
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800 bg-ink-900/30">
  <div class="container-page grid grid-cols-1 lg:grid-cols-3 gap-8">
    <div class="lg:col-span-1">
      <span class="eyebrow"><i class="fa-solid fa-seedling"></i> Themes</span>
      <h2 class="font-display text-2xl sm:text-3xl font-bold text-white mt-4">What Reflection Is About</h2>
    </div>
    <div class="lg:col-span-2 grid grid-cols-1 sm:grid-cols-3 gap-6">
      <div class="card p-6">
        <i class="fa-solid fa-mountain text-gold-400 text-xl mb-4"></i>
        <h3 class="font-semibold text-white mb-2">Discipline</h3>
        <p class="text-sm text-ink-400 leading-relaxed">Short reflections on consistency, focus, and doing the work when motivation runs out.</p>
      </div>
      <div class="card p-6">
        <i class="fa-solid fa-water text-gold-400 text-xl mb-4"></i>
        <h3 class="font-semibold text-white mb-2">Stillness</h3>
        <p class="text-sm text-ink-400 leading-relaxed">Music and narration built for quiet moments &mdash; a counterweight to fast content.</p>
      </div>
      <div class="card p-6">
        <i class="fa-solid fa-arrow-trend-up text-gold-400 text-xl mb-4"></i>
        <h3 class="font-semibold text-white mb-2">Growth</h3>
        <p class="text-sm text-ink-400 leading-relaxed">Stories and sound about long-term progress, in three languages and one voice.</p>
      </div>
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800">
  <div class="container-page text-center max-w-2xl mx-auto">
    <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mb-4">Want to Collaborate?</h2>
    <p class="text-ink-400 leading-relaxed mb-8">Music licensing, guest collaborations, and early access &mdash; reach out directly.</p>
    <a href="contact.html" class="btn-gold">Get in Touch</a>
  </div>
</section>
"""
    return page(
        title="Shariful Reflection &mdash; Multilingual Motivational &amp; Music Channel",
        description="Shariful Reflection is Md. Shariful Islam's multilingual, AI-assisted motivational and music channel, spanning Bangla, Hindi, and English.",
        page_file="reflection.html",
        main_html=main,
    )

# ---------------------------------------------------------------------------
# SOP — Remote Work Briefing: Operational Blueprint & Standards
# ---------------------------------------------------------------------------

SOP_SECTIONS = [
    {
        "num": "01",
        "title": "Remote Operating Philosophy &amp; Storytelling Workflows",
        "icon": "fa-clapperboard",
        "body": "Our core production framework prioritizes narrative-first video storytelling, balancing high-conversion advertising creatives with viral short-form loops and long-form brand building. Every frame must actively serve the campaign goal.",
    },
    {
        "num": "02",
        "title": "Transparency &amp; Notion-Based Milestone Tracking",
        "icon": "fa-table-list",
        "body": "All operations run through a centralized Notion database. Every delivery milestone, revision cycle, and client sign-off is logged and tracked to ensure absolute accountability and real-time project visibility.",
    },
    {
        "num": "03",
        "title": "Asset Routing, Data Security &amp; QA Checkpoints",
        "icon": "fa-shield-halved",
        "body": "High-volume project files from DaVinci Resolve and Premiere are managed through decentralized, secure file-routing mechanisms. We enforce strict multi-tiered quality assurance checkpoints and adhere to robust data security standards to protect client assets.",
    },
    {
        "num": "04",
        "title": "Global Delivery &amp; Team Standards",
        "icon": "fa-globe",
        "body": "As an international video-first production and growth agency, our distributed team maintains high-speed internet compliance, secure home workstation environments, and synchronized communication schedules to guarantee consistent global delivery.",
    },
]

def sop_section(s, index, total):
    border_bottom = "" if index == total - 1 else "border-b border-ink-800"
    return f"""<section id="section-{s['num']}" aria-labelledby="section-{s['num']}-title" class="scroll-mt-28 py-12 {border_bottom}">
  <div class="grid grid-cols-1 md:grid-cols-[auto_1fr] gap-6 md:gap-10">
    <div class="flex md:flex-col items-center md:items-start gap-4 md:gap-3">
      <span class="font-display text-4xl sm:text-5xl font-bold text-brand-500/80 tabular-nums">{s['num']}</span>
      <span class="h-10 w-10 rounded-lg bg-crimson-950/70 border border-crimson-800 flex items-center justify-center">
        <i class="fa-solid {s['icon']} text-crimson-400"></i>
      </span>
    </div>
    <div>
      <h2 id="section-{s['num']}-title" class="font-display text-xl sm:text-2xl font-bold text-white mb-4 leading-snug">{s['title']}</h2>
      <p class="text-ink-400 leading-relaxed max-w-3xl">{s['body']}</p>
    </div>
  </div>
</section>"""

def build_sop():
    sections_html = "\n".join(sop_section(s, i, len(SOP_SECTIONS)) for i, s in enumerate(SOP_SECTIONS))
    toc_html = "\n".join(
        f'<a href="#section-{s["num"]}" class="flex items-center gap-3 px-4 py-3 rounded-lg border border-ink-700 hover:border-brand-400/60 hover:bg-ink-900 transition group">'
        f'<span class="font-display text-xs text-brand-400">{s["num"]}</span>'
        f'<span class="text-sm text-ink-300 group-hover:text-white transition">{s["title"]}</span>'
        f'</a>'
        for s in SOP_SECTIONS
    )
    main = f"""
<section class="section-pad bg-grid-fade">
  <div class="container-page max-w-3xl">
    <span class="eyebrow"><i class="fa-solid fa-file-lines"></i> Internal Documentation</span>
    <h1 class="font-display text-4xl sm:text-5xl font-extrabold text-white mt-5 leading-tight">Remote Work Briefing</h1>
    <p class="text-lg text-crimson-400 font-semibold mt-2">Operational Blueprint &amp; Standards</p>
    <p class="text-ink-400 mt-5 leading-relaxed max-w-2xl">A reference standard for how GoVidCo's distributed production team operates &mdash; storytelling workflow, milestone tracking, asset security, and global delivery expectations. Four sections, summarized below and available as a downloadable PDF.</p>
    <div class="flex flex-wrap gap-4 mt-8">
      <a href="assets/docs/remote-work-briefing.pdf" download class="btn-primary">
        <i class="fa-solid fa-file-arrow-down"></i> Download PDF Briefing
      </a>
      <a href="#section-01" class="btn-outline">
        <i class="fa-solid fa-arrow-down"></i> Read Below
      </a>
    </div>
  </div>
</section>

<section class="border-t border-ink-800">
  <div class="container-page py-12">
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
      {toc_html}
    </div>
  </div>
</section>

<section class="border-t border-ink-800">
  <div class="container-page max-w-4xl">
    {sections_html}
  </div>
</section>

<section class="section-pad border-t border-ink-800 bg-ink-900/30">
  <div class="container-page">
    <div class="card p-8 sm:p-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-6 border-crimson-900/60">
      <div>
        <span class="eyebrow"><i class="fa-solid fa-file-pdf"></i> Full Document</span>
        <h2 class="font-display text-xl sm:text-2xl font-bold text-white mt-3">Keep a Copy On Hand</h2>
        <p class="text-sm text-ink-400 mt-2 max-w-xl">The PDF version of this briefing is the reference copy for onboarding, client handoffs, and offline review.</p>
      </div>
      <a href="assets/docs/remote-work-briefing.pdf" download class="btn-primary w-fit shrink-0">
        <i class="fa-solid fa-file-arrow-down"></i> Download PDF
      </a>
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800">
  <div class="container-page text-center max-w-2xl mx-auto">
    <h2 class="font-display text-3xl sm:text-4xl font-bold text-white mb-4">Questions About These Standards?</h2>
    <p class="text-ink-400 leading-relaxed mb-8">For clients: this is how your project stays on track. For collaborators: this is how we work.</p>
    <a href="contact.html" class="btn-outline">Get in Touch</a>
  </div>
</section>
"""
    return page(
        title="Remote Work Briefing &mdash; Operational Blueprint &amp; Standards | GoVidCo",
        description="GoVidCo's Remote Work Briefing: operational blueprint and standards covering storytelling workflow, Notion-based milestone tracking, asset security and QA checkpoints, and global delivery standards.",
        page_file="sop.html",
        main_html=main,
    )

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------

def build_contact():
    main = f"""
<section class="section-pad bg-grid-fade">
  <div class="container-page max-w-3xl">
    <span class="eyebrow"><i class="fa-solid fa-message"></i> Contact</span>
    <h1 class="font-display text-4xl sm:text-5xl font-extrabold text-white mt-5 leading-tight">Let's Build Something</h1>
    <p class="text-lg text-ink-300 mt-5 leading-relaxed">Three ways to reach me, depending on what you need. Pick the right door and I'll take it from there.</p>
  </div>
</section>

<section class="border-t border-ink-800">
  <div class="container-page py-14">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="card p-8 border-crimson-900/60">
        <div class="h-12 w-12 rounded-xl bg-crimson-950/70 border border-crimson-800 flex items-center justify-center mb-6"><i class="fa-solid fa-building text-crimson-400 text-lg"></i></div>
        <h3 class="font-display text-lg font-bold text-white mb-2">Agency Projects</h3>
        <p class="text-sm text-ink-400 leading-relaxed mb-6">Full production, retainer growth, or team-based work &mdash; go through GoVidCo.</p>
        <a href="{GOVIDCO_URL}" target="_blank" rel="noopener noreferrer" class="btn-crimson-outline !px-4 !py-2 text-xs w-fit">Visit GoVidCo</a>
      </div>
      <div class="card p-8 border-brand-900/60">
        <div class="h-12 w-12 rounded-xl bg-brand-950/70 border border-brand-800 flex items-center justify-center mb-6"><i class="fa-brands fa-upwork text-brand-400 text-lg"></i></div>
        <h3 class="font-display text-lg font-bold text-white mb-2">Individual Contracts</h3>
        <p class="text-sm text-ink-400 leading-relaxed mb-6">A single project, hourly or fixed-price, direct with me &mdash; through Upwork.</p>
        <a href="{UPWORK_URL}" target="_blank" rel="noopener noreferrer" class="btn-primary !px-4 !py-2 text-xs w-fit">View Upwork Profile</a>
      </div>
      <div class="card p-8 border-gold-900/60">
        <div class="h-12 w-12 rounded-xl bg-gold-950/70 border border-gold-800 flex items-center justify-center mb-6"><i class="fa-solid fa-envelope text-gold-400 text-lg"></i></div>
        <h3 class="font-display text-lg font-bold text-white mb-2">Everything Else</h3>
        <p class="text-sm text-ink-400 leading-relaxed mb-6">General questions, Reflection collaborations, or anything in between.</p>
        <a href="mailto:{EMAIL}" class="btn-gold-outline !px-4 !py-2 text-xs w-fit">{EMAIL}</a>
      </div>
    </div>
  </div>
</section>

<section class="section-pad border-t border-ink-800 bg-ink-900/30">
  <div class="container-page grid grid-cols-1 lg:grid-cols-5 gap-14">
    <div class="lg:col-span-2">
      <span class="eyebrow"><i class="fa-solid fa-paper-plane"></i> Direct Message</span>
      <h2 class="font-display text-3xl font-bold text-white mt-4 mb-4">Send a Quick Note</h2>
      <p class="text-ink-400 leading-relaxed mb-6">This form opens your email client with the message pre-filled &mdash; nothing is sent through a third-party server.</p>
      <ul class="space-y-4 text-sm text-ink-300">
        <li class="flex gap-3"><i class="fa-solid fa-envelope text-brand-400 mt-1"></i>{EMAIL}</li>
        <li class="flex gap-3"><i class="fa-solid fa-building text-crimson-400 mt-1"></i>GoVidCo &mdash; <a href="{GOVIDCO_URL}" target="_blank" rel="noopener noreferrer" class="hover:text-white underline decoration-ink-600">govidco.com</a></li>
        <li class="flex gap-3"><i class="fa-brands fa-upwork text-brand-400 mt-1"></i>Upwork &mdash; <a href="{UPWORK_URL}" target="_blank" rel="noopener noreferrer" class="hover:text-white underline decoration-ink-600">Top Rated Profile</a></li>
      </ul>
    </div>
    <div class="lg:col-span-3">
      <form id="contact-form" class="card p-8 space-y-5">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
          <div>
            <label for="name" class="block text-sm font-medium text-ink-300 mb-2">Name</label>
            <input type="text" id="name" name="name" required class="w-full rounded-lg bg-ink-950 border border-ink-700 px-4 py-3 text-sm text-white placeholder-ink-500 focus:outline-none focus:border-brand-400" placeholder="Your name">
          </div>
          <div>
            <label for="email" class="block text-sm font-medium text-ink-300 mb-2">Email</label>
            <input type="email" id="email" name="email" required class="w-full rounded-lg bg-ink-950 border border-ink-700 px-4 py-3 text-sm text-white placeholder-ink-500 focus:outline-none focus:border-brand-400" placeholder="you@email.com">
          </div>
        </div>
        <div>
          <label for="interest" class="block text-sm font-medium text-ink-300 mb-2">I'm interested in</label>
          <select id="interest" name="interest" class="w-full rounded-lg bg-ink-950 border border-ink-700 px-4 py-3 text-sm text-white focus:outline-none focus:border-brand-400">
            <option>GoVidCo &mdash; Agency Project</option>
            <option>Upwork &mdash; Individual Contract</option>
            <option>Shop &mdash; Package or Product</option>
            <option>Shariful Reflection Collaboration</option>
            <option>Something Else</option>
          </select>
        </div>
        <div>
          <label for="message" class="block text-sm font-medium text-ink-300 mb-2">Message</label>
          <textarea id="message" name="message" rows="5" required class="w-full rounded-lg bg-ink-950 border border-ink-700 px-4 py-3 text-sm text-white placeholder-ink-500 focus:outline-none focus:border-brand-400" placeholder="Tell me about your project..."></textarea>
        </div>
        <button type="submit" class="btn-primary w-full sm:w-fit"><i class="fa-solid fa-paper-plane"></i> Send Message</button>
        <p id="contact-fallback" class="hidden text-xs text-ink-500">Your email client didn't open automatically &mdash; email me directly at <a href="mailto:{EMAIL}" class="text-brand-400 hover:underline">{EMAIL}</a>.</p>
      </form>
    </div>
  </div>
</section>
"""
    return page(
        title="Contact Md. Shariful Islam &mdash; GoVidCo, Upwork &amp; Shariful Reflection",
        description="Get in touch with Md. Shariful Islam for GoVidCo agency projects, individual Upwork contracts, Shop packages, or Shariful Reflection collaborations.",
        page_file="contact.html",
        main_html=main,
    )

# ---------------------------------------------------------------------------
# 404
# ---------------------------------------------------------------------------

def build_404():
    main = f"""
<section class="section-pad min-h-[70vh] flex items-center bg-grid-fade">
  <div class="container-page text-center">
    <img src="assets/img/mark-nav.png" alt="{SITE_NAME} mark" class="h-16 w-16 rounded-full ring-1 ring-ink-700 mx-auto mb-8">
    <p class="font-display text-7xl sm:text-8xl font-extrabold text-brand-500/80">404</p>
    <h1 class="font-display text-2xl sm:text-3xl font-bold text-white mt-4 mb-4">This Page Didn't Make the Final Cut</h1>
    <p class="text-ink-400 max-w-md mx-auto leading-relaxed mb-10">The page you're looking for doesn't exist or has moved. Let's get you back on track.</p>
    <div class="flex flex-wrap justify-center gap-4">
      <a href="index.html" class="btn-primary"><i class="fa-solid fa-house"></i> Back Home</a>
      <a href="cuts.html" class="btn-outline">View Portfolio</a>
      <a href="contact.html" class="btn-outline">Contact Me</a>
    </div>
  </div>
</section>
"""
    return page(
        title="Page Not Found &mdash; Md. Shariful Islam",
        description="The page you're looking for doesn't exist or has moved.",
        page_file="404.html",
        main_html=main,
    )

# ---------------------------------------------------------------------------
# Build all
# ---------------------------------------------------------------------------

PAGES = {
    "index.html": build_index,
    "about.html": build_about,
    "cuts.html": build_cuts,
    "shop.html": build_shop,
    "reflection.html": build_reflection,
    "sop.html": build_sop,
    "contact.html": build_contact,
    "404.html": build_404,
}

if __name__ == "__main__":
    for filename, fn in PAGES.items():
        html = fn()
        out_path = os.path.join(ROOT, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"wrote {filename} ({len(html)} bytes)")
