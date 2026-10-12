# Packed sources

Full `Code.gs` and `Portal.html` are large (~500KB each).

## Recommended (always latest)

Download from Google Drive (linked in root README) and paste into Apps Script.

## Reconstruct from segments

If `sources.tar.gz.b64.*` segments are present under this folder:

```bash
cd apps-script
python3 unpack_tar.py
```

Or from Drive artifact copies in the project workspace: `KAVRO_PORTAL_V6/Code.gs` and `Portal.html`.
