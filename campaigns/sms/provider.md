# SMS provider comparison (prices checked Nov 7, 2026 from provider pages)
List: 1,049 US numbers x 3 messages x 1 segment = ~3,147 outbound segments.

| | Twilio | Telnyx | SimpleTexting |
|---|---|---|---|
| Per SMS segment | $0.0083 + carrier fee ($0.0035 AT&T / $0.0045 T-Mobile / $0.005 Verizon) | $0.004 + carrier fee ($0.003 AT&T/T-Mobile, $0.0045 Verizon) | Credits: $29/mo for 500 (toll-free) or $39/mo local 10DLC; extra credits 5.5¢ |
| 10DLC brand | $4.50 (Low Volume Standard) | $4.50 | $4 one-time |
| Campaign | $15 vetting + $1.50/mo (Low Volume Mixed) | $15 review + $1.50/mo (first 3 months billed upfront) | included / guided |
| Number | ~$1.15/mo local | ~$1/mo (verify at signup) | $10/mo local (toll-free included) |
| Est. total for this campaign | ~$62 | ~$50 | ~$190 (500-credit plan + ~2,650 extra credits; a larger tier may be cheaper — check calculator) |
| Ease | API/console; needs a sending tool or script | API; needs script | No-code web app, contact upload, scheduling, STOP built in |

Sources: twilio.com/en-us/sms/pricing/us; help.twilio.com A2P 10DLC fees; telnyx.com/pricing/messaging; support.telnyx.com 10DLC fees; simpletexting.com/pricing.

## Registration & timelines
- **10DLC (local number):** Brand (EIN, legal name, address) + Campaign (use case, sample messages, opt-in description, privacy/terms URLs). Telnyx states carrier review typically ~72 business hours after their internal review; Twilio commonly days to weeks. Unregistered 10DLC traffic is blocked.
- **Toll-free:** toll-free verification required before sending; SimpleTexting says "typically 1-3 days", up to a week.
- Opt-in description must be truthful: consent from a 2018 list (see compliance.md). Carriers may reject a campaign whose consent can't be shown. Registration also wants a live website with privacy policy — website work is currently paused for the new site.

## Is Monday Nov 9 realistic?
**No, not for a compliant send.** Registration submitted Sat/Sun would at best clear mid-to-late next week. Realistic first send: ~Nov 12–18 after approval.

## Recommendation
**SimpleTexting** if William wants to run it himself without code (cost ~$190, still under $200), or **Telnyx** (~$50) if a bot runs sends via API. My pick: **Telnyx** for cost, with a send script + STOP handling built in; Twilio is the fallback (~$62, more docs/support).

---
# FREE / near-free options (researched Nov 7, 2026) — need: 1,049 × 3 = 3,147 texts

| Option | What's free | Real cost for 3,147 | Limits / registration |
|---|---|---|---|
| Twilio trial | 100 SMS, 30 days | Can't do it free | Trial sends only to ≤5 **verified** recipients — useless for a list. [twilio.com/docs/usage/trials] |
| Telnyx trial | $5 credit | Can't do it free | Only 1 verified destination, 100 msgs/day. Paid: ~$50 (see above). [developers.telnyx.com …/trial] |
| Textbelt | 1 free SMS/day | ~$0 would take 8.6 years; paid quota otherwise | Free key = 1/day. [docs.textbelt.com] |
| Textedly | Free trial, 50 texts | $79/mo Plus (2,000) + overage, or $125 Enterprise (3,500) + $8/mo telecom + $4–44 10DLC | 14-day trial. [textedly.com/pricing] |
| EZ Texting / SlickText / SimpleTexting | 14-day trials, ~50–120 texts | ~$45–190 | Registration still required. [christopholivierconsulting.com/sms-marketing-platforms] |
| Brevo SMS | None | ~$10.90/1,000 US → **~$34** + carrier/number fees (unverified) | Sender registration required. [emailvendorselection.com/sms-marketing-pricing] |
| Omnisend | Free plan = email only | US SMS $0.009 → **~$28** + plan/number/registration (not stated on page) | US/Canada. [christopholivierconsulting.com] |
| Klaviyo | Free plan: $5 of SMS/mo | Covers only a few hundred texts at most; paid for the rest | Registration needed. [same] |
| WhatsApp Business | 1,000 free service replies/mo | **Can't be done** | Meta has not delivered marketing templates to US numbers since Apr 1, 2025. [developers.facebook.com WhatsApp pricing; manysetter.com] |
| RCS | none | Same per-message pricing as SMS (Twilio RCS ≥ $0.0083 + carrier fees), plus brand verification | Not free. [twilio.com/en-us/sms/pricing/us] |
| Android phone + bulk SMS app | $0 on an unlimited plan | $0 in cash | **Not legitimate:** carrier terms ban commercial/bulk messaging on consumer lines. Unregistered mass texts get filtered and the line suspended. Consent rules (TCPA/CTIA) still apply. Not recommended. |

**Toll-free verification:** there's no fee at most providers (SimpleTexting includes it). You still pay for the number and messages, and approval takes 1–3 days, up to a week.

## Verdict
- **A truly $0 compliant send to 1,049 people is not possible.** Every free tier is capped at ≤120 texts or limited to verified recipients, and WhatsApp marketing doesn't reach US numbers.
- **Cheapest legitimate options:**
  - Omnisend (~$28 in message fees) or Brevo (~$34). Their number and registration fees aren't stated, so confirm them at signup.
  - **Telnyx, ~$50 all-in with published fees.** This is the most certain low cost.
- Registration (10DLC or toll-free verification) is required on every option.
