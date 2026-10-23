# -*- coding: utf-8 -*-
"""Write the publication list from folk.ntnu.no into the UAV Icing Lab Publications page.

  python3 scripts/push_uavicinglab.py                 # update https://uavicinglab.com/publications/
  python3 scripts/push_uavicinglab.py --dry-run       # only show what would change
  python3 scripts/push_uavicinglab.py --preview x.html  # write the generated list to a file, no login needed

Source: markdown_generator/folk_snapshot.json (written by build_from_folk.py)
      + markdown_generator/uavicinglab_extra_pubs.json (lab papers without Hann, not on folk)
Left out: every entry with Hermanson as author, and theses.

Only the "Papers" part of the page is replaced: everything between the "Papers" heading
and the horizontal line above "Theses". The banner, the headings and the Theses section
stay as edited in WordPress. WordPress keeps a revision of every update (Page -> Revisions).

Login (WordPress.com REST API, the site is a hosted WordPress.com site), from environment:
  WPCOM_CLIENT_ID, WPCOM_CLIENT_SECRET   app from https://developer.wordpress.com/apps/
  WPCOM_USERNAME, WPCOM_PASSWORD         WordPress.com user; with two-step login an application password
or WPCOM_TOKEN (an OAuth2 token with access to the site).
"""
import os, re, sys, json, html, urllib.request, urllib.parse, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SNAP = os.path.join(ROOT, "markdown_generator", "folk_snapshot.json")
EXTRA = os.path.join(ROOT, "markdown_generator", "uavicinglab_extra_pubs.json")

SITE_ID = "189910960"           # uavicinglab.com
PAGE_ID = 45                    # /publications/
API = f"https://public-api.wordpress.com/wp/v2/sites/{SITE_ID}/pages/{PAGE_ID}"
EXCLUDE = re.compile(r"Herm[ae]ns[oe]n", re.I)
MAX_SHRINK = 0.30               # refuse if the list would lose more than 30 % of its entries

# ---------------------------------------------------------------- list
def load_items():
    with open(SNAP, encoding="utf-8") as f:
        folk = json.load(f)["sections"]["Publications"]["items"]
    with open(EXTRA, encoding="utf-8") as f:
        extra = json.load(f)["items"]
    items = [i for i in folk if i.get("entry", True)] + extra
    keep, seen = [], set()
    for i in items:
        t = i["t"]
        if EXCLUDE.search(t) or re.search(r"\bthesis\b", t, re.I):
            continue
        key = re.sub(r"\W+", "", t.lower())
        if key in seen:
            continue
        seen.add(key)
        keep.append(i)
    return keep

def fix_url(u):
    if re.match(r"^[\w.-]+\.(no|com|org|edu|net|de|eu)/", u):
        return "https://" + u
    m = re.match(r"^https?://richahan\.folk\.ntnu\.no/((?:[\w-]+\.)+(?:no|com|org|edu|net|de|eu)/.*)$", u)
    return "https://" + m.group(1) if m else u

def fmt(text, links=()):
    """Plain text -> HTML: link the linked words and the DOI."""
    s = html.escape(text, quote=False)
    holders = []
    for (lt, href) in sorted([l for l in links if l[0] and l[1]], key=lambda l: -len(l[0])):
        e = html.escape(lt, quote=False)
        if e in s:
            holders.append(f'<a href="{html.escape(fix_url(href))}">{e}</a>')
            s = s.replace(e, f"\x00{len(holders) - 1}\x00", 1)
    s = re.sub(r"(?<![/\w])(doi\.org/[^\s<\x00]+?)(\.?)(\s|$)",
               lambda m: f'<a href="https://{m.group(1)}">{m.group(1)}</a>{m.group(2)}{m.group(3)}', s)
    return re.sub("\x00(\\d+)\x00", lambda m: holders[int(m.group(1))], s)

def year_key(y):
    m = re.match(r"\d{4}", y or "")
    return int(m.group()) if m else 0

