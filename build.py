#!/usr/bin/env python3
"""
HELLOBAR AUTHORITY ENGINE 2026
Ultimate Programmatic SEO Builder
Deploy Target:
https://brightlane.github.io/hellobar/

Author: Benny Palmarino
Affiliate ID: benpalmarini6380
"""

import os
import re
import html
import random
from pathlib import Path
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

# =========================================================
# CONFIG
# =========================================================

CONFIG = {
    "SITE_NAME": "HelloBar Authority",
    "BASE_URL": "https://brightlane.github.io/hellobar",
    "AUTHOR": "Benny Palmarino",
    "AFFILIATE_ID": "benpalmarini6380",
    "AFFILIATE_URL": "https://try.hellobar.com/benpalmarini6380?utm_source=deploy",
    "OUTPUT_DIR": "site",
    "DESCRIPTION": (
        "Hello Bar popup software reviews, CRO strategies, "
        "exit intent guides, lead generation systems and "
        "affiliate marketing optimization."
    ),
}

# =========================================================
# MASSIVE SEO DATA
# =========================================================

NICHES = [
    "Affiliate Marketing",
    "Real Estate",
    "Dental",
    "Roofing",
    "HVAC",
    "Local SEO",
    "Fitness",
    "Crypto",
    "Law Firms",
    "Travel Blogs",
    "Agencies",
    "Ecommerce",
    "SaaS",
    "Course Creators",
    "Insurance",
    "Consulting",
    "Podcasting",
]

POPUP_TYPES = [
    "Exit Intent",
    "Slide In",
    "Top Bar",
    "Alert Bar",
    "Fullscreen Popup",
    "Coupon Popup",
    "Email Capture",
]

KEYWORDS = [
    "Guide",
    "Review",
    "Blueprint",
    "Tutorial",
    "Case Study",
    "Strategy",
]

BENEFITS = [
    "increase conversions",
    "capture more leads",
    "recover abandoning visitors",
    "grow email subscribers",
    "improve affiliate commissions",
    "boost ecommerce sales",
    "scale agency clients",
]

FEATURES = [
    "Exit-intent detection",
    "A/B testing",
    "Mobile optimized popups",
    "Scroll triggers",
    "Geo targeting",
    "Advanced analytics",
    "Email integrations",
    "Conversion tracking",
    "Unlimited campaigns",
    "Lead segmentation",
]

# =========================================================
# HELPERS
# =========================================================

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def save_file(path, content):
    ensure_dir(os.path.dirname(path))

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# =========================================================
# SEO PAGE GENERATOR
# =========================================================

def generate_posts():
    posts = []

    for niche in NICHES:
        for popup in POPUP_TYPES:
            for keyword in KEYWORDS:

                slug = slugify(
                    f"hello-bar-{popup}-{niche}-{keyword}"
                )

                title = (
                    f"Hello Bar {popup} for "
                    f"{niche}: 2026 {keyword}"
                )

                description = (
                    f"Learn how {niche} websites use "
                    f"Hello Bar {popup.lower()} campaigns "
                    f"to {random.choice(BENEFITS)}."
                )

                posts.append({
                    "slug": slug,
                    "title": title,
                    "description": description,
                    "niche": niche,
                    "popup": popup,
                    "keyword": keyword,
                })

    return posts


# =========================================================
# CSS
# =========================================================

def styles():
    return """
<style>

:root{
    --bg:#0f172a;
    --card:#111827;
    --text:#f1f5f9;
    --muted:#94a3b8;
    --accent:#10b981;
    --orange:#f97316;
}

*{
    box-sizing:border-box;
}

body{
    margin:0;
    font-family:Inter,system-ui,sans-serif;
    background:var(--bg);
    color:var(--text);
    line-height:1.7;
}

.container{
    width:min(1150px,92%);
    margin:auto;
}

.hero{
    margin:30px 0;
    padding:80px 30px;
    border-radius:24px;
    text-align:center;
    background:linear-gradient(135deg,#ff6b6b,#f59e0b);
}

.hero h1{
    font-size:3rem;
    margin-bottom:20px;
}

.hero p{
    font-size:1.2rem;
}

.button{
    display:inline-block;
    background:var(--accent);
    color:#fff;
    padding:16px 30px;
    border-radius:14px;
    text-decoration:none;
    font-weight:700;
    margin-top:20px;
}

.grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:24px;
}

.card{
    background:var(--card);
    border:1px solid #1e293b;
    border-radius:18px;
    padding:24px;
}

.card h3{
    margin-top:0;
}

a{
    color:#93c5fd;
    text-decoration:none;
}

table{
    width:100%;
    border-collapse:collapse;
    margin:30px 0;
}

th,td{
    border:1px solid #334155;
    padding:12px;
}

th{
    background:#1e293b;
}

.cta{
    margin:50px 0;
    padding:50px;
    border-radius:24px;
    text-align:center;
    background:linear-gradient(135deg,#16a34a,#15803d);
}

footer{
    padding:40px 0;
    text-align:center;
    color:var(--muted);
}

.meta{
    color:var(--muted);
    margin-bottom:20px;
}

ul{
    padding-left:20px;
}

</style>
"""


