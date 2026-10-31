"""Build the course site into calendar/course/ from module-*.md and ../essay.md.

Run from community-360-research/:  python cross-cutting/minnesota-culture/course/build_course.py
"""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = ROOT / 'calendar' / 'course'
PROFILE = 'https://github.com/alphaequity123-afk/one-dsd-pac-standalones/blob/community-360-research/community-360-research/communities/{}/profile.md'
COURSE = 'The Water We Swim In'
SUPPORT = ('If something here brings up a hard memory or feeling, you can stop at any time. State employees can reach '
           'the State of Minnesota Employee Assistance Program for free, confidential support; your human resources '
           'office can connect you.')


def inline(t):
    t = html.escape(t, quote=False)
    keep = []

    def stash(markup):
        keep.append(markup)
        return '\x00%d\x00' % (len(keep) - 1)

    t = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)',
               lambda m: stash('<a href="%s" target="_blank" rel="noopener">%s</a>' % (m.group(2).replace('"', '%22'), m.group(1))), t)
    t = re.sub(r'(?<![\w/"])(https?://[^\s<]+[^\s<.,;)])',
               lambda m: stash('<a href="%s" target="_blank" rel="noopener">%s</a>' % (m.group(1), m.group(1))), t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return re.sub(r'\x00(\d+)\x00', lambda m: keep[int(m.group(1))], t)


def slug(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:60]


def paragraphs(lines):
    """Plain markdown: paragraphs and bullet lists."""
    out, para, items = [], [], []

    def flush():
        nonlocal para, items
        if para:
            out.append('<p>%s</p>' % inline(' '.join(para)))
            para = []
        if items:
            out.append('<ul>%s</ul>' % ''.join('<li>%s</li>' % inline(x) for x in items))
            items = []
    for s in lines:
        s = s.rstrip()
        if not s:
            flush()
        elif s.startswith('- '):
            if para:
                flush()
            items.append(s[2:])
        elif items:
            items[-1] += ' ' + s
        else:
            para.append(s)
    flush()
    return '\n'.join(out)


def scenario_html(lines, n):
    setup, question, options = [], '', []
    for s in lines:
        s = s.strip()
        if s.startswith('? '):
            question = s[2:]
        elif s.startswith('- ') and '||' in s:
            choice, fb = s[2:].split('||', 1)
            options.append((choice.strip(), fb.strip()))
        elif s:
            setup.append(s)
    label = setup[0] if setup and setup[0].lower().startswith('example') else ''
    body = setup[1:] if label else setup
    opts = ''.join(
        '<li><button type="button" class="choice" aria-expanded="false" aria-controls="fb-%d-%d" id="ch-%d-%d">%s</button>'
        '<div class="feedback" id="fb-%d-%d" hidden>%s</div></li>' % (n, i, n, i, inline(c), n, i, inline(f))
        for i, (c, f) in enumerate(options))
    return ('<section class="scenario" aria-label="Practice scenario">%s%s<p class="ask">%s</p><ol class="choices">%s</ol>'
            '<p class="hint">Choose any answer to see what it might lead to. You can open all three.</p></section>') % (
        '<p class="label">%s</p>' % inline(label) if label else '', paragraphs(body), inline(question), opts)


def module_html(md, n):
    meta_txt, body = md.split('\n---\n', 1) if md.startswith('---') else ('', md)
    meta = dict(re.findall(r'^(\w+):\s*(.+)$', meta_txt, re.M))
    main_part, _, deeper_part = body.partition('## Go deeper')
    deeper_items = re.findall(r'^- (.+)$', deeper_part, re.M)
    parts, block, buf, sec_lines = [], None, [], []
    has_note = False

    def flush_sec():
        nonlocal sec_lines
        if any(x.strip() for x in sec_lines):
            parts.append(paragraphs(sec_lines))
        sec_lines = []
    for line in main_part.split('\n'):
        s = line.rstrip()
        if block:
            if s == ':::':
                text = [x for x in buf]
                if block == 'note':
                    has_note = True
                    parts.append('<aside class="note" role="note"><strong>Content note.</strong> %s</aside>' %
                                 inline(' '.join(x.strip() for x in text if x.strip()).replace('Content note:', '').strip()))
                elif block == 'voice':
                    parts.append('<blockquote class="voice">%s</blockquote>' % paragraphs(text))
                elif block == 'fact':
                    parts.append('<aside class="fact">%s</aside>' % paragraphs(text))
                elif block == 'scenario':
                    parts.append(scenario_html(text, n))
                elif block == 'reflect':
                    items = [x.strip()[2:] for x in text if x.strip().startswith('- ')]
                    parts.append('<section class="reflect"><p class="label">For your own reflection. Nothing here is collected.</p><ol>%s</ol>'
                                 '<label for="notes-%d">Private notes (saved only in this browser)</label>'
                                 '<textarea id="notes-%d" data-key="notes-%d" rows="5"></textarea></section>' % (
                                     ''.join('<li>%s</li>' % inline(x) for x in items), n, n, n))
                elif block == 'takeaway':
                    parts.append('<aside class="takeaway"><p class="label">Practice this week</p>%s</aside>' % paragraphs(text))
                else:
                    parts.append(paragraphs(text))
                block, buf = None, []
            else:
                buf.append(s)
            continue
        m = re.match(r':::(\w+)$', s)
        if m:
            flush_sec()
            block = m.group(1)
            continue
        m = re.match(r'## (.+)', s)
        if m:
            flush_sec()
            parts.append('<h2 id="%s">%s</h2>' % (slug(m.group(1)), inline(m.group(1))))
            continue
        sec_lines.append(s)
    flush_sec()
    html_body = '\n'.join(parts)
    if deeper_items:
        html_body += '\n<h2 id="go-deeper">Go deeper</h2>\n<ul class="deeper">%s</ul>' % ''.join(deeper_link(x) for x in deeper_items)
    return meta, html_body, has_note


ESSAY_IDS = {}
TITLES = json.loads((ROOT / 'calendar' / 'tools' / 'community-titles.json').read_text(encoding='utf-8'))


def deeper_link(text):
    m = re.match(r'Essay, section (\d+)', text)
    if m and m.group(1) in ESSAY_IDS:
        return '<li><a href="/course/essay.html#%s">%s</a></li>' % (ESSAY_IDS[m.group(1)], inline(text))
    m = re.match(r'Community profile: (.+)', text)
    if m:
        name = m.group(1).strip().rstrip('.')
        cid = next((k for k, v in TITLES.items() if name.lower() in v.lower() or name.lower() == k.replace('-', ' ')), None)
        if cid and (ROOT / 'communities' / cid / 'profile.md').exists():
            return '<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (PROFILE.format(cid), inline(text))
    return '<li>%s</li>' % inline(text)


def essay_html():
    md = (ROOT / 'cross-cutting' / 'minnesota-culture' / 'essay.md').read_text(encoding='utf-8')
    out, para, items, ltype = [], [], [], None

    def flush():
        nonlocal para, items, ltype
        if para:
            out.append('<p>%s</p>' % inline(' '.join(para)))
            para = []
        if items:
            tag = 'ol class="sources"' if ltype == 'ol' else 'ul'
            out.append('<%s>%s</%s>' % (tag, ''.join('<li>%s</li>' % inline(x) for x in items), tag.split()[0]))
            items, ltype = [], None
    toc = []
    for s in md.split('\n'):
        s = s.rstrip()
        if not s:
            flush()
            continue
        if s.startswith('# ') or s.startswith('Checked:'):
            continue
        m = re.match(r'(#{2,3}) (.+)', s)
        if m:
            flush()
            sid = slug(m.group(2))
            num = re.match(r'(\d+)\.', m.group(2))
            if num and len(m.group(1)) == 2:
                ESSAY_IDS[num.group(1)] = sid
            if len(m.group(1)) == 2:
                toc.append((sid, m.group(2)))
            out.append('<h%d id="%s">%s</h%d>' % (len(m.group(1)), sid, inline(m.group(2)), len(m.group(1))))
            continue
        if s.startswith('> '):
            flush()
            out.append('<aside class="note" role="note">%s</aside>' % inline(s[2:]))
            continue
        m = re.match(r'(- |\d+\. )(.*)', s)
        if m:
            kind = 'ol' if m.group(1)[0].isdigit() else 'ul'
            if para or (ltype and ltype != kind):
                flush()
            ltype = kind
            items.append(m.group(2))
            continue
        if items:
            items[-1] += ' ' + s
        else:
            para.append(s)
    flush()
    return toc, '\n'.join(out)


def page(title, body, active=None, extra_head=''):
    nav = ''.join('<li><a href="/course/module-%d.html"%s>Module %d</a></li>' % (i, ' aria-current="page"' if active == i else '', i) for i in range(1, 7))
    return '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@500;600;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&display=swap">
<link rel="stylesheet" href="/course/course.css">
%s</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bar"><div class="bar-in"><a class="home" href="/course/">%s</a><nav aria-label="Modules"><ol class="mods">%s<li><a href="/course/essay.html"%s>Essay</a></li></ol></nav></div></header>
<main id="main" class="wrap">
%s
</main>
<script src="/course/course.js"></script>
</body>
</html>
''' % (html.escape(title), extra_head, COURSE, nav, ' aria-current="page"' if active == 'essay' else '', body)


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    toc, essay_body = essay_html()
    mods = []
    for n in range(1, 7):
        src = HERE / ('module-%d.md' % n)
        if not src.exists():
            raise SystemExit('missing ' + src.name)
        meta, body, has_note = module_html(src.read_text(encoding='utf-8'), n)
        mods.append((n, meta))
        support = '<aside class="support">%s</aside>' % SUPPORT if has_note else ''
        prev_link = '<a href="/course/module-%d.html">&larr; Module %d</a>' % (n - 1, n - 1) if n > 1 else '<a href="/course/">&larr; Course home</a>'
        next_link = '<a href="/course/module-%d.html">Module %d &rarr;</a>' % (n + 1, n + 1) if n < 6 else '<a href="/course/">Course home &rarr;</a>'
        content = '''<article class="module">
<p class="kicker">Module %d of 6 &middot; About %s minutes</p>
<h1>%s</h1>
<p class="goal">%s</p>
%s
%s
<div class="done"><button type="button" class="done-btn" id="done-%d" data-done="%d" aria-pressed="false">Mark this module finished</button><span class="done-note">Saved only in this browser.</span></div>
<nav class="pager" aria-label="Module navigation">%s%s</nav>
</article>''' % (n, html.escape(meta.get('minutes', '20')), inline(meta.get('title', 'Module %d' % n)), inline(meta.get('goal', '')),
                 support, body, n, n, prev_link, next_link)
        (OUT / ('module-%d.html' % n)).write_text(page('Module %d: %s' % (n, meta.get('title', '')), content, n), encoding='utf-8')
    cards = ''.join('''<li class="card"><a href="/course/module-%d.html"><span class="num">%d</span><span class="ct"><strong>%s</strong><span>%s</span></span><span class="status" data-status="%d">Not finished</span></a></li>''' % (
        n, n, inline(m.get('title', '')), inline(m.get('goal', '')), n) for n, m in mods)
    index = '''<section class="intro">
<p class="kicker">A voluntary course for Minnesota Department of Human Services staff</p>
<h1>%s</h1>
<p class="lede">Most training on culture asks us to learn about other people's cultures. This course asks a different question first: what does our own culture look like, and how does it shape the way we serve Minnesotans whose cultures differ from ours?</p>
<p>Six modules, about 20 minutes each. Take them in order or one at a time. Each one opens with something familiar, explains the research in plain language with every fact linked to its source, offers one practice scenario, and ends with private reflection and one habit to try.</p>
</section>
<ol class="cards">%s</ol>
<section class="how">
<h2>How this course works</h2>
<ul>
<li><strong>Private by design.</strong> Your checkmarks and notes are saved only in your own browser. Nothing is collected or graded.</li>
<li><strong>Examples are labeled.</strong> Practice scenarios are composites written for teaching. They are not real cases or real people.</li>
<li><strong>Content notes.</strong> Modules 4 and 5 include a short note before passages that describe violence, deaths or abuse, so you can pause or skip ahead.</li>
<li><strong>Frameworks are mirrors.</strong> The research describes averages and tendencies. It never tells you who any one person is.</li>
</ul>
<p class="support">%s</p>
<p>The <a href="/">Minnesota cultural calendar</a> is part of the same research. The course is drawn from <a href="/course/essay.html">the full essay</a>, which has every source, and from the Community 360 profiles of 39 Minnesota communities.</p>
</section>''' % (COURSE, cards, SUPPORT)
    (OUT / 'index.html').write_text(page(COURSE, index), encoding='utf-8')
    toc_html = ''.join('<li><a href="#%s">%s</a></li>' % (sid, inline(t)) for sid, t in toc)
    essay_page = '''<article class="essay">
<p class="kicker">The essay behind the course</p>
<h1>%s</h1>
<details class="toc"><summary>Contents</summary><ol>%s</ol></details>
%s
</article>''' % (COURSE, toc_html, essay_body)
    (OUT / 'essay.html').write_text(page('%s: the essay' % COURSE, essay_page, 'essay'), encoding='utf-8')
    for f in ('course.css', 'course.js'):
        (OUT / f).write_text((HERE / f).read_text(encoding='utf-8'), encoding='utf-8')
    print('built', len(mods), 'modules, essay and index into', OUT.relative_to(ROOT))


if __name__ == '__main__':
    build()
