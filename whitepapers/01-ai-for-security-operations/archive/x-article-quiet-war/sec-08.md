## Part IX: Illustrative scenarios

The three scenarios below are **illustrative and hypothetical**. They do not describe any real organization, client or incident. No figures in them are measured results. They exist to show how the ideas in this paper fit together in practice.



**Illustrative scenario A (hypothetical): The quiet administrator account**

*Setting.* A regional services company with about 600 staff and a three-person security team. Logs from domain controllers and the VPN are centralized. The team has piloted an AI assistant for log analysis, approved under its governance rules and limited to read-only access.

*What happens.* The assistant's weekly baseline summary notes that an IT administrator account has been signing in through the VPN at consistent times, but from an address range not seen before, and using built-in administrative tools on a file server where that account has not previously been active. No single alert fired. Every action stayed under existing thresholds.

*What the people do.* An analyst reviews the summary, checks the raw logs directly and confirms the pattern. She contacts the administrator by phone, using a number from the staff directory rather than one in an email. The administrator has not been working remotely. The team escalates to incident response, follows its plan, and the incident owner decides on containment steps.

*Lessons.* The assistant did not detect the intrusion. It surfaced a deviation from a baseline that only existed because logging was centralized. The person decided. Verification used an out-of-band channel, an influence-resistant habit. This is the threshold-management problem from Part I, met by baselines and judgment rather than by a single rule.





**Illustrative scenario B (hypothetical): The patch list nobody trusted**

*Setting.* A mid-size manufacturer with hundreds of open vulnerability findings and a long-standing argument between security and operations about what to patch first.

*What happens.* The security lead pilots AI-assisted prioritization. The tool combines KEV status, internet exposure and asset importance, and produces one ranked list per system owner, with a short explanation for each item. Two internet-facing remote-access appliances with KEV-listed vulnerabilities rise to the top. One is past its supported lifecycle.

*What the people do.* System owners review the lists. Operations flags one server that cannot be rebooted during a production run; the owner documents an exception with a compensating control and an expiry date. The appliances are patched within the week. Leadership approves a replacement plan for the end-of-life device.

*Lessons.* The value was not the score. It was a shared, explained list that owners could accept. The AI ranked; people approved. The team denied the adversary the cheapest route in, the asymmetric move discussed in Parts I and IV. The team now tracks time to remediate KEV-listed vulnerabilities as a board metric.





**Illustrative scenario C (hypothetical): The helpful assistant that read the wrong email**

*Setting.* A professional services firm uses an AI assistant to summarize reported phishing emails for its small security team. During the pilot, the assistant also had permission to add sender domains to a block list automatically.

*What happens.* A reported email contains hidden text crafted to manipulate any AI system that reads it. The assistant's summary describes the message as benign, and the instructions in the hidden text attempt to steer the assistant's output. Because the block-list permission existed, the team realizes that a similar message could have caused the assistant to take an unwanted action.

*What the people do.* An analyst notices the summary does not match the message's obvious signs of phishing. The team reviews the design under its governance rules, removes the assistant's ability to change the block list, and separates the summarizing function from any function that takes action. They add this case to analyst training and to the scope of their next authorized security test.

*Lessons.* This is prompt injection, the first risk on the OWASP 2025 list, meeting excessive agency. The fix was architectural, not heroic: reduce the tool's authority, keep a person between output and action, and test the workflow. Over-reliance would have missed it. A trained reviewer caught it.



Across all three scenarios, the pattern is the same. Fundamentals first. AI as an assistant to judgment, not a replacement for it. Clear authority. Measured results.