# =========================================================
# SCHEMA
# =========================================================

def article_schema(post):

    return f"""
<script type="application/ld+json">
{{
    "@context":"https://schema.org",
    "@type":"Article",
    "headline":"{html.escape(post['title'])}",
    "description":"{html.escape(post['description'])}",
    "author":{{
        "@type":"Person",
        "name":"{CONFIG['AUTHOR']}"
    }},
    "publisher":{{
        "@type":"Organization",
        "name":"HelloBar Authority"
    }},
    "datePublished":"{datetime.utcnow().strftime('%Y-%m-%d')}",
    "mainEntityOfPage":"{CONFIG['BASE_URL']}/blog/{post['slug']}.html"
}}
</script>
"""


# =========================================================
# HTML WRAPPER
# =========================================================

def page_template(title, description, content, canonical, extra_head=""):

    return f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{html.escape(title)}</title>

<meta name="description" content="{html.escape(description)}">

<link rel="canonical" href="{canonical}">

<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="website">

<meta name="robots" content="index,follow">

{styles()}

{extra_head}

</head>

<body>

<div class="container">

{content}

<footer>
<p>
© {datetime.now().year} {CONFIG['AUTHOR']}
•
HelloBar Authority Engine
•
Built for AI Search + SEO
</p>
</footer>

</div>

</body>
</html>
"""


# =========================================================
# RELATED POSTS
# =========================================================

def related_posts(posts, current_slug):

    related = [
        p for p in posts
        if p["slug"] != current_slug
    ][:6]

    items = ""

    for p in related:
        items += (
            f"<li>"
            f"<a href='/hellobar/blog/{p['slug']}.html'>"
            f"{p['title']}"
            f"</a>"
            f"</li>"
        )

    return f"""
    <div class="card">
    <h3>Related Hello Bar Guides</h3>
    <ul>{items}</ul>
    </div>
    """


# =========================================================
# ARTICLE BUILDER
# =========================================================

def build_article(post, posts):

    feature_list = "".join([
        f"<li>{feature}</li>"
        for feature in FEATURES
    ])

    related = related_posts(posts, post["slug"])

    content = f"""

<section class="hero">

<h1>{post['title']}</h1>

<p>
Learn how businesses use Hello Bar
<strong>{post['popup']}</strong>
campaigns to increase conversions in 2026.
</p>

<a class="button"
href="{CONFIG['AFFILIATE_URL']}"
target="_blank"
rel="nofollow sponsored">

Start Hello Bar FREE

</a>

</section>

<div class="meta">
Updated {datetime.utcnow().strftime('%B %d, %Y')}
</div>

<div class="card">

<h2>
Why Hello Bar Works for {post['niche']}
</h2>

<p>
Hello Bar helps websites deploy
high-converting popups, bars,
slide-ins and lead generation campaigns
without slowing down the site.
</p>

<p>
For businesses in
<strong>{post['niche']}</strong>,
this means more leads,
higher email opt-ins and
better affiliate conversion rates.
</p>

</div>

<div class="card">

<h2>Top Hello Bar Features</h2>

<ul>
{feature_list}
</ul>

</div>

<div class="card">

<h2>Hello Bar Pricing 2026</h2>

<table>

<tr>
<th>Plan</th>
<th>Monthly</th>
<th>Views</th>
</tr>

<tr>
<td>Starter</td>
<td>FREE</td>
<td>5,000</td>
</tr>

<tr>
<td>Growth</td>
<td>$39</td>
<td>50,000</td>
</tr>

<tr>
<td>Premium</td>
<td>$69</td>
<td>150,000</td>
</tr>

<tr>
<td>Elite</td>
<td>$129</td>
<td>500,000</td>
</tr>

</table>

</div>

<div class="cta">

<h2>
Boost Conversions with Hello Bar
</h2>

<p>
Launch exit intent campaigns,
slide-ins and lead generation systems
today.
</p>

