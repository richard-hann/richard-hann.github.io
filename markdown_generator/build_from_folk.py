# -*- coding: utf-8 -*-
"""Build the website content from the folk.ntnu.no snapshot.

  node scripts/folk_extract.mjs > /tmp/new.json      # read the NTNU page (sections = Word bookmarks)
  python3 markdown_generator/build_from_folk.py /tmp/new.json

Without an argument the stored snapshot (markdown_generator/folk_snapshot.json) is rebuilt.
A new snapshot is only accepted if all required sections are present and no section
shrank by more than 30 % - otherwise nothing is changed and the script exits with an error.

Writes: _publications/*.md, _talks/*.md, _data/folk.yml
"""
import os, re, sys, json, html, shutil, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SNAP = os.path.join(HERE, "folk_snapshot.json")
REQUIRED = ["Publications", "Presentations", "Datasets", "People", "Teaching", "Funding", "Research_projects"]

# Entries that are not part of a bookmarked section on the NTNU page
EXTRA_PUBS = [
    {"y": "2020", "cat": "theses", "links": [],
     "t": "Hann, R. (2020). Atmospheric Ice Accretions, Aerodynamic Icing Penalties, and Ice Protection Systems on Unmanned Aerial Vehicles. PhD Thesis NTNU 2020:200, Norwegian University of Science and Technology.",
     "title": "Atmospheric Ice Accretions, Aerodynamic Icing Penalties, and Ice Protection Systems on Unmanned Aerial Vehicles"},
]

# ---------------------------------------------------------------- helpers
def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()[:60].rstrip("-")

def yq(s):
    return "'" + s.replace("'", "''") + "'"

def fix_url(u):
    if re.match(r"^[\w.-]+\.(no|com|org|edu|net|de|eu)/", u):   # "ntnu.edu/..." without https://
        return "https://" + u
    m = re.match(r"^https?://richahan\.folk\.ntnu\.no/((?:[\w-]+\.)+(?:no|com|org|edu|net|de|eu)/.*)$", u)
    if m:                                                           # same, made absolute against the NTNU page
        return "https://" + m.group(1)
    return u

def fmt(text, links=()):
    """Plain text -> HTML: link the linked words, bold own name, small DOI."""
    s = html.escape(text, quote=False)
    holders = []
    for (lt, href) in sorted(links, key=lambda l: -len(l[0])):
        e = html.escape(lt, quote=False)
        if e and e in s:
            holders.append(f'<a href="{html.escape(fix_url(href))}">{e}</a>')
            s = s.replace(e, f"\x00{len(holders) - 1}\x00", 1)
    s = re.sub(r"\bHann,? R\.", "<b>Hann, R.</b>", s)
    s = re.sub(r"(?<![/\w])(doi\.org/[^\s<\x00]+?)(\.?)(\s|$)",
               lambda m: f'<span class="pub-doi"><a href="https://{m.group(1)}">{m.group(1)}</a></span>{m.group(2)}{m.group(3)}', s)
    return re.sub("\x00(\\d+)\x00", lambda m: holders[int(m.group(1))], s)

def main_link(item):
    links = [l for l in item.get("links", []) if l[0] and l[1]]
    if not links:
        return "", ""
    lt, href = max(links, key=lambda l: len(l[0]))
    return lt, fix_url(href)

JOURNALS = ["Remote Sensing", "Earth-Science Reviews", "Drones,", "Journal of", "Cold Regions Science",
            "CEAS Aeronautical", "Aerospace, ", "Atmosphere, ", "Aircraft Engineering", "Water, ",
            "ACS Earth", "The Cryosphere", "Environmental Science", "IEEE Journal", "Atmospheric Measurement",
            "International Journal of Aeroacoustics"]
def category(t):
    if any(k in t for k in ["Response to Comment", "Wind Energy Science Discussions", "contribution: drone mapping"]):
        return "reports"
    if "thesis" in t.lower(): return "theses"
    if "In: Habashi" in t or "Handbook" in t: return "books"
    if any(k in t for k in ["SESS Report", "STO Technical Report", "Report. UBIQ", "EDGE Research Report",
                            "Aerospace Developments", "Book of Abstracts", "Artistic result"]): return "reports"
    if any(k in t for k in JOURNALS): return "manuscripts"
    return "conferences"

def clear(d):
    os.makedirs(d, exist_ok=True)
    for f in os.listdir(d):
        os.remove(os.path.join(d, f))

def entries(sec):
    return [i for i in sec["items"] if i.get("entry")]

# ---------------------------------------------------------------- load + validate
def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

new_path = sys.argv[1] if len(sys.argv) > 1 else None
data = load(new_path or SNAP)
S = data["sections"]
missing = [k for k in REQUIRED if k not in S]
if missing:
    sys.exit(f"ERROR: bookmark(s) not found on the NTNU page: {missing} - nothing changed.")
if new_path and os.path.exists(SNAP):
    old = load(SNAP)["sections"]
    for k in REQUIRED:
        n_old, n_new = len(entries(old.get(k, {"items": []}))), len(entries(S[k]))
        if n_old and n_new < 0.7 * n_old:
            sys.exit(f"ERROR: section {k} shrank from {n_old} to {n_new} entries - nothing changed.")

# ---------------------------------------------------------------- publications
d = os.path.join(ROOT, "_publications"); clear(d)
pubs = []
for i in entries(S["Publications"]):
    lt, href = main_link(i)
    pubs.append({"y": i["y"], "t": i["t"], "links": i["links"], "title": lt or i["t"][:80], "url": href, "cat": category(i["t"])})
