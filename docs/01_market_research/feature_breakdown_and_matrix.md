# Feature Breakdown & Product Matrix

This document defines the product taxonomy and detailed feature requirements for the AI Dating Assistant, organized into **Phase 1 (MVP Table Stakes)**, **Phase 2 (Differentiators & UX Enhancements)**, and **Phase 3 (Long-Term Moat & Advanced Intelligence)**.

---

## 1. Feature Taxonomy

```
AI Dating Assistant Features
├── 1. In-Conversation Assistance (Tactical)
│   ├── Multimodal Screenshot Reply Generator
│   ├── Contextual First-Message (Opener) Generator
│   ├── Multi-Tone Response Selectors (Flirty, Witty, Direct, Chill)
│   ├── iOS Third-Party Keyboard Extension
│   └── iOS Share-Sheet Quick Action
├── 2. Profile Doctor & Optimization (Strategic)
│   ├── Dating Profile Photo Review & Rating
│   ├── Prompt & Bio Optimizer (Hinge prompts, Tinder bio)
│   └── Red Flag & Cliché Eliminator
├── 3. Conversation Analytics & Intelligence
│   ├── Interest Level & "Ghosting Risk" Meter
│   ├── "Close-to-Date" CTA Recommendation
│   └── Topic Pivot Suggestions (when chat goes dry)
└── 4. Practice & Coaching (Interactive)
    ├── Mock Dating Simulator (Interactive Voice/Text Roleplay)
    ├── Custom Tone & Authenticity Mimicry
    └── In-Person Date Prep & Conversational Rules
```

---

## 2. Detailed Feature Breakdown

### Category 1: In-Conversation Assistance (Tactical Copilot)

#### 1.1 Multimodal Screenshot Reply Generator (Core MVP)
- **Description**: User uploads or pastes a screenshot from Tinder, Hinge, Bumble, WhatsApp, Instagram, or iMessage.
- **Processing**:
  - Automatically crops and detects dialogue bubbles.
  - Distinguishes between incoming message (Match) and outgoing message (User).
  - Understands conversational subtleties, emojis, sarcasm, and slang.
- **Output**: Generates **3 distinct response options**:
  1. *Safe & Witty*: Natural, clever banter with low cringe risk.
  2. *Flirty & Playful*: High energy, teasing, romantic tension.
  3. *Bold & Direct*: Steering toward setting up a date or exchanging numbers.

#### 1.2 Profile-Based Opener Generator
- **Description**: User screenshots the match's profile photos and prompts (e.g. Hinge "A shower thought I recently had...").
- **Output**: Generates unique, highly specific opening messages referencing details in their photos or prompts, achieving significantly higher response rates than generic "Hey" messages.

#### 1.3 iOS Keyboard Extension (`UIInputViewController`)
- **Description**: A custom keyboard integrated directly into the iOS system.
- **UX**:
  - The user stays inside Tinder or iMessage.
  - Switches to our keyboard.
  - Taps "Generate Reply" or pastes clipboard text.
  - One-tap insertion into the chat box.
- **Benefit**: Removes the annoying app-switching loop that plagues 90% of competitors.

---

### Category 2: Profile Doctor & Optimization

#### 2.1 AI Photo Rater & Auditor
- **Description**: Evaluates a user's dating profile photo deck.
- **Scoring Dimensions**:
  - Lighting, resolution, facial visibility (no sunglasses/hat obstruction).
  - Solo vs group photo balance (identifying the "Where's Waldo" problem).
  - Activity / lifestyle variety (hobbies, pets, travel, social proof).
- **Actionable Feedback**: Recommends order of photos, which photo to delete, and what types of photos are missing.

#### 2.2 Bio & Prompt Revamp
- **Description**: Transforms dry or cliché bios ("I love tacos, dogs, and travel") into intriguing, hook-filled profile bios customized for specific apps (Hinge vs Bumble vs Tinder).

---

### Category 3: Conversation Analytics & Date Closing

#### 3.1 Interest Level & "Ghosting Risk" Meter
- **Description**: Analyzes message length, reply frequency, and question-asking ratio to quantify the match's interest level on a scale of 0–100%.
- **Actionable Alert**: Warns user if they are over-texting, dry-texting, or if the conversation is entering the "friendzone" or "dead-end" danger zone.

#### 3.2 Date Closing Advisor
- **Description**: Identifies the optimal moment to transition from app chat to phone number exchange or first in-person date invitation.
- **Suggestions**: Generates low-pressure date proposals based on shared interests identified in the conversation (e.g., matcha, boba, speakeasy, art gallery).

---

### Category 4: Interactive Practice & Skill Building

#### 4.1 Mock Date Practice Simulator
- **Description**: An AI chat partner allowing users to practice flirting and banter in a safe, zero-judgment sandbox before messaging real matches.
- **Feedback**: After a 10-message exchange, the AI coach rates the user on charisma, conversational balance, and charm.

#### 4.2 Voice & Personality Mirroring
- **Description**: Analyzes past real texts sent by the user to learn their specific vocabulary, capitalization style, and humor, ensuring generated suggestions sound authentically like them.

---

## 3. Product Phase Matrix

| Feature | Phase 1: Feasibility & MVP | Phase 2: Growth & Retention | Phase 3: Advanced Moat |
|---|:---:|:---:|:---:|
| Screenshot-to-Reply (Vision AI) | **P0 (Must Have)** | Enhanced | Continuous Tuning |
| Multi-Tone Options | **P0 (Must Have)** | Customizable | Dynamic learning |
| In-App Photo Picker & Clipboard Paste | **P0 (Must Have)** | Optimized | Automatic sync |
| Profile Opener Generator | **P0 (Must Have)** | Multi-photo deck | Real-time scan |
| iOS Keyboard Extension | P1 (Fast Follow) | **P0 (Core USP)** | Cross-app presets |
| Profile Doctor & Photo Scorer | P2 | **P1 (High Priority)** | Benchmarking |
| Interest Meter & Date Closer | P2 | P1 | **P0** |
| Mock Date Simulator | P3 | P2 | **P1** |
| Android Client App | Post-iOS Launch | **P0 (Sprint 2)** | Feature Parity |
