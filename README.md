# AI Dating Assistant (iOS & Android)

An intelligent, privacy-first AI dating copilot designed to empower modern daters with contextual conversation assistance, profile optimization, and actionable dating coaching.

Starting with **iOS-first**, this repository documents the end-to-end product lifecycle—commencing with feasibility assessment, market sizing, competitive intelligence, architecture design, and implementation.

---

## Project Structure

```
ai-dating-assistant/
├── README.md
├── .gitignore
├── docs/
│   ├── 01_market_research/
│   │   ├── market_overview_and_size.md
│   │   ├── competitive_landscape.md
│   │   ├── feature_breakdown_and_matrix.md
│   │   └── user_pain_points_and_opportunities.md
│   ├── 02_feasibility_study/
│   │   ├── technical_feasibility_ios.md
│   │   ├── ai_architecture_and_cost.md
│   │   ├── app_store_compliance_and_privacy.md
│   │   └── feasibility_verdict_and_recommendations.md
│   ├── 03_feature_analysis/
│   │   └── feature_prioritization_and_selection.md
│   ├── 04_design_system/
│   │   └── design_language_specification.md
│   └── assets/
│       └── designs/
├── app/                  # iOS (SwiftUI) & Future Android Client
├── backend/              # AI Orchestration & API Gateway
└── scripts/              # Research scripts and utilities
```

---

## Phases of Development

1. **Phase 0: Feasibility & Market Validation (Completed)**
   - App Store & Google Play Store competitive teardown.
   - Sizing TAM / SAM / SOM and consumer willingness to pay.
   - Technical feasibility analysis for iOS (Keyboard Extension vs In-App / Share Sheet).
   - AI pipeline, token cost modeling, and latency validation.
   - App Store Review Guidelines (Guideline 4.0 & 5.1.1) compliance plan.

2. **Phase 1: Feature Prioritization & Strategy (Current)**
   - RICE scoring and Kano classification across 16 candidate features.
   - MVP scope definition (iOS Native App + Keyboard Extension).
   - Anti-roadmap formulation (features to avoid).

3. **Phase 2: iOS Proof of Concept (PoC)**
   - Multimodal chat screenshot analyzer.
   - Dynamic tone adjustment engine (witty, bold, flirty, casual).
   - Local on-device OCR + fast Vision LLM pipeline (<1.2s response time).

4. **Phase 3: MVP Product & iOS Keyboard Extension**
   - Native iOS App (SwiftUI).
   - Custom iOS Keyboard Extension (`UIInputViewController`) for inline replies.
   - Profile doctor & opening line generator.
   - StoreKit 2 monetization (Free trial + weekly/yearly subscription).

5. **Phase 4: Android Expansion & Advanced Coaching**
   - Android client & Accessibility/Overlay integration.
   - Audio roleplay / mock date simulator.
   - Safety & ghosting predictor.

---

## Documentation Index

- [Market Overview & Sizing](docs/01_market_research/market_overview_and_size.md)
- [Competitive Landscape (iOS & Android)](docs/01_market_research/competitive_landscape.md)
- [Feature Matrix & Taxonomy](docs/01_market_research/feature_breakdown_and_matrix.md)
- [User Reviews, Pain Points & Sentiment](docs/01_market_research/user_pain_points_and_opportunities.md)
- [iOS Technical Feasibility & Extension Architecture](docs/02_feasibility_study/technical_feasibility_ios.md)
- [AI Vision Pipeline, Latency & Cost Modeling](docs/02_feasibility_study/ai_architecture_and_cost.md)
- [App Store Compliance, Safety & Privacy](docs/02_feasibility_study/app_store_compliance_and_privacy.md)
- [Feasibility Verdict & Strategic Recommendations](docs/02_feasibility_study/feasibility_verdict_and_recommendations.md)
- [Feature Analysis, RICE Prioritization & MVP Scope](docs/03_feature_analysis/feature_prioritization_and_selection.md)
- [Design Language Specification (Spatial Sunset Glass)](docs/04_design_system/design_language_specification.md)
