# Technical Feasibility Study: iOS Platform Architecture

## Executive Feasibility Verdict: FEASIBLE WITH SPECIFIC ARCHITECTURAL CONSTRAINTS

Developing an AI Dating Assistant for iOS is technically feasible, proven by commercial applications in production. However, Apple's strict iOS security sandboxing, App Extension memory limits, and privacy restrictions dictate specific architectural trade-offs that must be engineered from day one.

---

## 1. Input Integration Pathways on iOS

Dating apps (Tinder, Hinge, Bumble) run in isolated application sandboxes. An assistant app cannot passively monitor or read the screen of another app. Therefore, our iOS client must rely on user-initiated bridge mechanisms:

```
+-----------------------------------------------------------------------------------+
| iOS Integration Modalities Comparison                                             |
+-------------------+-----------------+-----------------------+---------------------+
| Modality          | User Friction   | Technical Complexity  | Feasibility / Risk  |
+-------------------+-----------------+-----------------------+---------------------+
| In-App Photo      | Medium          | Low                   | 100% Feasible       |
| Picker / Paste    | (App switch)    | Standard SwiftUI      | Zero App Store risk |
+-------------------+-----------------+-----------------------+---------------------+
| iOS Share Sheet   | Low-Medium      | Low-Medium            | 100% Feasible       |
| Extension         | (Share screen)  | `UIActivityItem`      | Standard Apple API  |
+-------------------+-----------------+-----------------------+---------------------+
| iOS Keyboard      | Very Low        | High                  | Highly Feasible     |
| Extension         | (In-app typing) | `UIInputViewController`| 30MB RAM Limit!     |
+-------------------+-----------------+-----------------------+---------------------+
| Accessibility /   | None            | Prohibited            | NOT Feasible        |
| Screen Reader     |                 |                       | Guaranteed Rejection|
+-------------------+-----------------+-----------------------+---------------------+
```

### Modality 1: Native In-App Experience (MVP Foundation)
- **Mechanism**:
  - `PhotosPicker` (iOS 16+) with zero permission prompts required for user-selected photos.
  - `UIPasteboard.general.image` detection: when the user opens the app, detect if a screenshot is in the clipboard and automatically prompt: *"Analyze screenshot from Tinder?"*
- **Advantages**: Full memory access, complete design freedom in SwiftUI, zero risk of sandbox termination.

### Modality 2: Custom iOS Keyboard Extension (`UIInputViewController`)
- **Mechanism**:
  - The app installs a custom keyboard that appears inside any text field across the OS (Tinder, Hinge, iMessage, Instagram).
  - The keyboard contains action buttons: *"Analyze Latest Screenshot"*, *"Smart Reply"*, *"Change Vibe"*.
- **Critical Technical Constraints & Mitigations**:
  1. **Memory Limit (RAM Cap)**:
     - iOS strictly limits Keyboard Extensions to **~30MB–48MB of RAM**. If memory exceeds this threshold, the OS immediately kills the extension process and falls back to the default system keyboard.
     - *Mitigation*: Do NOT load heavy image models or large UI libraries inside the keyboard extension. The keyboard should offload image resizing and network requests to lightweight URLSession tasks or an `AppGroup` shared container.
  2. **"RequestsOpenAccess" (Allow Full Access)**:
     - Keyboards are isolated by default and cannot access network sockets without user permission.
     - In `Info.plist`, set `RequestsOpenAccess = YES`.
     - An educational onboarding screen must guide the user to **Settings → Keyboards → Allow Full Access** to communicate with our AI backend.
  3. **Photo Library Access in Keyboard**:
     - Keyboards cannot present standard `PHPickerViewController`.
     - *Solution*: The main app saves the latest user screenshots into a shared App Group (`group.com.company.aidatingassistant`), or the user copies the chat text / screenshot to clipboard, which the keyboard reads via `UIPasteboard`.

### Modality 3: iOS Share Sheet Action Extension
- **Mechanism**:
  - When the user takes an iOS screenshot (Power + Volume Up), a floating thumbnail appears.
  - The user taps the thumbnail, taps **Share**, and selects our **"Dating Assistant"** action.
  - A compact modal displays 3 generated replies with a "Copy & Open Dating App" button.
- **Feasibility**: High. Clean native Apple extension pattern.

---

## 2. Recommended iOS Tech Stack

```
+-------------------------------------------------------------+
|               iOS Client Architecture (Native Swift)         |
+-------------------------------------------------------------+
| UI Framework      | SwiftUI (iOS 17+ targeted)              |
| Architecture      | MVVM + Clean Architecture / Swift Concurrency|
| Extensions        | - Custom Keyboard (UIInputViewController)|
|                   | - Share Extension (SLComposeService)     |
| Local Vision      | Apple Vision Framework (VNRecognizeText) |
| Data Persistence  | SwiftData / CoreData + Shared AppGroup   |
| In-App Purchases  | StoreKit 2 (native async/await IAP)      |
| Network           | URLSession + async/await with Server     |
+-------------------------------------------------------------+
```

### Why Native Swift / SwiftUI over Cross-Platform for Phase 1?
1. **App Extension Reliability**: React Native and Flutter have severe overhead and bundle size bloat that frequently exceeds Apple's 30MB Keyboard Extension RAM ceiling.
2. **First-Party Vision Framework**: Native Swift allows zero-latency on-device OCR using `VNRecognizeTextRequest` before sending text to the cloud, reducing bandwidth and server costs.
3. **StoreKit 2**: Apple's modern Swift-native In-App Purchase API simplifies subscription handling, trial detection, and receipt verification with zero third-party dependencies.
4. **Android Sprint 2 Ready**: The backend API, prompt engineering, and database schemas remain 100% reusable when Android is introduced in Phase 2.

---

## 3. Performance & Latency Targets

Daters are often mid-conversation and demand instant replies. A delay of more than 3 seconds breaks the flow.

```
Target Latency Budget: < 1,500ms Total Round-Trip
├── On-device Image Preprocessing & Crop: ~100ms
├── Network Upload (compressed WebP / JPEG): ~250ms
├── Cloud Gateway & OCR / Vision LLM Inference: ~800ms
└── Response Parsing & Client Display: ~150ms
```

---

## 4. Technical Feasibility Conclusion

The iOS implementation is **100% FEASIBLE**. 
- The MVP can launch with a refined in-app flow + clipboard auto-detection.
- Phase 1 fast-follow will deliver the iOS Custom Keyboard Extension with strict adherence to memory boundaries (<30MB) and App Group data sharing.
