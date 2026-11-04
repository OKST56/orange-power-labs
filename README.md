# Orange Power Labs

Website-only source for the public repository `OKST56/orange-power-labs`.
No game source code, executables, extracted assets, or game downloads belong here.
Included raster images are the supplied studio logo, the supplied David Ortiz MLB The Show 16 reference image credited to GameSpot, and the supplied native title-screen development capture. Field graphics are decorative CSS, not gameplay captures.

## Preview

Run `python build.py`, then `python -m http.server 8080 --directory site`.
Open http://localhost:8080. The built HTML also works directly from disk.

## Content

`content/recovered-dev-logs.txt` preserves the retrieved source conversation text.
Entries 001–004 were recovered in full. Entry 005 was truncated by retrieval and is visibly labeled a draft excerpt. Obtain the original ending before treating it as a complete published log.
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
