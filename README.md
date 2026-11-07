# Orange Power Labs

Website-only source for the public repository `OKST56/orange-power-labs`.
No game source code, executables, extracted assets, or game downloads belong here.
Included raster images are the supplied studio logo, the supplied David Ortiz MLB The Show 16 reference image credited to GameSpot, and the supplied native title-screen development capture. Field graphics are decorative CSS, not gameplay captures.

## Preview

Run `python build.py`, then `python -m http.server 8080 --directory site`.
Open http://localhost:8080. The built HTML also works directly from disk.

## Content

The three project journals have independent numbering. Existing CBL article URLs remain `dev-log-001.html` through `dev-log-006.html`; do not rename published files. Journal indexes are `college-baseball-legacy-dev-logs.html`, `missouri-high-school-football-dev-logs.html`, and `ncaa-football-07-dev-logs.html`.

Project metadata is in `content/projects.json`; added landing pages and journal gateways are generated in `expansion.py`. The NCAA Football 07 writing plan is not a publication manifest and produces no article pages. There are no published football articles yet.

To add an article, provide its project, independent number, final title, date, text, and optional image. Save the text under a project-specific content path and generate a project-specific output such as `ncaa-football-07-dev-log-001.html` or `missouri-high-school-football-dev-log-001.html`. Use the existing `page()` and `markdown()` helpers for the consistent article layout, identify the project in the heading, and add links to its own journal and adjacent entries. Update that project’s index and metadata only after the article is finalized. Rebuild, verify links, then push to deploy. Proposed articles must never be listed as published entries.

`content/recovered-dev-logs.txt` preserves the retrieved source conversation text.
Entries 001–004 use the recovered source text. Entry 005 uses the complete owner-supplied text in `content/dev-log-005.md`.
Edit page copy and metadata in `build.py`, styles in `site/assets/style.css`, and navigation behavior in `site/assets/app.js`. Rebuild after editing content.

Discord currently uses the supplied temporary invite `https://discord.gg/mByxc7QGq`. Replace it in `build.py` and rebuild when it expires; preferably use a permanent invite when available. No exact expiry date has been assumed.

## Deployment

GitHub Pages publishes this website from the included workflow. To reproduce the setup:

1. Create a separate public repository named `orange-power-labs` under `OKST56`.
2. Upload or push only the contents of this directory, never its parent workspace.
3. In repository Settings → Pages, select **GitHub Actions** as the publishing source.
4. Run the Pages workflow, or push to `main` to trigger it.
5. Verify the deployment at https://okst56.github.io/orange-power-labs/ and check navigation on mobile.

The workflow uploads only `site/`. Relative links support the repository subpath.
No custom domain or CNAME is configured. A custom domain can be added later after registration and DNS verification.

External fonts load from Google Fonts with system font fallbacks. There are no analytics, forms, cookies, or third-party scripts.
