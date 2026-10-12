#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parent
parts = root / 'parts'
(code := root / 'Code.gs').write_text(''.join(p.read_text() for p in sorted(parts.glob('Code.gs.part*'))))
(portal := root / 'Portal.html').write_text(''.join(p.read_text() for p in sorted(parts.glob('Portal.html.part*'))))
print('Wrote', code, code.stat().st_size, 'and', portal, portal.stat().st_size)