def blocks(items):
    """Gutenberg markup in the page's existing layout: one row per year (10 % year | 90 % list)."""
    years = sorted({i["y"] for i in items}, key=year_key, reverse=True)
    out = []
    for y in years:
        lis = "\n\n".join(
            f"<!-- wp:list-item -->\n<li>{fmt(i['t'], i.get('links', []))}</li>\n<!-- /wp:list-item -->"
            for i in items if i["y"] == y)
        out.append(
            '<!-- wp:columns -->\n<div class="wp-block-columns">'
            '<!-- wp:column {"width":"10%"} -->\n<div class="wp-block-column" style="flex-basis:10%">'
            '<!-- wp:paragraph {"style":{"typography":{"fontSize":"24px"}}} -->\n'
            f'<p style="font-size:24px">{html.escape(y)}</p>\n<!-- /wp:paragraph --></div>\n<!-- /wp:column -->\n\n'
            '<!-- wp:column {"width":"90%"} -->\n<div class="wp-block-column" style="flex-basis:90%">'
            f'<!-- wp:list -->\n<ul class="wp-block-list">{lis}</ul>\n<!-- /wp:list --></div>\n<!-- /wp:column --></div>\n'
            '<!-- /wp:columns -->')
    return "\n\n" + "\n\n".join(out) + "\n\n"

# ---------------------------------------------------------------- page
PAPERS = re.compile(r"(<!-- wp:heading\b[^>]*-->\s*<h\d[^>]*>\s*Papers\s*</h\d>\s*<!-- /wp:heading -->)(.*?)(<!-- wp:separator\b)", re.S)

def split_page(raw):
    found = PAPERS.findall(raw)
    if len(found) != 1:
        sys.exit("Could not find exactly one 'Papers' heading followed by a separator line on the page - nothing changed.")
    m = PAPERS.search(raw)
    return raw[:m.end(1)], m.group(2), raw[m.start(3):]

def token():
    if os.environ.get("WPCOM_TOKEN"):
        return os.environ["WPCOM_TOKEN"]
    need = ["WPCOM_CLIENT_ID", "WPCOM_CLIENT_SECRET", "WPCOM_USERNAME", "WPCOM_PASSWORD"]
    missing = [k for k in need if not os.environ.get(k)]
    if missing:
        print("UAV Icing Lab page not updated: missing secrets " + ", ".join(missing))
        sys.exit(0)
    body = urllib.parse.urlencode({
        "client_id": os.environ["WPCOM_CLIENT_ID"], "client_secret": os.environ["WPCOM_CLIENT_SECRET"],
        "grant_type": "password", "username": os.environ["WPCOM_USERNAME"],
        "password": os.environ["WPCOM_PASSWORD"]}).encode()
    return call("https://public-api.wordpress.com/oauth2/token", data=body)["access_token"]

def call(url, data=None, tok=None, json_body=None):
    headers = {"User-Agent": "folk-sync (richard-hann.github.io)"}
    if tok:
        headers["Authorization"] = "Bearer " + tok
    if json_body is not None:
        data = json.dumps(json_body).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"WordPress.com answered {e.code} for {url.split('?')[0]}: {e.read().decode(errors='replace')[:500]}")

# ---------------------------------------------------------------- main
def main():
    args = sys.argv[1:]
    items = load_items()
    new = blocks(items)
    if "--preview" in args:
        path = args[args.index("--preview") + 1]
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        print(f"{len(items)} entries written to {path}")
        return

    tok = token()
    page = call(API + "?context=edit", tok=tok)
    before, old, after = split_page(page["content"]["raw"])
    n_old, n_new = old.count("<li"), new.count("<li")
    print(f"Lab page: {n_old} entries now, {n_new} after the update.")
    if old.strip() == new.strip():
        print("Already up to date.")
        return
    if n_old and n_new < n_old * (1 - MAX_SHRINK):
        sys.exit(f"The list would shrink by more than {int(MAX_SHRINK * 100)} % - nothing changed.")
    if "--dry-run" in args:
        print("Dry run - not saved.")
        return
    call(API, tok=tok, json_body={"content": before + new + after})
    print("Updated https://uavicinglab.com/publications/")

if __name__ == "__main__":
    main()
