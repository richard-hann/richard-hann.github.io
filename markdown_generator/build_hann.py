# -*- coding: utf-8 -*-
"""Regenerate _publications/ and _talks/ from hann_publications.py.
Usage (from repo root):  python3 markdown_generator/build_hann.py
"""
import os, re, sys, html, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from hann_publications import PUBS, EXTRA, TALKS

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()[:60].rstrip("-")
def yq(s): return "'" + s.replace("'", "''") + "'"

JOURNALS = ["Remote Sensing", "Earth-Science Reviews", "Drones,", "Journal of", "Cold Regions Science",
            "CEAS Aeronautical", "Aerospace, ", "Atmosphere, ", "Aircraft Engineering", "Water, ",
            "ACS Earth", "The Cryosphere", "Environmental Science", "IEEE Journal", "Atmospheric Measurement",
            "International Journal of Aeroacoustics", "Wind Energy Science"]
def category(t):
    # counted as "other" on folk.ntnu.no: comments, preprints, contributions
    if any(k in t for k in ["Response to Comment", "Wind Energy Science Discussions", "contribution: drone mapping"]): return "reports"
    if "thesis" in t.lower(): return "theses"
    if "In: Habashi" in t: return "books"
    if any(k in t for k in ["SESS Report", "STO Technical Report", "Report. UBIQ", "EDGE Research Report",
                            "Aerospace Developments", "Book of Abstracts", "Artistic result"]): return "reports"
    if any(k in t for k in JOURNALS): return "manuscripts"
    return "conferences"

def fmt(text, url, title):
    s = html.escape(text, quote=False)
    s = re.sub(r"\bHann,? R\.", "<b>Hann, R.</b>", s)
    s = re.sub(r"(?<![/\w])(doi\.org/[^\s<]+?)(\.?)(\s|$)",
               lambda m: f'<span class="pub-doi"><a href="https://{m.group(1)}">{m.group(1)}</a></span>{m.group(2)}{m.group(3)}', s)
    t = html.escape(title, quote=False)
    if url and t in s:
        s = s.replace(t, f'<a href="{html.escape(url)}">{t}</a>', 1)
    return s

d = os.path.join(ROOT, "_publications")
for f in os.listdir(d): os.remove(os.path.join(d, f))
items = [(y, t, u, ti, category(t)) for (y, t, u, ti) in PUBS] + list(EXTRA)
# keep EXTRA inside their year at the end of that year
items.sort(key=lambda x: -int(x[0]))
used = set()
for i, (y, t, u, ti, cat) in enumerate(items):
    s = f"{y}-{slug(ti)}"
    while s in used: s += "-2"
    used.add(s)
    m = re.search(r"\((?:\d{4}|Ed\.)\)\.?\s*(.*)$", t)
    venue = re.sub(r"\s*doi\.org/\S+", "", t.split(ti, 1)[1]).strip(" .") if ti in t else ""
    doi = re.search(r"doi\.org/(\S+?)\.?(\s|$)", t)
    fm = ["---", f"title: {yq(ti)}", "collection: publications", f"category: {cat}",
          f"permalink: /publication/{s}", f"date: {y}-01-01", f"order: {i}",
          f"venue: {yq(venue)}", "excerpt: ''", f"citation: {yq(fmt(t, u, ti))}"]
    if u: fm.append(f"paperurl: {yq(u)}")
    fm.append("---")
    body = fmt(t, u, ti) + "\n"
    if u: body += f"\n[Open publication]({u})\n"
    open(os.path.join(d, s + ".md"), "w", encoding="utf-8").write("\n".join(fm) + "\n" + body)

d = os.path.join(ROOT, "_talks")
for f in os.listdir(d): os.remove(os.path.join(d, f))
used = set()
for i, (y, t) in enumerate(TALKS):
    authors, rest = re.split(r"\s*\(\d{4}\)\.\s*", t, maxsplit=1)
    title, after = rest.split(". ", 1)
    after = after.rstrip(".")
    parts = [p.strip() for p in after.split(",")]
    loc = parts[-1] if len(parts) > 1 else ""
    venue_parts = parts[:-1] if len(parts) > 1 else parts
    ty = "Conference presentation"
    if re.match(r"(Invited|Keynote)", venue_parts[0]):
        ty = venue_parts.pop(0)
        ty = ty[0].upper() + ty[1:]
    venue = ", ".join(venue_parts)
    s = f"{y}-{slug(title)}"
    while s in used: s += "-2"
    used.add(s)
    fm = ["---", f"title: {yq(title)}", "collection: talks", f"type: {yq(ty)}", f"permalink: /talks/{s}",
          f"venue: {yq(venue)}", f"date: {y}-01-01", f"order: {i}"]
    if loc: fm.append(f"location: {yq(loc)}")
    cit = re.sub(r"\bHann,? R\.", "<b>Hann, R.</b>", html.escape(t, quote=False))
    fm.append(f"citation: {yq(cit)}")
    fm.append("---")
    body = cit + "\n"
    open(os.path.join(d, s + ".md"), "w", encoding="utf-8").write("\n".join(fm) + "\n" + body)
from collections import Counter
print(len(items), "publications", dict(Counter(x[4] for x in items)), "|", len(TALKS), "talks")

# ---------- datasets, people, funding, projects -> _data/folk.yml ----------
import json
from hann_more import DATASETS, DATASETS_HEADER, PEOPLE, FUNDING, FUNDING_HEADER, PROJECTS
def items(lst): return [fmt(t, u, ti) for (t, u, ti) in lst]
data = {
  "datasets_header": DATASETS_HEADER, "datasets": items(DATASETS),
  "people": [{"title": sec, "groups": [{"name": g or "", "items": items(lst)} for (g, lst) in groups]} for (sec, groups) in PEOPLE],
  "funding_header": FUNDING_HEADER, "funding": items(FUNDING),
  "projects": items(PROJECTS),
}
# JSON is valid YAML
open(os.path.join(ROOT, "_data", "folk.yml"), "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, indent=1))
print(len(DATASETS), "datasets,", len(FUNDING), "funding,", len(PROJECTS), "projects")
