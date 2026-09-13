# Feature Analysis & Strategic Prioritization: AI Dating Assistant

## Executive Summary: The Product Thesis

Most AI dating apps in the market (e.g. RIZZ, WingAI, Plug AI) suffer from a critical product deficiency: **high initial novelty, followed by rapid churn within 2 to 4 weeks**. 

Users download the app during a moment of texting panic, use it to get 2–3 witty replies, and then abandon it because:
1. The replies feel **repetitive, cheesy, or robotic** ("Doesn't sound like me").
2. The workflow of **switching back and forth** between dating apps and the assistant to upload screenshots is too cumbersome.
3. The app is purely **reactive** (answering "what do I say next?" based on 1 screenshot), completely missing **long-term conversation context, inside jokes, and deep profile nuances**.
4. Profiles and chats are long (often 5–6 screens or 30+ messages), making multi-screenshot capture painful and cluttering the Camera Roll.

To build a category-defining, defensible product, our feature architecture implements a **Dual-Ingestion Pipeline** (Quick Screenshot + ReplayKit Continuous Scroll Broadcast) paired with a **Whole-Profile Multi-Hook Discovery Engine** and **Native iOS Keyboard Extension**.

---

## 1. The Dual-Ingestion Input Architecture

To make the app truly frictionless, we eliminate the multi-screenshot bottleneck by providing two specialized ingestion channels:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                             DUAL-INGESTION INPUT ARCHITECTURE                               │
├──────────────────────────────────────────────┬──────────────────────────────────────────────┤
│ Channel 1: Quick Screenshot & Clipboard      │ Channel 2: ReplayKit Continuous Scroll       │
├──────────────────────────────────────────────┼──────────────────────────────────────────────┤
│ • Best for: Instant single-screen replies    │ • Best for: Full profiles (6 photos/prompts) │
│ • Friction: Zero-tap clipboard auto-detect   │ • Best for: Long existing chats (30-50 msgs) │
│ • Storage: 1 image or pasted text            │ • Best for: Training "Sound Like Me" style   │
│ • Flow: In-app picker or iOS Keyboard        │ • Storage: ZERO photos in Camera Roll        │
│                                              │ • Flow: 3-sec Control Center scroll broadcast│
└──────────────────────────────────────────────┴──────────────────────────────────────────────┘
```

### Channel 1: Quick Screenshot & Clipboard Detection (Fast Tactical Replies)
- **Mechanism**: The user takes a standard single screenshot or copies text.
- **UX**: When opening our app or switching to our custom iOS keyboard, the app instantly recognizes the image/text in `UIPasteboard` and offers one-tap reply suggestions.

### Channel 2: ReplayKit Continuous Scroll Broadcast (Deep Ingestion)
- **Mechanism**: An iOS Broadcast Upload Extension (`RPBroadcastSampleHandler`).
- **UX Flow**:
  1. User is in Hinge, Tinder, iMessage, or WhatsApp.
  2. Swipes down Control Center → long-presses Screen Recording → selects **"Dating Assistant"** → taps **Start Broadcast**.
  3. Scrolls smoothly through the profile or chat thread (3 to 5 seconds).
  4. Taps red status bar to finish.
- **On-Device Keyframe Extraction (Zero AI Token Cost)**:
  - The extension runs 100% locally on the iPhone using Apple’s `VNTranslationalImageRegistrationRequest` (Vision framework).
  - Measures vertical scroll translation (`delta Y`) in real time (~2ms per frame).
  - Samples a crisp static keyframe every ~700–800 pixels of vertical travel, discarding motion-blurred frames.
  - Extracts **4 to 8 non-overlapping, high-resolution still images**.
  - **AI Token Cost**: **$0.00 spent on video processing**. The static frames are batched into a single multimodal call to Gemini 1.5 Flash (costing `< $0.0005`).
- **Three Breakthrough Applications of ReplayKit**:
  1. **Full Profile Dossier**: Scans all 6 photos, prompt answers, Spotify anthems, and bio in one continuous scroll.
  2. **Long Existing Chat Ingestion**: Ingests 30–50 previous messages from iMessage or WhatsApp. The AI understands relationship history, callbacks, and inside jokes before suggesting the next move.
  3. **"Sound Like Me" Style Calibration**: The user scrolls through an authentic past chat with friends/crushes. The AI analyzes their capitalization, emoji habits, slang, and message length to calibrate their personal texting voice without manual surveys.

---

## 2. Whole-Profile Multi-Hook Discovery: The "Banter Strategy Board"

Instead of dumping 3 generic lines, the AI acts as a **social detective**. It evaluates the entire profile and presents the user with an organized **Menu of Hooks & Angles**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ MATCH PROFILE ANALYSIS: Chloe, 25 (Hinge)                                   │
│ "Found 3 high-probability banter hooks across her profile"                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🎯 HOOK 1: The "I have an irrational fear of pigeons" Prompt                │
│    (High humor, safe playfulness)                                           │
│    • [Witty]  "I was going to say hello, but I needed to make sure you're   │
│               not currently surrounded by birds first."                     │
│    • [Tease]  "Duly noted: our first date will not be in Central Park."     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🎯 HOOK 2: The Vintage Film Camera in Photo #3                              │
│    (Niche interest, shows genuine observation)                              │
│    • [Curious] "Is that an Olympus 35mm or did you borrow it for the aesthetic?"│
│    • [Flirty]  "Great taste in cameras. Tell me you actually shoot film."   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🎯 HOOK 3: Her Dog with the Head Tilt in Photo #1                           │
│    (Warm, conversational)                                                   │
│    • [Direct] "Your dog looks like he gives great relationship advice.      │
│               Did he approve this match?"                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Why this wins**:
- Eliminates user anxiety over *what* to talk about.
- Provides 2–3 tone choices under each hook (Witty, Flirty, Direct).
- Ensures 100% contextual specificity, drastically increasing response rates.

---

## 3. Comprehensive Feature Evaluation Matrix (RICE + Kano)

```
+----+-----------------------------------------+-----------------+-----------+--------+--------+-------+--------+------------+-------------------------------------+
| ID | Feature Name                            | Category        | Kano Type | Reach  | Impact | Conf. | Effort | RICE Score | Recommendation                      |
+----+-----------------------------------------+-----------------+-----------+--------+--------+-------+--------+------------+-------------------------------------+
| F01| Multimodal Screenshot Reply Gen         | Tactical Chat   | Must-Have | 10     | 3.0    | 95%   | 3.0    | **9.50**   | **P0: Core MVP Launch**             |
| F02| Multi-Tone Selector (Witty/Flirty/Direct)| Tactical Chat  | Must-Have | 10     | 2.5    | 95%   | 2.0    | **11.88**  | **P0: Core MVP Launch**             |
| F03| Whole-Profile Multi-Hook Discovery      | Strategic Chat  | Delighter | 9      | 3.0    | 90%   | 3.5    | **6.94**   | **P0: Core MVP Launch**             |
| F04| Clipboard Auto-Detect on Launch         | UX / Speed      | Delighter | 8      | 2.0    | 90%   | 1.5    | **9.60**   | **P0: Core MVP Launch**             |
| F05| Anti-Cringe & Safety Filter             | AI Quality      | Must-Have | 10     | 2.5    | 85%   | 2.0    | **10.63**  | **P0: Core MVP Launch**             |
| F06| "Sound Like Me" Voice Customizer        | Personalization | Delighter | 8      | 3.0    | 85%   | 3.0    | **6.80**   | **P0: Core MVP Launch**             |
| F07| iOS Custom Keyboard Extension           | Workflow        | Perform.  | 9      | 3.0    | 80%   | 6.0    | **3.60**   | **P0: Core MVP Launch**             |
| F08| ReplayKit Scroll Broadcast (Profiles)   | Deep Ingestion  | Delighter | 8      | 3.0    | 85%   | 4.5    | **4.53**   | **P0: Core MVP Launch**             |
| F09| Long Existing Chat Ingestion (ReplayKit)| Context AI      | Delighter | 7      | 3.0    | 80%   | 3.5    | **4.80**   | **P0: Core MVP Launch**             |
| F10| Date Closing & Transition Advisor       | Coaching        | Perform.  | 7      | 2.5    | 80%   | 3.0    | **4.67**   | **P1: Phase 1.5 Update**            |
| F11| Dating Profile Photo Auditor & Scorer   | Profile Doctor  | Perform.  | 6      | 2.5    | 85%   | 4.0    | **3.19**   | **P1: Phase 1.5 Update**            |
| F12| Bio & Prompt Revamp Engine              | Profile Doctor  | Perform.  | 7      | 2.0    | 90%   | 2.5    | **5.04**   | **P1: Phase 1.5 Update**            |
| F13| Discreet / Camouflage App Mode          | Privacy / UX    | Delighter | 5      | 1.5    | 95%   | 1.0    | **7.13**   | **P1: Phase 1.5 Update**            |
| F14| Conversation Health & Ghosting Meter    | Analytics       | Delighter | 6      | 1.5    | 75%   | 3.5    | **1.93**   | **P2: V2.0 Roadmap**                |
| F15| Interactive Mock Date Simulator (Text)  | Gamification    | Delighter | 4      | 2.0    | 80%   | 5.0    | **1.28**   | **P2: V2.0 Roadmap**                |
| F16| Voice Call Practice Simulator           | Advanced AI     | Delighter | 3      | 2.0    | 70%   | 8.0    | **0.53**   | **P3: Long Term**                   |
| F17| Automated Swiping & Chatting Bot        | Automation      | Unsafe    | 4      | 2.5    | 20%   | 9.0    | **0.22**   | **DO NOT BUILD (High Ban Risk)**     |
+----+-----------------------------------------+-----------------+-----------+--------+--------+-------+--------+------------+-------------------------------------+
```

---

## 4. The Anti-Roadmap: What We Will NOT Build

1. **Automated Swiping & Auto-Chatting Bots (CupidBot Model)**:
   - Violates Tinder/Bumble Terms of Service and Apple App Store Guideline 5.6.
   - Leads to immediate device and phone number bans for users, plus guaranteed App Store rejection.
2. **Heavy On-Device AI Models inside the Keyboard Extension**:
   - iOS enforces a strict ~30MB RAM limit on keyboard extensions. On-device LLMs will trigger instant OS termination.
3. **Deceptive Paywalls with No Free Tier**:
   - Competitors charging $9.99/week with no free usage suffer 40%+ 1-star reviews. We maintain a generous 5 free daily credits to drive viral word-of-mouth.

---

## 5. Phased Product Scope Summary

```
Phase 1: iOS MVP Scope (Sprint 1)
├── [Core Ingestion] Quick Screenshot & Clipboard Auto-Detection
├── [Deep Ingestion] ReplayKit Continuous Scroll Broadcast (Zero Gallery Clutter)
├── [Intelligence] Whole-Profile Multi-Hook Discovery (Banter Strategy Board)
├── [Context AI] Long Existing Chat Ingestion (Scroll past 30+ messages)
├── [Personalization] "Sound Like Me" Voice Customizer (Learns via real chat scroll)
├── [Workflow] Native iOS Custom Keyboard Extension (UIInputViewController)
├── [AI Quality] Anti-Cringe & Moderation Guardrails
└── [Monetization] StoreKit 2 Transparent Subscriptions + 5 Free Daily Credits

Phase 2: Strategic Coaching & Profile Doctor (v1.1 - v1.2)
├── [Coaching] Date Closing & "Ask Out" Timing Advisor
├── [Profile Doctor] 6-Photo Batch Photo Scorer (Lighting, Smile, Group Balance)
├── [Profile Doctor] Bio & Hinge Prompt Revamp Engine
└── [Privacy] Discreet Home Screen Camouflage Mode

Phase 3: Cross-Platform & Advanced Intelligence (v2.0)
├── [Android] Native Android App & Floating Bubble Overlay
├── [Gamification] Interactive Text-Based Mock Date Simulator
└── [Analytics] Conversation Health & Ghosting Risk Meter
```
