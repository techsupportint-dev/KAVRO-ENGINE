# KAVRO-ENGINE · CredLock Tech Support System

**Version:** 14.6.0  
**Repo:** https://github.com/techsupportint-dev/KAVRO-ENGINE  

## Custom portal link (GitHub Pages)

Enable **Settings → Pages → Deploy from branch `main` / root** (or allow the Pages workflow).

### https://techsupportint-dev.github.io/KAVRO-ENGINE/

Use that URL as your public **portal hub**. Enter your Apps Script `/exec` URL once on the page — it opens the live system.

Brand domain (point to the same `/exec`):

**https://support.credlockng.com**

## Live Apps Script sources (paste into project)

| File | Drive |
|------|-------|
| Code.gs v14.6 | https://drive.google.com/file/d/1o8ipobUzNEkERdJdMPtGVOQb8BE4-nQz/view |
| Portal.html v14.6 | https://drive.google.com/file/d/1e9kzdk76Zzu3Os-J6yAdNRtfiKB7CACi/view |

## Deploy (permanent URL)

1. Paste Code.gs + Portal (+ PublicChat) into Apps Script  
2. Run `autoConfigureSystem`  
3. **Manage deployments → Edit → New version** (keep the same `/exec` link)  
4. Save that `/exec` on the GitHub Pages hub  

## Features (14.6)

- Ticketing, BNPL recovery import → KAVRO_ISSUES  
- Live Chat auto-refresh only (not Records)  
- Admin auto-configure, delete NEW_ISSUES  
- Roles, audit, WhatsApp Cloud API hooks  
- Navy / white professional UI  

## Structure

- `index.html` — GitHub Pages portal hub  
- `docs/` — deploy & connections  
- `apps-script/` — helpers & version  
