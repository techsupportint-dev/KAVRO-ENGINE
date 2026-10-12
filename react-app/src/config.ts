/** CredLock backend constants — match Apps Script CONFIG */
export const APP = {
  name: 'CredLock Tech Support',
  version: '14.7.0',
  spreadsheetId: '1Xkg76BduW4xGPpU__GK0hMBxU3hQqf2Kk1BIPbBMigA',
  scriptId: '1G0VYOg2mvRRD3OiEPurfT1ACspQZ0BqFaT4UAJcQsW6wC2u3WgJCyI_k',
  sheetUrl: 'https://docs.google.com/spreadsheets/d/1Xkg76BduW4xGPpU__GK0hMBxU3hQqf2Kk1BIPbBMigA/edit',
  scriptUrl: 'https://script.google.com/home/projects/1G0VYOg2mvRRD3OiEPurfT1ACspQZ0BqFaT4UAJcQsW6wC2u3WgJCyI_k/edit',
  hubUrl: 'https://techsupportint-dev.github.io/KAVRO-ENGINE/',
  primaryTab: 'KAVRO_ISSUES',
} as const;

export const TABS = {
  tickets: 'KAVRO_ISSUES',
  users: 'USERS',
  customers: 'CUSTOMERS',
  devices: 'DEVICES',
  activity: 'TICKET_ACTIVITY',
  audit: 'AUDIT',
  chatThreads: 'CHAT_THREADS',
  chatMessages: 'CHAT_MESSAGES',
} as const;
