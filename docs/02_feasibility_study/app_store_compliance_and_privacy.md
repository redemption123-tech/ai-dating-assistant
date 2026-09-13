# App Store Compliance, Privacy & Safety Feasibility

Navigating Apple's App Store Review Guidelines and Google Play Developer Policies is one of the most critical feasibility factors for an AI Dating Assistant. This document details the compliance architecture required to ensure frictionless app approval and high user trust.

---

## 1. Key Apple App Store Review Guidelines & Mitigations

```
+-----------------------------------------------------------------------------------------+
| Apple App Store Review Guidelines Risk Matrix                                           |
+-------------------+-------------------------------------+-------------------------------+
| Guideline         | Risk Description                    | Our Compliance Strategy       |
+-------------------+-------------------------------------+-------------------------------+
| **Guideline 4.0** | Apps that are simple repackaging of | Deep native utility: custom   |
| (Design / Minimum | a public API (e.g., generic ChatGPT | keyboard, photo scorer,       |
| Functionality)    | wrapper) face rejection.            | conversation health metrics.  |
+-------------------+-------------------------------------+-------------------------------+
| **Guideline 5.1.1**| Screenshots contain private chats, | In-memory processing only;    |
| (Data Collection  | names, and photos of third parties  | zero data retention policy;   |
| & Privacy)        | without explicit consent.           | client-side PII scrubbing.    |
+-------------------+-------------------------------------+-------------------------------+
| **Guideline 3.1.2**| Deceptive auto-renewing subscriptions| Transparent paywalls with clear|
| (Subscriptions &  | and misleading "Free" trial claims. | terms, easy restore & cancel  |
| Monetization)     |                                     | links, and honest pricing.    |
+-------------------+-------------------------------------+-------------------------------+
| **Guideline 1.2** | Generation of abusive, sexually     | System prompt guardrails,     |
| (User-Generated   | explicit, or harassing content.     | automated moderation filter,  |
| Content / Safety) |                                     | flag/report mechanism.        |
+-------------------+-------------------------------------+-------------------------------+
```

### Deep Dive: Guideline 5.1.1 (Privacy of Third-Party Chat Data)
- **The Challenge**: Users upload screenshots of conversations featuring other people (their dating matches). If these images or names are permanently saved or indexed, it raises GDPR, CCPA, and Apple App Store compliance red flags.
- **Our Architectural Solution**:
  1. **Zero Data Retention**: The server processes the image in volatile RAM, extracts conversational context, invokes the LLM, and immediately discards the image buffer. No image is written to disk or S3 buckets.
  2. **Client-Side Name / PII Anonymization**: The client or backend automatically scrubs phone numbers, handles, and addresses before sending context to LLMs.
  3. **Privacy Nutrition Label**: On App Store Connect, declare that User Content is collected strictly for app functionality and **Not Linked to Identity**.

### Deep Dive: Guideline 3.1.2 (Subscription Transparency)
- **The Challenge**: Apple actively rejects apps with confusing or dark-pattern paywalls (e.g. tiny cancel buttons, hidden pricing details).
- **Our Solution**:
  - Clear billing cadence: "$7.99 per week after 3-day free trial" displayed in prominent typography.
  - Direct links to **Terms of Service**, **Privacy Policy**, and **Manage Subscription**.
  - Provide a transparent Free Tier so users can test before buying.

### Deep Dive: Guideline 1.2 & Safety Moderation
- **The Challenge**: Flirting can occasionally cross into harassment, non-consensual sexual content, or hate speech.
- **Our Solution**:
  - Layered content moderation: Apply automated text safety filters (e.g., Google Content Safety / OpenAI Moderation API).
  - Explicit prompt instructions forbidding sexually explicit, threatening, or coercive suggestions.
  - Age rating set to **17+ (Infrequent/Mild Sexual Content and Nudity)** to ensure zero friction with Apple's age categorization.

---

## 2. Google Play Policy Alignment (For Future Android Phase)

When expanding to Android in Phase 2:
1. **Accessibility Service Restrictions**: Google strictly regulates Accessibility Services and bans apps from using them to scrape or monitor other apps unless intended for users with disabilities. We will **NOT** use Accessibility Services; instead, we will use Android's **Picture-in-Picture / Floating Bubble (Overlay Permission)** where the user explicitly taps to capture their screen.
2. **Foreground Services & Screenshot Capture**: Use Android's standard `MediaProjection` API with clear user consent.

---

## 3. Compliance Verdict

The project is **COMPLIANT & FULLY FEASIBLE** provided:
- The zero-retention privacy policy is clearly posted and implemented.
- StoreKit 2 paywalls adhere strictly to Apple's design guidelines without dark patterns.
- The app offers differentiated native utility (SwiftUI Keyboard + coaching) beyond a basic API wrapper.
