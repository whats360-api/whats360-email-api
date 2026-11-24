# whats360.live Email Send API

Send email from your own application through [whats360.live](https://whats360.live): one JSON `POST` endpoint plus a login endpoint that returns a token.

> Documentation derived from the whats360.live dashboard developer pages. The whats360.live owner states the documented endpoints are tested and working. **The examples in this repository were not executed against the live service by the person who wrote them.** Code is illustrative, uses placeholders only, and was not executed unless a test is listed. whats360.live links WhatsApp numbers by QR code. It is not the Meta Cloud API, not a Business Solution Provider, and not affiliated with or endorsed by Meta. No delivery or ban-avoidance guarantees.

Base URL: `https://whats360.live`

## Flow (from the dashboard page)
1. Get a token: `POST /api/auth/login` with JSON `username` and `password`. The response contains a `token`.
2. Send: `POST /api/v1/email/send` with header `Authorization: Bearer YOUR_TOKEN` and a JSON body.

The token shown on the dashboard page is the JWT of the current session. The page says to log in again to get a fresh token, so treat it as expiring. Do not store your account password in source code. Keep it in an environment variable or a secret manager.

## Request body (all strings)
| Field | Meaning |
|---|---|
| from | Sender address. It must be one of your own accounts (domains set up in the dashboard). |
| to | Recipient address |
| subject | Subject |
| body | Message body |

Success (200): `{ "ok": true, "data": { "message": "Email sent successfully" } }`  
Error (4xx or 5xx): `{ "ok": false, "error": "Error description" }`

## DNS records the dashboard recommends
Add these to your sending domain before sending, to reduce the chance of landing in spam:
| Type | Name | Value |
|---|---|---|
| MX | @ | mail.yourdomain.com (priority 10) |
| A | mail | your server IP |
| TXT | @ | `v=spf1 ip4:SERVER_IP ~all` |
| TXT | _dmarc | `v=DMARC1; p=none` |
| TXT | default._domainkey | `v=DKIM1; k=rsa; p=...` (the DKIM value appears on the dashboard Domains page after activation) |

New domains need time to build reputation. Start with small volumes and increase gradually. whats360.live does not guarantee inbox placement and neither does this repository.

## Examples
[cURL](examples/curl.sh) · [JavaScript](examples/send-email.js) · [PHP](examples/send-email.php) · [Python](examples/send_email.py) (the Python 3 example has a unit test with a fake transport) · [OpenAPI draft](openapi.yaml)

## Gaps
Attachments, cc/bcc, HTML body, templates, token lifetime and rate limits are not documented on the page and are not invented here. See [DOCUMENTATION_GAPS.md](DOCUMENTATION_GAPS.md).

WhatsApp: https://wa.me/whats360.live · Direct chat support: https://wa.me/201030741766 · info@whats360.live