<a class="button"
href="{CONFIG['AFFILIATE_URL']}"
target="_blank"
rel="nofollow sponsored">

Deploy Hello Bar FREE

</a>

</div>

{related}

"""

    return page_template(
        title=post["title"],
        description=post["description"],
        content=content,
        canonical=f"{CONFIG['BASE_URL']}/blog/{post['slug']}.html",
        extra_head=article_schema(post),
    )


# =========================================================
# HOMEPAGE
# =========================================================

def build_homepage(posts):

    cards = ""

    for p in posts[:24]:

        cards += f"""
        <div class="card">

        <h3>
        <a href="/hellobar/blog/{p['slug']}.html">
        {p['title']}
        </a>
        </h3>

        <p>{p['description']}</p>

        </div>
        """

    content = f"""

<section class="hero">

<h1>
Hello Bar Review 2026:
Popup Software + CRO Engine
</h1>

<p>
The ultimate authority site for
Hello Bar popups, conversion optimization,
lead generation and affiliate marketing.
</p>

<a class="button"
href="{CONFIG['AFFILIATE_URL']}"
target="_blank"
rel="nofollow sponsored">

Start FREE Hello Bar

</a>

</section>

<div class="grid">
{cards}
</div>

"""

    homepage = page_template(
        title="Hello Bar Review 2026",
        description=CONFIG["DESCRIPTION"],
        content=content,
        canonical=f"{CONFIG['BASE_URL']}/",
    )

    save_file(
        f"{CONFIG['OUTPUT_DIR']}/index.html",
        homepage
    )


# =========================================================
# SITEMAP
# =========================================================

def build_sitemap(urls):

    root = Element(
        "urlset",
        xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    )

    for url in urls:

        u = SubElement(root, "url")

        loc = SubElement(u, "loc")
        loc.text = url

        lastmod = SubElement(u, "lastmod")
        lastmod.text = datetime.utcnow().strftime("%Y-%m-%d")

    xml = minidom.parseString(
        tostring(root)
    ).toprettyxml(indent="  ")

    save_file(
        f"{CONFIG['OUTPUT_DIR']}/sitemap.xml",
        xml
    )


# =========================================================
# ROBOTS
# =========================================================

def build_robots():

    robots = f"""
User-agent: *
Allow: /

Sitemap: {CONFIG['BASE_URL']}/sitemap.xml
"""

    save_file(
        f"{CONFIG['OUTPUT_DIR']}/robots.txt",
        robots.strip()
    )


# =========================================================
# LLMS.TXT
# =========================================================

def build_llms(posts):

    content = "# HelloBar Authority Engine\n\n"

    content += "## AI Search Optimized Content\n\n"

    for p in posts:
        content += (
            f"- {p['title']} | "
            f"{CONFIG['BASE_URL']}/blog/{p['slug']}.html\n"
        )

    save_file(
        f"{CONFIG['OUTPUT_DIR']}/llms.txt",
        content
    )


# =========================================================
# 404
# =========================================================

def build_404():

    content = """

<section class="hero">

<h1>404</h1>

<p>
This page could not be found.
</p>

<a class="button" href="/hellobar/">
Return Home
</a>

</section>

"""

    page = page_template(
        title="404",
        description="Page not found",
        content=content,
        canonical="",
    )

    save_file(
        f"{CONFIG['OUTPUT_DIR']}/404.html",
        page
    )


# =========================================================
# MAIN BUILD
# =========================================================

def build():

    print("=" * 60)
    print("HELLOBAR AUTHORITY ENGINE STARTING")
    print("=" * 60)

    ensure_dir(CONFIG["OUTPUT_DIR"])
    ensure_dir(f"{CONFIG['OUTPUT_DIR']}/blog")

    posts = generate_posts()

    urls = [
        CONFIG["BASE_URL"] + "/"
    ]

    # Homepage
    build_homepage(posts)

    # Articles
    for post in posts:

        article = build_article(post, posts)

        path = (
            f"{CONFIG['OUTPUT_DIR']}/blog/"
            f"{post['slug']}.html"
        )

        save_file(path, article)

        urls.append(
            f"{CONFIG['BASE_URL']}/blog/"
            f"{post['slug']}.html"
        )

    # SEO Infrastructure
    build_sitemap(urls)
    build_robots()
    build_llms(posts)
    build_404()

    print(f"Generated Pages: {len(posts)}")
    print(f"Sitemap URLs: {len(urls)}")
    print(f"Affiliate ID: {CONFIG['AFFILIATE_ID']}")
    print("Deploy Complete")
    print("=" * 60)


if __name__ == "__main__":
    build()
