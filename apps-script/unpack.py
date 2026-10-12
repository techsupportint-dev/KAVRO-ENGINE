#!/usr/bin/env python3
import base64, zlib, re
from pathlib import Path
from collections import defaultdict
root = Path(__file__).resolve().parent
packed = root / 'packed'
if not packed.exists():
    print('No packed/ folder. Copy full Code.gs and Portal.html from CI artifacts or Drive.')
    raise SystemExit(1)
groups = defaultdict(list)
for p in sorted(packed.glob('*.b64.*')):
    m = re.match(r'(.+)\.b64\.(\d+)$', p.name)
    if not m: continue
    groups[m.group(1)].append((int(m.group(2)), p.read_text().strip()))
for name, segs in groups.items():
    segs.sort(key=lambda x: x[0])
    data = zlib.decompress(base64.b64decode(''.join(s for _, s in segs)))
    out = root / name
    out.write_bytes(data)
    print('Wrote', out, len(data))
