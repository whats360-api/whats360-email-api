# Documentation gaps (Email API)
- Token lifetime. The dashboard says to log in again for a new token.
- Attachments, cc, bcc, reply-to, HTML versus plain text body: not documented.
- Rate and volume limits: not documented.
- Whether a dedicated API token exists instead of the login flow: not documented on this page.
- Error codes: only the generic error shape is shown.
- Never post a token, password or real email address in an issue.
- Dashboard export p18 (Email Send API page, read at full size) marks `from`, `to` and `subject` as required and `body` (plain text) as not required. What happens when `body` is missing is not documented and was not tested.
- Email templates and email bots exist in the dashboard (export p19 and p20, read at full size). See dashboard-email-features.md. No API for them was shown.
