// Extract bookmarked sections from Richard Hann's folk.ntnu.no page (Word-exported HTML).
//
// Usage:  node scripts/folk_extract.mjs [url] > markdown_generator/folk_snapshot.json
// Needs:  npm install jsdom
//
// The page is split at Word bookmarks (<a name="...">). Bookmarks whose name starts
// with "_" are Word-internal and ignored. Every text block after a bookmark belongs to
// that section until the next bookmark. For each block we keep: the year (from the year
// column in tables), the plain text, the links, and whether it is a list entry
// (bullet or table row) or a sub-heading.

const DEFAULT_URL = "https://richahan.folk.ntnu.no/index.htm";

export function extractFolk(doc) {
  const norm = (s) => (s || "").replace(/[\s ]+/g, " ").trim();
  const isMark = (el) => el.tagName === "A" && el.getAttribute("name") && !el.getAttribute("name").startsWith("_");
  const isBlock = (el) => /^(P|LI|H[1-6])$/.test(el.tagName) && !el.querySelector("p, li, h1, h2, h3, h4, h5, h6");

  const sections = {};
  const order = [];
  let current = null;

  for (const el of doc.body.querySelectorAll("*")) {
    if (isMark(el)) {
      // bookmark anchors are handled when their enclosing block is visited;
      // a bookmark outside any block starts a section here
      if (!el.closest("p, li, h1, h2, h3, h4, h5, h6")) {
        current = el.getAttribute("name");
        if (!sections[current]) { sections[current] = { title: "", items: [] }; order.push(current); }
      }
      continue;
    }
    if (!isBlock(el)) continue;

    const mark = [...el.querySelectorAll("a[name]")].find(isMark);
    let text = norm(el.textContent);
    if (mark) {
      current = mark.getAttribute("name");
      if (!sections[current]) { sections[current] = { title: text, items: [] }; order.push(current); }
      continue;                                   // the bookmarked line is the section heading
    }
    if (!current || !text || /^\d{4}$/.test(text)) continue;

    // year from the first cell of the table row (publication / presentation tables)
    let year = "";
    const td = el.closest("td");
    const tr = td && td.closest("tr");
    if (tr && tr.cells && tr.cells.length > 1 && tr.cells[0] !== td) {
      const y = norm(tr.cells[0].textContent);
      if (/^\d{4}$/.test(y)) sections[current].lastYear = y;   // empty year cell = same year as above
      year = sections[current].lastYear || "";
    }
    const bullet = /^[·•▪\-–]\s/.test(text) || el.tagName === "LI";
    text = text.replace(/^[·•▪]\s*/, "");
    const links = [...el.querySelectorAll("a[href]")]
      .map((a) => [norm(a.textContent), a.getAttribute("href")])
      .filter((l) => l[0] && l[1]);
    sections[current].items.push({ y: year, t: text, links, entry: Boolean(year) || bullet });
  }
  return { order, sections };
}

// ---------- command line (Node) ----------
const isMain = typeof process !== "undefined" && process.argv[1] && import.meta.url.endsWith(process.argv[1].split("/").pop());
if (isMain) {
  const url = process.argv[2] || DEFAULT_URL;
  const { JSDOM } = await import("jsdom");
  const res = await fetch(url, { headers: { "User-Agent": "richard-hann.github.io sync" } });
  if (!res.ok) { console.error(`HTTP ${res.status} for ${url}`); process.exit(1); }
  const buf = Buffer.from(await res.arrayBuffer());
  const head = buf.subarray(0, 4000).toString("latin1");
  const m = head.match(/charset=["']?([\w-]+)/i);
  const html = new TextDecoder(m ? m[1] : "utf-8").decode(buf);
  const doc = new JSDOM(html, { url }).window.document;
  // make all links absolute
  for (const a of doc.querySelectorAll("a[href]")) {
    try { a.setAttribute("href", new URL(a.getAttribute("href"), url).href); } catch { /* keep */ }
  }
  const data = extractFolk(doc);
  data.source = url;
  data.lastModified = res.headers.get("last-modified") || "";
  process.stdout.write(JSON.stringify(data, null, 1));
}
