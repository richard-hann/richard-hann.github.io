# scripts/

Utility scripts for the Academic Pages template.

## `make-og-image.py`

Generates the default Open Graph / social preview image at
`images/og-image.png` (1200x630 PNG) used by `_includes/seo.html` when a page
does not define its own header image.

```
python3 scripts/make-og-image.py
```

Requirements:

- Python 3 with [Pillow](https://python-pillow.org) (`pip install Pillow`)
- A TrueType font; defaults to DejaVu Sans (`/usr/share/fonts/truetype/dejavu`),
  override with the `FONT_DIR` environment variable
- The site favicon at `images/favicon-512x512.png` (already in the template);
  it is composited as the card logo

The output is byte-reproducible for a given Pillow/font version and is committed
to the repo, so the build itself does not need Pillow.

## `push_uavicinglab.py`

Copies the publication list from folk.ntnu.no to the **Papers** part of
https://uavicinglab.com/publications/ (WordPress.com, site 189910960, page 45).
Runs at the end of the nightly "Sync from folk.ntnu.no" Action.

- Source: `markdown_generator/folk_snapshot.json` plus
  `markdown_generator/uavicinglab_extra_pubs.json` (lab papers without Hann).
- Left out: entries with Hermanson, theses. The Theses section on the lab page stays hand-edited.
- Replaces only what sits between the "Papers" heading and the separator line above "Theses";
  stops if those are missing or the list would shrink by more than 30 %.
- Needs the repo secrets `WPCOM_CLIENT_ID`, `WPCOM_CLIENT_SECRET` (an app from
  https://developer.wordpress.com/apps/), `WPCOM_USERNAME`, `WPCOM_PASSWORD`
  (with two-step login: an application password). Without them the step is skipped.

```
python3 scripts/push_uavicinglab.py --preview /tmp/lab.html   # no login
python3 scripts/push_uavicinglab.py --dry-run                 # login, show counts, save nothing
```
