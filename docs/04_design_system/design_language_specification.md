# Design Language Specification: Spatial Sunset Glass

## 1. Design Vision & Philosophy

Our design language, **"Spatial Sunset Glass"**, represents a deliberate synthesis of two complementary design philosophies:

1. **Apple Spatial Glass (Structural Foundation - Concept 4)**:
   - Native iOS 17/18 liquid glassmorphism, multi-layer translucent frosted cards, subtle specular edge highlights, and strict adherence to Apple Human Interface Guidelines.
   - *Purpose*: Solves the "cheap AI toy" problem. Gives the app the credibility, trust, and polish of a built-in, first-party Apple utility.

2. **Warm Sunset Haze (Emotional Aura - Concept 5)**:
   - Rich golden-hour amber, sunset coral, and deep velvet plum tones.
   - *Purpose*: Solves the "cold robot" problem. Infuses the app with the emotional warmth, romance, and charm that users naturally seek in dating.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      "SPATIAL SUNSET GLASS" ARCHITECTURE                     │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ Structural Foundation                │ Emotional Aura                       │
│ (Apple Spatial Glass)                │ (Warm Sunset Haze)                   │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ • SwiftUI `.ultraThinMaterial` glass │ • Deep velvet plum background canvas │
│ • 1px translucent specular borders   │ • Sunset coral & golden amber glow   │
│ • Floating bento card layouts        │ • Warm ivory typography (#FFF9F2)    │
│ • Fluid iOS spring haptics           │ • Charismatic, romantic mood         │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

---

## 2. Color Palette & Token System

### Base Canvas (Dark-Mode Native)
- **Background Primary**: `#141018` (Deep Velvet Plum)
- **Background Secondary**: `#1D1724` (Elevated Midnight Plum)
- **Glass Card Fill**: `rgba(255, 255, 255, 0.06)` with background blur (`.ultraThinMaterial`)
- **Card Border**: `rgba(255, 255, 255, 0.12)` (1px hairline stroke with subtle top specular highlight)

### Romantic Accent System
- **Sunset Coral (Primary CTA)**: `#FF6565`
- **Golden Amber (Highlight & Energy)**: `#FFA24C`
- **Gradient Primary**: `LinearGradient(from: #FF6565, to: #FFA24C)` (Used for main action buttons and active indicators)
- **Subtle Ambient Radial Glow**: `rgba(255, 101, 101, 0.15)` blurred behind active match cards

### Typography Colors
- **Text Primary**: `#FFF8F0` (Warm Ivory - avoids harsh cold pure white)
- **Text Secondary**: `#B8B0C0` (Muted Mauve Gray)
- **Text Tertiary / Metadata**: `#7A7285` (Subtle Slate)

---

## 3. Typography & Micro-Interactions

- **Display & Headings**: `SF Pro Rounded` (Bold / SemiBold) — provides friendly, approachable warmth.
- **Body & Dialogue Text**: `SF Pro` (Regular / Medium) — ensures maximum readability for chat messages.
- **Tone Pill Badges**:
  - *Witty*: Amber glow pill (`#FFA24C`)
  - *Flirty*: Coral glow pill (`#FF6565`)
  - *Direct*: Warm gold pill (`#FFD166`)
- **Haptic Feedback**: Standard iOS tactile feedback (`UIImpactFeedbackGenerator(style: .light)`) on selecting hooks and copying openers.

---

## 4. Why This Wins Against Competitors

| Competitor Pattern | Their Problem | Our "Spatial Sunset Glass" Solution |
|---|---|---|
| **RIZZ / Plug AI** | Harsh neon green on pitch black; feels like a gaming or crypto app. | Sophisticated velvet plum and warm sunset tones; feels mature and stylish. |
| **WingAI** | Cluttered purple casino cards with hot pink fire emojis. | Clean Apple bento glass with restrained, high-status hierarchy. |
| **ChatGPT / Generic LLMs** | Cold, utilitarian black-and-white chat UI. | Warm romantic aura that sets a relaxed, flirtatious mood. |
