"""Merge the calculated seed entries with each community's researched entries.

Writes cultural-calendar.json, cultural-calendar.ics and calendar-by-month.md.
One entry per observance per community; `observanceKey` groups the same
observance across communities. Dates checked against opened official sources
in date-checks.json override and verify seed dates.
Run: python calendar/tools/merge_calendar.py
"""
import json, datetime as dt
from pathlib import Path

CAL = Path(__file__).resolve().parents[1]
ROOT = CAL.parent
BRIEF = 'https://one-dsd-people-access-culture-production.up.railway.app/minnesota-communities/'
PROFILE = 'https://github.com/alphaequity123-afk/one-dsd-pac-standalones/blob/community-360-research/community-360-research/communities/{}/profile.md'
DATA = Path(r'C:\Users\garyb\Projects\one-dsd-web-consult\lib\content\community-design-data.json')
TITLES = {x['id']: x['title'] for x in json.loads(DATA.read_text(encoding='utf-8'))}
TITLES.setdefault('deaf-deafblind-hard-of-hearing', 'Deaf, DeafBlind and Hard of Hearing Minnesotans')
IDS = sorted(p.stem for p in (CAL / 'seed-by-community').glob('*.json'))
ORDER = ['id', 'observanceKey', 'name', 'alsoKnownAs', 'communities', 'briefLinks', 'profileLink', 'kind', 'capsule',
         'dateRule', 'dates', 'dateCertainty', 'whatItMarks', 'howCelebratedInMinnesota', 'minnesotaEvents', 'workplaceNote', 'sources']


def slug(s):
    return '-'.join(''.join(c for c in s.lower() if c.isalnum() or c == ' ').split())


def capsule(text):
    text = (text or '').strip()
    words = text.split()
    return text if len(words) <= 25 else ' '.join(words[:25]) + '…'


def norm_date(d):
    return dict(year=d['year'], date=d.get('date'), endDate=d.get('endDate'), source=d.get('source'),
                sourceUrl=d.get('sourceUrl'), verified=bool(d.get('verified')))


checks = {}
cp = CAL / 'tools' / 'date-checks.json'
if cp.exists():
    for c in json.loads(cp.read_text(encoding='utf-8'))['checks']:
        checks[(c['seedId'], c['year'])] = c

entries, seen = [], set()
for cid in IDS:
    seeds = {e['id']: e for e in json.loads((CAL / 'seed-by-community' / f'{cid}.json').read_text(encoding='utf-8'))}
    f = ROOT / 'communities' / cid / 'calendar-entries.json'
    rs = json.loads(f.read_text(encoding='utf-8')) if f.exists() else dict(entries=[], droppedSeedEntries=[])
    dropped = {x['id'] for x in rs.get('droppedSeedEntries', [])}
    used = {r.get('seedId') for r in rs['entries'] if r.get('seedId')}
    rows = list(rs['entries'])
    for sid, s in seeds.items():
        if sid in used or sid in dropped:
            continue
        rows.append(dict(seedId=sid, name=s['name'], alsoKnownAs=s['alsoKnownAs'], kind=s['kind'], dateRule=s['dateRule'],
                         dates=s['dates'], dateCertainty=s['dateCertainty'], whatItMarks=s['whatItMarks'],
                         howCelebratedInMinnesota=None, minnesotaEvents=[], workplaceNote=None, sources=[]))
    for r in rows:
        key = r.get('seedId') or slug(r['name'])
        eid = f'{cid}--{slug(r["name"])}'
        n = 2
        while eid in seen:
            eid = f'{cid}--{slug(r["name"])}-{n}'
            n += 1
        seen.add(eid)
        dates = [norm_date(d) for d in r.get('dates', [])]
        for d in dates:
            c = checks.get((r.get('seedId'), d['year']))
            # A check replaces a date only if the entry has not got its own organizer-verified date.
            if c and not d['verified']:
                d.update(date=c['date'], source=c['source'], sourceUrl=c['sourceUrl'], verified=True)
        e = dict(r, id=eid, observanceKey=key, communities=[cid], dates=dates,
                 briefLinks=[dict(community=cid, title=TITLES.get(cid, cid), url=BRIEF + cid)],
                 profileLink=PROFILE.format(cid) if (ROOT / 'communities' / cid / 'profile.md').exists() else None,
                 capsule=r.get('capsule') or capsule(r.get('whatItMarks')))
        for k, default in (('alsoKnownAs', []), ('minnesotaEvents', []), ('sources', []), ('howCelebratedInMinnesota', None), ('workplaceNote', None)):
            e.setdefault(k, default)
        entries.append({k: e[k] for k in ORDER})

