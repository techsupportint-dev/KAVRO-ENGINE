# CredLock Tech Support — React + TypeScript

Modern front-end for data structure, layout, and charts. Bridges to Google Apps Script.

## Stack

- React 18 + TypeScript + Vite
- React Router layout
- Recharts dashboard
- Typed domain models (`src/types/helpdesk.ts`)
- GAS API bridge (`src/services/gasApi.ts`)
- Navy / white design system

## Run

```bash
cd react-app
npm install
cp .env.example .env
npm run dev
```

```
VITE_GAS_EXEC_URL=https://script.google.com/macros/s/XXXX/exec
VITE_USE_MOCK=true
```

## Pages

Dashboard · Tickets · Live Chat (12s auto-refresh) · Devices · Analytics · Admin · Settings

Full zip: see Drive release `credlock-react-ts-v14.6.1.zip` linked from root README.
