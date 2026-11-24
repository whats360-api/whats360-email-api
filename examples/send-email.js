// Placeholders only. Not run against the live service. Node 18+.
const BASE = 'https://whats360.live';
export async function login(username, password) {
  const res = await fetch(`${BASE}/api/auth/login`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ username, password }) });
  return (await res.json()).token;
}
export async function sendEmail(token, { from, to, subject, body }) {
  const res = await fetch(`${BASE}/api/v1/email/send`, { method: 'POST', headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' }, body: JSON.stringify({ from, to, subject, body }) });
  return res.json(); // { ok: true, data: { message } } or { ok: false, error }
}
