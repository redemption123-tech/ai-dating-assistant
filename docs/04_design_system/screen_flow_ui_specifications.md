# Screen-by-Screen UI Specification & Mockup Gallery

This document specifies the complete 20-screen user journey for the AI Dating Assistant app, rendered in the **Spatial Sunset Glass** design system (deep velvet charcoal `#131217`, soft golden-amber edge backlight, dark frosted liquid glass cards, and glowing sunset coral-orange buttons `#FF6B50`).

---

## Visual Mockup Index (11 Rendered Core Screens)

| Screen # | Screen Name | Visual Mockup File | Core Functional Elements |
|---|---|---|---|
| **01/02** | **Landing & Welcome** | [`07_screen_landing_welcome.jpg`](../assets/designs/07_screen_landing_welcome.jpg) | Glowing Amura brand, value props, "Get Started" CTA |
| **04** | **Login & Auth** | [`08_screen_login_auth.jpg`](../assets/designs/08_screen_login_auth.jpg) | Sign in with Apple, Google Sign-In, "Try as Guest", zero-retention privacy badge |
| **05** | **Voice Calibration** | [`15_screen_voice_calibration.jpg`](../assets/designs/15_screen_voice_calibration.jpg) | "Sound Like Me": casing style, humor vibe slider, emoji frequency |
| **06** | **Extension Setup Guide** | [`16_screen_extension_setup.jpg`](../assets/designs/16_screen_extension_setup.jpg) | Step 1 (Keyboard Enable + Allow Full Access), Step 2 (Control Center tile) |
| **07** | **Main Home Dashboard** | [`09_screen_home_dashboard.jpg`](../assets/designs/09_screen_home_dashboard.jpg) | "5 Free Rizzes Left" counter, Analyze/Paste buttons, Active Matches carousel, Tab Bar |
| **08** | **Matches List (CRM)** | [`17_screen_matches_list.jpg`](../assets/designs/17_screen_matches_list.jpg) | Search, Hinge/Tinder/Bumble filters, match status badges (Deepening, Date Set) |
| **13** | **Banter Strategy Board** | [`10_screen_strategy_board.jpg`](../assets/designs/10_screen_strategy_board.jpg) | Sarah (26) profile header, multi-hook cards (Sourdough, Film Camera), categorized openers |
| **14** | **In-Chat Reply Suggester** | [`11_screen_chat_reply.jpg`](../assets/designs/11_screen_chat_reply.jpg) | Chat bubble preview, 3 ranked replies (Witty, Flirty, Direct), tone slider |
| **15** | **Match Dossier & Memory** | [`12_screen_match_dossier.jpg`](../assets/designs/12_screen_match_dossier.jpg) | Stage pill, Key Facts, Inside Jokes/Callbacks, "Next Strategic Move" draft invite |
| **19** | **iOS Keyboard Extension** | [`13_screen_keyboard_extension.jpg`](../assets/designs/13_screen_keyboard_extension.jpg) | Active match pill (Sarah • Hinge), Suggest Reply, Opener, Vibe buttons in iMessage |
| **20** | **Paywall & Subscription** | [`14_screen_paywall_subscription.jpg`](../assets/designs/14_screen_paywall_subscription.jpg) | Amura Pro benefits, Annual ($49.99/yr) vs Weekly ($7.99/wk), 3-day free trial CTA |

---

## Detailed Specifications for Remaining Specialized Screens

### Screen 11: Quick Ingestion & Upload Modal (Action Sheet)
- **Component**: SwiftUI floating bottom sheet (`.presentationDetents([.medium])`).
- **Layout**:
  - Auto-detected clipboard card: If a screenshot is in the pasteboard, displays a small 60x60 thumbnail with text: *"Screenshot detected from Hinge — Analyze now?"*.
  - Secondary options: *"Choose from Photos"* (`PhotosPicker`) and *"Start Continuous Scroll Broadcast"*.
- **Styling**: Frosted glass card with glowing amber rim.

### Screen 12: ReplayKit Scroll Processing Modal
- **Component**: Transient modal shown immediately after a ReplayKit broadcast ends.
- **Layout**:
  - Horizontal filmstrip showing 4 extracted keyframes (Header, Prompts, Photos, Bio).
  - Status indicator: *"Processing profile with Gemini Vision... (0.8s)"*.
  - Transition: Automatically slides into the **Banter Strategy Board** (Screen 13).

### Screen 16: Match Chat History Timeline View
- **Component**: Dedicated child view accessible by tapping a match in the Dossier (Screen 15).
- **Layout**:
  - Reverse chronological message bubbles showing:
    - Messages received from the match.
    - Suggestions provided by Amura (marked with a subtle sparkle icon).
    - What the user actually sent.
  - Floating bottom bar: *"Suggest Next Reply"* or *"Propose Date"*.

### Screen 17: Profile Doctor (6-Photo Deck Scorer)
- **Component**: Tab 3 sub-module.
- **Layout**:
  - 2x3 grid of user photo cards.
  - Overlay badges: `#1 Lead Photo (9.4★)`, `Good Smile (8.8★)`, `Low Light Warning (6.2★)`.
  - Action card: *"Re-rank photos: Move Photo 4 to slot 2 for +25% match rate"* with glowing coral CTA *"Apply Order"*.

### Screen 18: Bio & Prompt Revamp Studio
- **Component**: Tab 3 sub-module.
- **Layout**:
  - Segmented control: `Hinge Prompts` | `Tinder Bio` | `Bumble Bio`.
  - Text editor field: *"Enter your current prompt or draft thoughts..."*.
  - Output cards: 3 rewritten versions (*Witty & Self-Deprecating*, *Mysterious & Bold*, *Conversation Hook*).

### Screen 10: Settings & Account Management
- **Component**: Tab 4.
- **Layout**:
  - Profile header: User name and current plan (`Amura Pro Active`).
  - Section 1: *Preferences* (Default tone, Voice calibration shortcut).
  - Section 2: *App Customization* (Discreet App Icon switcher: Amura, Notes, Calculator).
  - Section 3: *Legal & Data* (Terms, Privacy Policy, Restore Purchases).
  - Danger Zone: Red text button *"Delete Account & Wipe All Match Data"*.
