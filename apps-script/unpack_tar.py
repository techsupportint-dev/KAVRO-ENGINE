#!/usr/bin/env python3
import base64, tarfile, io
from pathlib import Path
root = Path(__file__).resolve().parent
packed = root / 'packed'
parts = sorted(packed.glob('sources.tar.gz.b64.*'))
if not parts:
    print('No sources.tar.gz.b64.* segments found. Use Drive links in README.md')
    raise SystemExit(1)
b64 = ''.join(p.read_text().strip() for p in parts)
data = base64.b64decode(b64)
tar = tarfile.open(fileobj=io.BytesIO(data), mode='r:gz')
tar.extractall(path=root)
print('Extracted:', tar.getnames())
