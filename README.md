# KAVRO-ENGINE · CredLock Tech Support System

**Version:** 14.5.3  
**Repo:** https://github.com/techsupportint-dev/KAVRO-ENGINE

## Live sources (Apps Script)

Full production files (latest build) — paste into Apps Script:

| File | Drive |
|------|-------|
| `Code.gs` (v14.5.3) | https://drive.google.com/file/d/1GFajWeRY8lb8-WVfPYox5Npy1GQU1Xa4/view |
| `Portal.html` (v14.5.3) | https://drive.google.com/file/d/1ecnJuISZKNVajfjemZAH6bLPkAqE3r3s/view |
| `PublicChat.html` | https://drive.google.com/file/d/1_yaLMpkhSEdHwcDQ6zINoXrLQo2QJPj5/view |

## Repository layout

- `README.md` — overview
- `docs/DEPLOY.md` — deploy steps
- `docs/CONNECTIONS.md` — keep Sheets, Drive, Gmail, WhatsApp, permanent URL connected
- `apps-script/` — helpers, VERSION, PublicChat entry, unpack scripts

## Deploy (permanent URL)

1. Paste `Code.gs` + `Portal` + `PublicChat` into Apps Script  
2. Run `repairMissingSheets`  
3. **Manage deployments → Edit → New version** (same `/exec` URL)  
4. Point `https://support.credlockng.com` at that `/exec` URL  

## Keep connections active

| Connection | Purpose |
|------------|---------|
| Google Sheets | Tickets, users, chat, audit |
| Google Drive | Attachments & reports |
| Gmail | PIN reset + notifications |
| WhatsApp Cloud API | Optional messaging |
| GitHub | This repo |

Never create a new web-app deployment for each update — always **Edit → New version**.
