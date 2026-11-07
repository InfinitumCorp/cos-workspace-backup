# LinkedIn native scheduled-post log

Updated 2026-11-07 04:02 MSK. Scope: approved personal TechPapers rows only; EchoForm was not touched. LinkedIn identity verified as William Aaron Turner. Native scheduler showed an empty queue before scheduling (Scheduled (0)). LinkedIn Help states scheduled times are converted to UTC based on device time-zone settings; box device reported MSK +0300. LinkedIn's confirmation and queue displayed 17:00 for each completed row.

## Verified scheduled

| Manifest row | Canonical key | Requested MSK time | Native confirmation / queue evidence | Native ID/URL |
|---|---|---|---|---|
| LI-02 (DR) | `179949703|personal|2026-11-09` | 2026-11-09 17:00 Europe/Moscow | Queue: Posting Mon, Nov 9, 2026 at 5:00 PM; image post and caption preview present | Not exposed in native queue UI |
| LI-06 (CCW) | `179983771|personal|2026-11-11` | 2026-11-11 17:00 Europe/Moscow | Queue: Posting Wed, Nov 11, 2026 at 5:00 PM; image post and caption preview present | Not exposed in native queue UI |
| LI-10 (CDH) | `179950632|personal|2026-11-13` | 2026-11-13 17:00 Europe/Moscow | Queue: Posting Fri, Nov 13, 2026 at 5:00 PM; image post and caption preview present | Not exposed in native queue UI |

Queue showed exactly three scheduled posts after LI-10. No same-canonical-asset, personal-channel, target-date duplicates were present when each was added. Each completed post used the manifest caption and matching local 1200×627 image; SHA-256 matched the manifest.

## Not scheduled

- LI-14 (DR), 2026-11-16 17:00 MSK: matching image attached; date/time set to 5:00 PM; scheduling submission returned LinkedIn error “We encountered a problem sharing your post.” Queue count remained 3 and no schedule confirmation appeared. Left in the composer; not scheduled and not retried.
- LI-18 (CCW), 2026-11-18 17:00 MSK: untouched.
- LI-22 (CDH), 2026-11-20 17:00 MSK: untouched.

The earlier `whatismytimezone.com` 403 was unrelated per clarification. LI-14 submission produced LinkedIn’s in-flow “We encountered a problem sharing your post” refusal; it was reported and no retry was made. No further scheduling or company-page discovery was performed. The user's computer is offline; browsing used the box network, not the user's computer.
