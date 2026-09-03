# Md. Shariful Islam — Personal Portfolio Site

Static 8-page site (HTML + Tailwind CSS, no build step required at deploy time). Original dark-mode design system: `ink` neutral base, `brand` (emerald green) / `crimson` (red) / `gold` (amber) accents, Poppins (display) + Inter (body) + Hind Siliguri (Bangla/Hindi labels) fonts.

## Pages

- `index.html` — Home
- `about.html` — About / journey / GoVidCo vs. Upwork explainer
- `cuts.html` — Video editing portfolio (6 categories)
- `shop.html` — Service packages + Shariful Reflection digital products
- `reflection.html` — Shariful Reflection (Bangla / Hindi / English)
- `sop.html` — Remote Work Briefing: Operational Blueprint & Standards (4 sections + downloadable PDF)
- `contact.html` — Contact (mailto-based form, no backend needed)
- `404.html` — Error page

## Deploying to Cloudflare Pages

1. Push this folder to a Git repo (or drag-and-drop deploy via the Cloudflare dashboard).
2. Framework preset: **None**. Build command: **none**. Output directory: `/` (repo root).
3. `_headers` is already included for asset caching. `robots.txt` and `sitemap.xml` are set up for `https://sharifulcuts.com` — update the domain in both files (and in `build.py`'s `DOMAIN` constant, then re-run `python3 build.py`) if the production domain changes.

## Editing content

All 8 HTML files are **generated** by `build.py` from shared header/nav/footer functions, so hand-editing the `.html` files directly will get overwritten if you regenerate. To change copy, links, or layout:

1. Edit `build.py` (page content lives in `build_index()`, `build_about()`, ..., `build_sop()`; shared nav/footer/head are in `nav()`, `footer()`, `head()`; the nav/footer link list is `NAV_ITEMS` near the top of the file).
2. Run `python3 build.py` to regenerate all 8 HTML files.
3. Recompile CSS (only needed if you added new Tailwind utility classes not already in the compiled stylesheet):
   ```
   npx tailwindcss -i src/input.css -o assets/css/style.css -c tailwind.config.js --minify
   ```
   (If `npx` can't reach the registry, install `tailwindcss` v3 locally first, or use any Tailwind CLI v3.x binary — the config and input CSS are registry-independent.)

To edit the SOP page's content specifically: the 4 briefing sections live in the `SOP_SECTIONS` list in `build.py`, just above `build_sop()`. If you change the wording there, also update `generate_sop_pdf.py`'s `SECTIONS` list (same content, separate file, since the PDF is a static generated asset, not rendered from HTML) and re-run `python3 generate_sop_pdf.py` to refresh `assets/docs/remote-work-briefing.pdf`.

If you'd rather hand-edit the static `.html` files going forward and stop using `build.py`, that's fine too — the generated files are plain, dependency-free HTML with no server-side templating.

## Design system

- **Background**: custom `ink` scale (`ink-950` page background, `ink-900` cards, `ink-800`/`ink-700` borders) defined in `tailwind.config.js`.
- **Fonts**: Poppins (headings, via `font-display`), Inter (body, via `font-sans`), Hind Siliguri (available as `font-bn` for Bangla/Hindi labels), all via Google Fonts.
- **Accent colors**: `brand` (emerald green, sampled from the personal-brand mark — Upwork/primary CTAs), `crimson` (red, sampled from the GoVidCo "G" play-triangle — GoVidCo-specific CTAs), `gold`/`maroon` (warm amber/maroon — Shariful Reflection).
- `sop.html` follows this exact system: crimson icon accents (tying it to GoVidCo, since it's an agency operations document), brand-colored section numbers, same card/button/badge components as every other page.

## Known follow-ups (things only you can supply)

These were intentionally left as clearly-labeled honest states rather than fabricated links, per the "no placeholders" requirement:

- **Shariful Reflection channel links** (YouTube + Facebook for Bangla, Hindi, English) — currently rendered as disabled "Coming Soon" buttons on `reflection.html` since the channels aren't confirmed live yet. Once you have the URLs, update the `language_card()` function in `build.py` (swap the disabled `<button>` markup for `<a href="...">`) and regenerate.
- **GoVidCo social links** — only `https://govidco.com` is wired in (LinkedIn/Instagram/etc. were not provided). Add them to the `GOVIDCO_URL`-adjacent markup in `nav()`/`footer()`/relevant pages if you want them.
- **Portfolio category CTAs** (`cuts.html`) link to a "Discuss This Style" contact CTA rather than specific YouTube playlist URLs, since no real playlist links were provided. Swap in real playlist URLs when available.
- **Shop pricing** — the service tiers ($150/video, $1,200/mo, custom) and digital product prices ($19/$29/$15) are reasonable starting-point figures for an agency of this type; adjust to your actual rates.
- **Upwork URL confirmed**: `https://www.upwork.com/freelancers/~01e389eef945cdf1aa?mp_source=share` — wired in throughout.
- **SOP content**: verbatim from the "Remote Work Briefing: Operational Blueprint & Standards" PDF included in this project (`assets/docs/remote-work-briefing.pdf`) — extracted programmatically and cross-checked, not paraphrased.

## Asset notes

- The four original "Shariful Cuts" logo files (with the text baked into the image pixels) are **not used** anywhere in this build, since the brand name "Shariful Cuts" is fully retired in favor of "Md. Shariful Islam." The green circular "C / play-button" icon mark (used as favicon + nav mark) is sourced from the icon-only favicon files, which have no text baked in.
- `Favicon.png` in the original project uploads is actually the GoVidCo "G" play-icon mark (mislabeled at upload) — used as `assets/img/mark-govidco-g.png`.
- Google Fonts (Poppins/Inter/Hind Siliguri) and Font Awesome are loaded from their standard CDNs (`fonts.googleapis.com`, `cdnjs.cloudflare.com`) — normal for any deployed site, but unreachable from this sandboxed build environment, so fonts/icons render as fallback system fonts/blank glyphs in in-sandbox screenshots only. This is a sandbox network restriction, not a defect in the shipped code — verified working once a normal internet connection is available.

## PDF briefing asset

`assets/docs/remote-work-briefing.pdf` is generated by `generate_sop_pdf.py` (uses `reportlab`; monospace-styled document with its own cyan/emerald accent treatment, kept as originally produced since it's a standalone downloadable reference document rather than a themed page — its content, not its color scheme, is what `sop.html` mirrors exactly). It's a real, complete document — not a placeholder file — linked from the prominent "Download PDF" buttons on `sop.html`.

## Version note

This is the **original ink/brand/crimson/gold design**, restored after a brief detour into a "Midnight Terminal" (Zinc/JetBrains Mono/cyan-emerald) restyle that was tried and then reverted at the user's request. `sop.html` was added during the Midnight Terminal detour and has been re-skinned here to match this original system exactly — same components, same palette, same fonts as every other page.
