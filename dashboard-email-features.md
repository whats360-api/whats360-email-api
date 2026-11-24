# Email dashboard features (not API)

Source: whats360.live dashboard screenshots, export pages p19 to p28, read at full size. Page headers are dated 2026-05-07. These are screen descriptions, not API documentation. No endpoint for these features was shown.

## Email templates (p19)
The page is titled for creating and managing HTML email templates. Fields on the "new template" form:
- Category (a dropdown, default "General"), template name, email subject.
- Template content: a rich text editor with Preview and HTML code views.
- Variables you can use in a template: `{company}`, `{date}`, `{email}`, `{name}`.
- Buttons: create template, cancel. A saved template card offers delete, edit and send icons.

## Email bots (p20)
Automatic replies to incoming email. The page says the incoming mailbox is checked every 5 minutes. Fields on the "new bot" form:
- Bot name and the email account it works on.
- When the bot replies: on every message, or when a keyword matches.
- Reply subject (optional) and reply text. Variables shown: `{email}` (sender) and `{subject}` (original subject).
- Delay before replying, in seconds (0 means reply immediately).
- An enabled switch.

## Email campaigns (p21-22)
Bulk email to mailing lists. Fields on the "new campaign" form:
- Sending account, campaign name, subject (the page says `{name}` and `{email}` can be used).
- Optional template, message text with the same editor and variables (`{company}`, `{date}`, `{email}`, `{name}`).
- Delay between messages in seconds. The page says the minimum is 2 seconds to avoid spam filters.
- Recipient list: optional, one email per line or comma separated. Buttons can fill it from a mail list or from the phone book.
- Each campaign card shows status, total, sent, failed and a progress bar.

## Mailing lists (p23-24)
A table with list name, description, member count and date. A "create list" dialog asks for a list name and an optional description.

## Mailboxes (p25-26)
Create and manage mailboxes per domain. You first pick one of your domains, then create a mailbox: a name before the `@` and a quota. The quota choices shown are 100 MB, 250 MB, 500 MB, 1 GB and 2 GB. The mailbox table lists the address, quota, status and action icons (delete, refresh, settings, edit, forward).

## Domains and email dashboard (p27-28)
- Domains page: "Add domain" with a counter (4 of 10 shown for that account), an expandable "How email hosting works" box, and a card per domain with DNS check, DNS verified and DKIM status. A DKIM TXT record is shown for the host `default._domainkey` to add in your DNS, and the page says that once added, mail is signed automatically and is less likely to land in spam. Each account's DKIM value is private to that account, so no value is shown here.
- Email dashboard: tiles for domains, active domains and domains under review, plus a domain list with Accounts and Inbox buttons. In the export this page is cut off on the right, so some labels were not visible.

## Not documented
- Whether templates can be used from the Send API, limits on templates or bots, and how keyword matching works are not shown. Nothing here is verified against the live service, and these features are not guaranteed to behave as described.
