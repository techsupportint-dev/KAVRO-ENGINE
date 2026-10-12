# CredLock Tech Support — React + TypeScript (v14.7)

Bound to spreadsheet `1Xkg76BduW4xGPpU__GK0hMBxU3hQqf2Kk1BIPbBMigA` (tab **KAVRO_ISSUES**).

## Windows

```bat
cd C:\Users\April\source\repos\techsupportint-dev\KAVRO-ENGINE\react-app
git pull
npm install
copy .env.example .env
notepad .env
npm run dev
```

Open http://localhost:5173

## .env

```
VITE_GAS_EXEC_URL=https://script.google.com/macros/s/XXXX/exec
VITE_USE_MOCK=true
```

## Features

- Auth (login / session / logout)
- Dashboard KPIs + charts
- Tickets list + detail status actions
- Devices grid
- Live Chat (12s refresh)
- Settings: sheet + script binding status

Full source zip on Drive when needed; pull this repo then merge local `src/` updates.
