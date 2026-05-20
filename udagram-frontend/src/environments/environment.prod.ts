export const environment = {
  production: true,
  apiUrl: (window as any).__env__?.apiUrl || '/api/v0',
};
