"""Build calendar-viewer.html and its identical copy index.html from cultural-calendar.json."""
import json
from pathlib import Path

CAL = Path(__file__).resolve().parents[1]
d = json.loads((CAL / 'cultural-calendar.json').read_text(encoding='utf-8'))
payload = json.dumps(d['entries'], ensure_ascii=False).replace('</', '<\\/')
tpl = (CAL / 'tools' / 'viewer-template.html').read_text(encoding='utf-8')
html = tpl.replace('__DATA__', payload)
for name in ('calendar-viewer.html', 'index.html'):
    with open(CAL / name, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)
print(len(html), 'bytes')
