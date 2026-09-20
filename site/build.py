#!/usr/bin/env python3
"""Build site/index.html from site/index.src.html. Usage: build.py [--check]

invariant: the landing page never carries its own copy of a fact. The setup prompt comes from
setup-prompt.md and the provider tables from docs/providers.md, so the page cannot say something
the repo does not. --check fails when the built page is stale; the commit hook runs it.
"""
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
read = lambda p: open(os.path.join(ROOT, p), encoding="utf-8").read()


def prompt():
    m = re.search(r"```text\n(.*?)```", read("setup-prompt.md"), re.S)
    assert m, "setup-prompt.md has no ```text block"
    return html.escape(m.group(1).rstrip("\n"))


def inline(s):
    s = html.escape(s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)


def section(name):
    """The markdown between <!-- site:name --> and <!-- /site:name -->, tables and paragraphs only."""
    m = re.search(r"<!-- site:%s -->\n(.*?)<!-- /site:%s -->" % (name, name), read("docs/providers.md"), re.S)
    assert m, "docs/providers.md has no site:%s block" % name
    out, rows = [], []

    def flush():
        if rows:
            head, body = rows[0], rows[2:]
            out.append('<div class="rows"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
                "".join("<th>%s</th>" % inline(c) for c in head),
                "".join("<tr>%s</tr>" % "".join(
                    '<th scope="row">%s</th>' % inline(c) if i == 0 else '<td data-label="%s"><span>%s</span></td>' % (html.escape(head[i]), inline(c))
                    for i, c in enumerate(r)) for r in body)))
            rows.clear()

    for line in m.group(1).splitlines():
        if line.startswith("|"):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
            continue
        flush()
        if line.strip():
            out.append("<p>%s</p>" % inline(line.strip()))
    flush()
    return "\n".join(out)


def build():
    page = read("site/index.src.html")
    page = page.replace("<!--PROMPT-->", prompt())
    for name in re.findall(r"<!--PROVIDERS:(\w+)-->", page):
        page = page.replace("<!--PROVIDERS:%s-->" % name, section(name))
    left = re.findall(r"<!--[A-Z:]+\w*-->", page)
    assert not left, "unfilled slots: %s" % left
    return page


if __name__ == "__main__":
    out = os.path.join(ROOT, "site/index.html")
    page = build()
    if "--check" in sys.argv:
        if not os.path.exists(out) or open(out, encoding="utf-8").read() != page:
            sys.exit("site/index.html is stale: run python3 site/build.py")
        print("ok")
    else:
        open(out, "w", encoding="utf-8").write(page)
        print("wrote site/index.html, %d B" % len(page.encode()))