for e in EXTRA_PUBS:
    pubs.append(dict(e, url=""))
pubs.sort(key=lambda p: -int(p["y"] or 0))           # stable: keeps the NTNU order inside a year
used = set()
for n, p in enumerate(pubs):
    s = f'{p["y"]}-{slug(p["title"])}'
    while s in used: s += "-2"
    used.add(s)
    cit = fmt(p["t"], p["links"])
    venue = re.sub(r"\s*doi\.org/\S+", "", p["t"].split(p["title"], 1)[1]).strip(" .") if p["title"] in p["t"] else ""
    fm = ["---", f'title: {yq(p["title"])}', "collection: publications", f'category: {p["cat"]}',
          f"permalink: /publication/{s}", f'date: {p["y"]}-01-01', f"order: {n}",
          f"venue: {yq(venue)}", "excerpt: ''", f"citation: {yq(cit)}"]
    if p["url"]: fm.append(f'paperurl: {yq(p["url"])}')
    fm.append("---")
    body = cit + "\n" + (f'\n[Open publication]({p["url"]})\n' if p["url"] else "")
    open(os.path.join(d, s + ".md"), "w", encoding="utf-8").write("\n".join(fm) + "\n" + body)

# ---------------------------------------------------------------- presentations
d = os.path.join(ROOT, "_talks"); clear(d)
used = set()
for n, i in enumerate(entries(S["Presentations"])):
    t = i["t"]
    parts = re.split(r"\s*\(\d{4}\)\.\s*", t, maxsplit=1)
    rest = parts[1] if len(parts) > 1 else t
    title, _, after = rest.partition(". ")
    after = after.rstrip(".")
    bits = [b.strip() for b in after.split(",")] if after else []
    loc = bits.pop() if len(bits) > 1 else ""
    ty = "Conference presentation"
    if bits and re.match(r"(Invited|Keynote)", bits[0], re.I):
        ty = bits.pop(0); ty = ty[0].upper() + ty[1:]
    s = f'{i["y"]}-{slug(title)}'
    while s in used: s += "-2"
    used.add(s)
    cit = fmt(t, i["links"])
    fm = ["---", f"title: {yq(title)}", "collection: talks", f"type: {yq(ty)}", f"permalink: /talks/{s}",
          f'venue: {yq(", ".join(bits))}', f'date: {i["y"]}-01-01', f"order: {n}"]
    if loc: fm.append(f"location: {yq(loc)}")
    fm += [f"citation: {yq(cit)}", "---"]
    open(os.path.join(d, s + ".md"), "w", encoding="utf-8").write("\n".join(fm) + "\n" + cit + "\n")

# ---------------------------------------------------------------- lists -> _data/folk.yml
def flist(sec_items):
    return [fmt(i["t"], i["links"]) for i in sec_items if i.get("entry")]

def in_parens(title):
    m = re.search(r"\((.*)\)\s*$", title)
    return m.group(1) if m else ""

# People: sub-headings "People – ..." start a new block, other headings ("Current") a sub-group
people = [{"title": S["People"]["title"], "groups": [{"name": "", "items": []}]}]
for i in S["People"]["items"]:
    if not i.get("entry"):
        if i["t"].startswith("People"):
            people.append({"title": i["t"], "groups": [{"name": "", "items": []}]})
        else:
            people[-1]["groups"].append({"name": i["t"], "items": []})
    else:
        people[-1]["groups"][-1]["items"].append(fmt(i["t"], i["links"]))
for p in people:
    p["groups"] = [g for g in p["groups"] if g["items"]]

# Research projects: everything after a sub-heading (e.g. "Academic Engagement & Workgroups") goes to engagement
projects, engagement, eng_title, target = [], [], "", "p"
for i in S["Research_projects"]["items"]:
    if not i.get("entry"):
        target, eng_title = "e", i["t"]
        continue
    (projects if target == "p" else engagement).append(fmt(i["t"], i["links"]))
if "Academic_engagement" in S:
    eng_title = S["Academic_engagement"]["title"]
    engagement += flist(S["Academic_engagement"]["items"])

folk = {
    "source": data.get("source", ""), "last_modified": data.get("lastModified", ""),
    "publications_title": S["Publications"]["title"],
    "presentations_title": S["Presentations"]["title"],
    "datasets_title": S["Datasets"]["title"], "datasets": flist(S["Datasets"]["items"]),
    "people": people,
    "teaching_title": S["Teaching"]["title"], "teaching": flist(S["Teaching"]["items"]),
    "funding_title": S["Funding"]["title"], "funding_header": in_parens(S["Funding"]["title"]),
    "funding": flist(S["Funding"]["items"]),
    "projects_title": S["Research_projects"]["title"], "projects": projects,
    "engagement_title": eng_title or "Academic Engagement & Workgroups", "engagement": engagement,
}
with open(os.path.join(ROOT, "_data", "folk.yml"), "w", encoding="utf-8") as f:
    json.dump(folk, f, ensure_ascii=False, indent=1)          # JSON is valid YAML

if new_path and os.path.abspath(new_path) != SNAP:
    shutil.copyfile(new_path, SNAP)

from collections import Counter
print(f"OK: {len(pubs)} publications {dict(Counter(p['cat'] for p in pubs))}, "
      f"{len(entries(S['Presentations']))} presentations, {len(folk['datasets'])} datasets, "
      f"{sum(len(g['items']) for p in people for g in p['groups'])} people, {len(folk['teaching'])} teaching, "
      f"{len(folk['funding'])} funding, {len(projects)} projects, {len(engagement)} engagement")
