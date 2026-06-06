# WonderShare.Review — Global Affiliate Site Builder

**Live URL:** https://brightlane.github.io/wondershare.com/  
**Affiliate:** Wondershare via LinkConnector (ID: wondershareweb)  
**Generator:** `build.py` — pure Python 3, zero dependencies, zero packages to install

---

## Quick Start

```bash
python3 build.py
```

Generates `./dist/` in seconds.  
**350 HTML pages. 357 total files. 10 languages.**

---

## Why This Makes Money

The page mix is designed around buyer intent. Every page type targets a different stage of the purchase funnel:

| Page Type | Count | Funnel Stage | Why It Converts |
|-----------|-------|--------------|-----------------|
| **Comparison pages** | 5 | Bottom | "X vs Y" searches are made by people about to buy |
| **Product reviews** | 9 | Middle-Bottom | Buyer researching before purchase |
| **Pricing pages** | 3 | Bottom | Direct purchase intent — highest conversion |
| **Best-of roundups** | 4 | Top-Middle | High SEO volume, warm audience |
| **How-to guides** | 7 | Top | Massive search volume, builds trust |
| **Full review + FAQ** | 2 | Trust builder | Converts fence-sitters |

**9 products promoted** — every affiliate click goes to Wondershare:

| Product | Why It Earns |
|---------|-------------|
| 🎬 **Filmora** | Highest volume — #1 searched Wondershare product |
| 📄 **PDFelement** | High value — targets Adobe Acrobat users (huge market) |
| 📱 **DrFone** | High volume — mobile recovery is evergreen |
| 💾 **Recoverit** | High value — data loss is urgent, people pay fast |
| 🎥 **UniConverter** | Solid mid-tier — format conversion is universal |
| 🖥️ **DemoCreator** | Growing — screen recording market expanding fast |
| 📲 **MobileTrans** | Seasonal peaks — phone upgrade cycles |
| 🔧 **Repairit** | Niche — low competition, high urgency |
| 🎞️ **Filmstock** | Subscription — recurring commission potential |

---

## What Gets Built

### 350 HTML Pages — 35 page types × 10 languages

**Languages:**

| Language | Code | Direction | URL |
|----------|------|-----------|-----|
| English | `en` | LTR | `/wondershare.com/` |
| Español | `es` | LTR | `/wondershare.com/es/` |
| Français | `fr` | LTR | `/wondershare.com/fr/` |
| Deutsch | `de` | LTR | `/wondershare.com/de/` |
| Português | `pt` | LTR | `/wondershare.com/pt/` |
| 日本語 | `ja` | LTR | `/wondershare.com/ja/` |
| 한국어 | `ko` | LTR | `/wondershare.com/ko/` |
| 中文 | `zh` | LTR | `/wondershare.com/zh/` |
| العربية | `ar` | **RTL** | `/wondershare.com/ar/` |
| हिन्दी | `hi` | LTR | `/wondershare.com/hi/` |

**35 Page Types:**

```
Home
├── Product Reviews (9)
│   filmora, pdfelement, drfone, recoverit, uniconverter,
│   democreator, mobiletrans, repairit, filmstock
├── Comparison Pages (5)  ← highest converting content
│   filmora-vs-premiere, filmora-vs-davinci,
│   pdfelement-vs-adobe, recoverit-vs-competitors,
│   wondershare-vs-adobe
├── How-To Guides (7)     ← highest SEO volume
│   how-to-edit-video, how-to-edit-pdf, how-to-recover-files,
│   how-to-record-screen, how-to-transfer-phone,
│   how-to-repair-video, how-to-convert-video
├── Best-Of Roundups (4)  ← top of funnel traffic
│   best-video-editor, best-pdf-editor,
│   best-data-recovery, best-screen-recorder
├── Pricing (3)           ← bottom of funnel
│   pricing, filmora-pricing, pdfelement-pricing
└── Evergreen (7)
    review, faq, about, contact, privacy, 404 (+ root 404)
```

