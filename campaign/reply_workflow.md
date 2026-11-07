# Promo Reply Workflow – Infinitum Free 1-Week Pentest

**Trigger:** Someone replies to the promo email (Email 1 went to 147 contacts on Oct 26, 2026).
**Owner:** William Aaron Turner. **Nothing is sent to a client without William's approval.**

## Flow

1. **Reply lands** in William's mailbox (info@theinfinitumcorporation.com / his Gmail), watched by **EmailBot**.
2. **EmailBot** logs the reply in the Pipeline Tracker (status: New) and sends a short summary (sender, company, what they asked, link to thread) to:
   - **HackerBot**: technical qualification and scoping (real company? assets owned? scope doable in 1 week?)
   - **CoS**: tracking and coordination (tracker row, due dates, reminders)
3. **EmailBot drafts the reply** using template (a) "First reply" from the intake doc, and shows it to **William for approval**. Not interested or no capacity: use template (c).
4. **William approves** -> reply goes out with the intake doc link (target: within 4 business hours of the reply).
5. **Intake:** client completes the intake doc, including the signed authorization (Section 4). Status: Intake sent -> Intake signed. **No testing before the signature.**
6. **Kickoff** (within 2 days of signed intake): EmailBot sends template (b); HackerBot confirms scope, window, source IPs, emergency contacts.
7. **Testing** (HackerBot, inside the signed window only) -> **report delivered within the week** -> **debrief** -> **upsell/follow-up** (retest, paid engagement).
8. **CoS closes out** the row and handles data deletion/return per policy.

## Roles

| Bot | Responsibility |
|---|---|
| EmailBot | Watch inbox, log replies, draft client emails, send only after William approves |
| HackerBot | Qualification, scoping, testing, report, debrief |
| CoS | Tracker upkeep, deadlines, reminders, escalations to William |

## Statuses (tracker)

New -> Qualified -> Intake sent -> Intake signed -> Kickoff -> Testing -> Report delivered -> Closed

## Targets

- Reply to client within **4 business hours**
- Kickoff within **2 days** of signed intake
- Report within the 1-week engagement

## Escalate to William

Legal or authorization questions, third-party hosted targets, requests for DoS/social engineering/physical testing, anything that looks like a non-owner asking to test someone else's systems.

## Links

- Intake & Onboarding doc (Notion): https://app.notion.com/p/40558b84599a81d4af0cee0a7e5c680b
- Pipeline Tracker (Google Sheet): https://docs.google.com/spreadsheets/d/1-aciOcce67mMkMk6FN67i7Tu2yJHLrVAiogefpKmAB0/edit
