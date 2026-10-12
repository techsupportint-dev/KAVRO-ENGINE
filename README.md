# KAVRO-ENGINE · CredLock Tech Support System

Google Apps Script web app for CredLock technical support operations.

## Core files (Apps Script)

| File | Purpose |
|------|---------|
| `Code.gs` | Backend API, sheets, auth, chat, WhatsApp, reports |
| `Portal.html` | Main staff portal UI |
| `PublicChat.html` | Public / guest live chat page |

## Deploy

1. Create a Google Apps Script project bound to your spreadsheet (or standalone with Spreadsheet ID in Settings).
2. Paste `Code.gs` and add HTML files `Portal` and `PublicChat`.
3. Deploy as **Web app** → Execute as **Me** → Who has access **Anyone** (for webhooks/chat).
4. Use **Manage deployments → Edit → New version** so the `/exec` URL stays permanent.
5. Point `https://support.credlockng.com` (or your brand domain) at that `/exec` URL.

## Features (v14.5.3)

- Ticketing, device validation, SLA, admin settings
- Live chat (WhatsApp-style) + WhatsApp Cloud API integration
- Sign-in / register / PIN reset, roles, audit logs
- Agent live dashboard, auto-refresh, stream filters (Incoming vs Kavro)
- Missing-sheet repair, permanent URL helpers

## Connections

- Google Sheets (data)
- Google Drive (attachments/reports)
- Gmail (notifications / reset codes)
- Meta WhatsApp Cloud API (optional)

Keep one deployment URL active; do not create a new deployment for every update.
