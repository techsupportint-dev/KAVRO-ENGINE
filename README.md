# KAVRO-ENGINE · CredLock Tech Support System

**Version:** 14.5.3  
**Repo:** https://github.com/techsupportint-dev/KAVRO-ENGINE

## Live sources (Apps Script)

Full production files are in Google Drive (latest from the build workspace). Paste into the Apps Script project:

| File | Drive |
|------|-------|
| `Code.gs` (v14.5.3) | https://drive.google.com/file/d/1FtC2sgWZnoirgm6x3IlfGx-Rszt_r3zp/view |
| `Portal.html` (v14.5.3) | https://drive.google.com/file/d/1MEUSIeSMTmUJsufNOTypkuIOm--z4Hc0/view |
| `PublicChat.html` | https://drive.google.com/file/d/1_yaLMpkhSEdHwcDQ6zINoXrLQo2QJPj5/view |

## This repository

- `README.md` — overview
- `docs/DEPLOY.md` — deploy steps
- `docs/CONNECTIONS.md` — keep Sheets, Drive, Gmail, WhatsApp, permanent URL connected
- `apps-script/PublicChat.html` — public chat entry
- `apps-script/unpack.py` — reconstruct from packed segments when present
- `apps-script/VERSION` — `14.5.3`

## Deploy (keep one permanent URL)

1. Apps Script → paste Code.gs + Portal + PublicChat  
2. Run `repairMissingSheets`  
3. **Deploy → Manage deployments → Edit → New version** (same `/exec` URL)  
4. Brand domain `https://support.credlockng.com` → that `/exec` URL  

## Connections to keep active

| Connection | Purpose |
|------------|---------|
| Google Sheets | Tickets, users, chat, audit |
| Google Drive | Attachments & reports |
| Gmail | Reset PIN + notifications |
| WhatsApp Cloud API | Optional inbound/outbound |
| GitHub | Source control (this repo) |

Do **not** create a new web-app deployment for each update — always **Edit → New version**.