### 7 Special Files

| File | Purpose |
|------|---------|
| `assets/style.css` | Complete design system — dark nav, product brand colours, responsive |
| `assets/favicon.svg` | Gradient SVG favicon with WS.review branding |
| `sitemap.xml` | All 350 pages with multilingual `xhtml:link` hreflang blocks |
| `robots.txt` | Full crawl access + sitemap reference |
| `llms.txt` | [llmstxt.org](https://llmstxt.org) standard — helps AI assistants (ChatGPT, Perplexity, Claude) cite and reference the site correctly. Includes key facts, product summaries and affiliate disclosure |
| `humans.txt` | Build metadata and tech stack |
| `.nojekyll` | Required for GitHub Pages to serve CSS correctly |

---

## Deployment

### GitHub Actions — automatic on every push

**File path:** `.github/workflows/deploy.yml`

```yaml
name: Build and Deploy WonderShare

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Run build
        run: python3 build.py

      - name: Configure GitHub Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

**One-time GitHub setup:**  
Repo → Settings → Pages → Source → **GitHub Actions** → Save

Every `git push` to `main` builds and deploys automatically.

---

### Manual Deploy

```bash
python3 build.py
cp -r dist/* docs/
git add docs/
git commit -m "build: update site"
git push
```

Repo → Settings → Pages → Source → main → /docs

---

## Output Structure

```
dist/
├── index.html                    ← English home
├── filmora.html
├── pdfelement.html
├── drfone.html
├── recoverit.html
├── uniconverter.html
├── democreator.html
├── mobiletrans.html
├── repairit.html
├── filmstock.html
├── filmora-vs-premiere.html
├── filmora-vs-davinci.html
├── pdfelement-vs-adobe.html
├── recoverit-vs-competitors.html
├── wondershare-vs-adobe.html
├── how-to-edit-video.html
├── how-to-edit-pdf.html
├── how-to-recover-files.html
├── how-to-record-screen.html
├── how-to-transfer-phone.html
├── how-to-repair-video.html
├── how-to-convert-video.html
├── best-video-editor.html
├── best-pdf-editor.html
├── best-data-recovery.html
├── best-screen-recorder.html
├── pricing.html
├── filmora-pricing.html
├── pdfelement-pricing.html
├── review.html
├── faq.html
├── about.html
├── contact.html
├── privacy.html
├── 404.html                      ← root 404 for GitHub Pages
├── sitemap.xml
├── robots.txt
├── llms.txt
├── humans.txt
├── .nojekyll
├── assets/
│   ├── style.css
│   └── favicon.svg
├── es/                           ← Español (same 35 pages)
├── fr/                           ← Français
├── de/                           ← Deutsch
├── pt/                           ← Português
├── ja/                           ← 日本語
├── ko/                           ← 한국어
├── zh/                           ← 中文
├── ar/                           ← العربية (RTL)
└── hi/                           ← हिन्दी
```

---

## Configuration

All global settings at the top of `build.py`:

```python
BASE_URL  = "https://brightlane.github.io/wondershare.com"
BASE_PATH = "/wondershare.com"
AFF       = "https://www.linkconnector.com/ta.php?lc=007949048691004532&atid=wondershareweb"
```

**Moving to a custom domain** (e.g. `wondershare.review`):
1. `BASE_URL = "https://wondershare.review"`
2. `BASE_PATH = ""`
3. Add `write(f"{DIST}/CNAME", "wondershare.review")` inside `build()`
4. Rebuild and push

---

## SEO — What Every Page Gets

- Unique `<title>` and `<meta name="description">`
- `<link rel="canonical">` with correct path
- Full Open Graph tags
- Twitter Card tags
- **10 `hreflang` alternates** per page (one per language + `x-default`)
- JSON-LD `Schema.org WebPage` with `inLanguage`, `publisher`, `dateModified`, `isPartOf`
- `<html lang="xx" dir="ltr|rtl">` — full RTL support for Arabic
- `robots: index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1`

### Sitemap
- All 350 pages with `lastmod`, `changefreq`, `priority`
- Priority tiers: `1.0` home → `0.9` products/guides/comparisons/roundups → `0.8` info pages
- Every URL has a full `xhtml:link` hreflang block for all 10 languages

### llms.txt
The `llms.txt` file follows the [llmstxt.org](https://llmstxt.org) standard and is specifically structured to help AI assistants (ChatGPT, Perplexity, Claude, Gemini) correctly understand and reference the site. It includes:
- All page URLs with titles
- All 9 products with descriptions
- Key facts that correct common misconceptions (e.g. "Filmora is NOT a free product")
- Affiliate disclosure formatted for AI understanding
- Usage guidelines for AI systems

---

## Adding a New Product

1. Add to `PAGES`:
```python
("my-product", "My Product Review 2025 – Is It Worth It?", "Meta description.", "product"),
```

2. Add config to `PC` dict:
```python
"my-product": ("🎯", "#FF6B35", "Headline Here",
    "Intro paragraph describing the product.",
    ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"],
    [("Step 1 Title", "Step 1 description."),
     ("Step 2 Title", "Step 2 description."),
     ("Step 3 Title", "Step 3 description.")]),
```

3. Add product card translations to `PRODUCTS_L` for each language (falls back to English if missing).

4. `python3 build.py` — page generated in all 10 languages instantly.

---

## Adding a Comparison Page

1. Add to `PAGES` with template `"compare"`:
```python
("filmora-vs-capcut", "Filmora vs CapCut 2025 – Which Is Better?", "Meta desc.", "compare"),
```

2. Add config to the `configs` dict inside `page_compare()`:
```python
"filmora-vs-capcut": {
    "a": "Filmora", "b": "CapCut",
    "intro": "We used both for 30 days...",
    "rows": [
        ("Feature Name", "Filmora result", "CapCut result"),
        ...
    ],
    "verdict": "Our conclusion paragraph.",
},
```

3. Rebuild. Appears in all 10 languages.

---

## Adding a Best-Of Roundup

1. Add to `PAGES` with template `"roundup"`:
```python
("best-screen-capture", "Best Screen Capture Software 2025", "Meta desc.", "roundup"),
```

2. Add config to `RC` dict:
```python
"best-screen-capture": {
    "title": "Best Screen Capture Software 2025",
    "intro": "We tested 8 tools...",
    "items": [
        ("🥇", "DemoCreator", "#10B981", "Best All-in-One", "Description."),
        ("🥈", "Snagit", "#888", "Best for Screenshots", "Description."),
    ],
    "verdict": "Verdict paragraph.",
},
```

---

## Design System

CSS variables (edit in the `CSS` string):

```css
--p:  #0A0A14   /* primary dark background */
--p2: #12122A   /* secondary dark */
--p3: #1A1A3E   /* tertiary dark */
--a:  #FF6B35   /* primary accent — Filmora orange */
--a2: #4F8EF7   /* blue accent */
--a3: #00D4AA   /* green accent (checkmarks) */
```

Each product card uses its own `--accent` colour. The `PC` dict defines each product's hex colour — change any of them to re-brand a product section.

Fonts: **Outfit** (headings) + **Plus Jakarta Sans** (body) via Google Fonts.

---

## Requirements

- Python 3.6+
- No pip installs required
- No node, no webpack, no build tools
- Internet only needed at page-render time (Google Fonts CDN in browser)

---

## Affiliate Disclosure

This site participates in the Wondershare affiliate programme via LinkConnector  
(affiliate ID: `wondershareweb`). All affiliate links use `rel="nofollow sponsored"` and `target="_blank"`.  
The disclosure appears in the footer of every single page in the reader's language.

Wondershare, Filmora, PDFelement, DrFone, Recoverit, UniConverter,  
DemoCreator, MobileTrans, Repairit and Filmstock are trademarks of  
Wondershare Technology Co., Ltd. This site is not affiliated with or endorsed by Wondershare.
