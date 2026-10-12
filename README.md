# KAVRO-ENGINE · CredLock Tech Support System

**Version:** 14.6.1  
**Repo:** https://github.com/techsupportint-dev/KAVRO-ENGINE  

## Custom portal link (GitHub Pages)

### https://techsupportint-dev.github.io/KAVRO-ENGINE/

Enable **Settings → Pages → Deploy from branch `main` / root** if the page is not live yet.

Brand domain: **https://support.credlockng.com** (point to your Apps Script `/exec`).

## Latest Apps Script sources (paste into project)

| File | Drive |
|------|-------|
| **Code.gs v14.6.1** | https://drive.google.com/file/d/1PWqxpozYaX8yHddVo1RMfyu3w7zoh5_G/view |
| **Portal.html v14.6.1** | https://drive.google.com/file/d/133zmI4eFTaU63Y8u51JROeSAo1Y2F0Dy/view |

## Deploy (keep permanent URL)

1. Open Apps Script → replace `Code.gs` and HTML file `Portal` with the files above  
2. Run `autoConfigureSystem` (optional)  
3. **Deploy → Manage deployments → Edit → New version**  
4. Hard-refresh the portal (Ctrl+Shift+R)  
5. Save the same `/exec` URL on the GitHub hub page  

## Features

- Ticketing, BNPL recovery import → KAVRO_ISSUES  
- Live Chat auto-refresh only (not Records)  
- Admin auto-configure, delete NEW_ISSUES  
- Sign-in session token, missing-sheet repair  
- Roles, audit, WhatsApp hooks, navy UI  