today = dt.date.today().isoformat()
(CAL / 'cultural-calendar.json').write_text(json.dumps(dict(generated=today, note='One entry per observance per community. A date marked verified has an opened source stating it; other dates are projections.', entries=entries), ensure_ascii=False, indent=1), encoding='utf-8')


# ICS: verified dates only, one event per observance per date, listing every community.
def esc(s):
    return str(s).replace('\\', '\\\\').replace(';', '\\;').replace(',', '\\,').replace('\n', '\\n')


def fold(line):
    out, b = [], line.encode('utf-8')
    while len(b) > 73:
        cut = 73
        while (b[cut] & 0xC0) == 0x80:
            cut -= 1
        out.append(b[:cut].decode('utf-8'))
        b = b[cut:]
    out.append(b.decode('utf-8'))
    return '\r\n '.join(out)


groups = {}
for e in entries:
    for d in e['dates']:
        if d['date'] and d['verified']:
            groups.setdefault((e['observanceKey'], d['date'], d['endDate']), []).append((e, d))
lines = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//community-360-research//cultural-calendar//EN', 'CALSCALE:GREGORIAN', 'X-WR-CALNAME:Minnesota cultural calendar']
for (key, start, end), items in sorted(groups.items(), key=lambda kv: kv[0][1]):
    e, d = items[0]
    day = dt.date.fromisoformat(start)
    last = dt.date.fromisoformat(end) if end else day
    who = ', '.join(sorted({TITLES.get(i[0]['communities'][0], i[0]['communities'][0]) for i in items}))
    desc = f"{e['whatItMarks']} Date: {e['dateRule']} Source: {d['source']} {d['sourceUrl'] or ''} Communities: {who}"
    lines += ['BEGIN:VEVENT', f'UID:{key}-{start}@community-360-research', f'DTSTAMP:{today.replace("-", "")}T000000Z',
              f'DTSTART;VALUE=DATE:{day:%Y%m%d}', f'DTEND;VALUE=DATE:{last + dt.timedelta(days=1):%Y%m%d}',
              fold('SUMMARY:' + esc(e['name'])), fold('DESCRIPTION:' + esc(desc)), 'CATEGORIES:' + esc(e['kind']), 'TRANSP:TRANSPARENT', 'END:VEVENT']
lines.append('END:VCALENDAR')
(CAL / 'cultural-calendar.ics').write_bytes(('\r\n'.join(lines) + '\r\n').encode('utf-8'))

# Month view, grouped by observance on each date.
md = ['# Minnesota cultural calendar by month, 2026 to 2028', '',
      'A plain date has an opened source stating it. "About" means the day is not yet confirmed for that year: moon-sighted dates are set by each mosque or religious authority, and other dates here are projections until a source confirms them.']
rows = {}
for e in entries:
    for d in e['dates']:
        if d['date']:
            rows.setdefault((d['date'], e['observanceKey']), []).append((e, d))
cur = None
for (date, key), items in sorted(rows.items()):
    day = dt.date.fromisoformat(date)
    label = f'{day:%B %Y}'
    if label != cur:
        md += ['', f'## {label}', '']
        cur = label
    e, d = items[0]
    about = '' if all(i[1]['verified'] for i in items) else 'about '
    span = ''
    if d['endDate']:
        last = dt.date.fromisoformat(d['endDate'])
        span = f' to {last:%B} {last.day}'
    links = ', '.join(f"[{i[0]['briefLinks'][0]['title']}]({i[0]['briefLinks'][0]['url']})" for i in items)
    md.append(f"- {about}{day:%A, %B} {day.day}{span}: **{e['name']}**. {e['capsule']} {links}")
md += ['', '## Dates each organizer announces', '']
for e in entries:
    if not any(d['date'] for d in e['dates']):
        md.append(f"- **{e['name']}** ({e['briefLinks'][0]['title']}): {e['dateRule']}")
(CAL / 'calendar-by-month.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print(len(entries), 'entries;', len(groups), 'ics events')
