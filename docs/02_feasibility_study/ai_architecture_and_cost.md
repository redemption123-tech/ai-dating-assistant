# AI Architecture, Pipeline & Cost Modeling

This document specifies the end-to-end AI orchestration pipeline, model selection, prompt engineering strategy, and cost-per-user financial modeling for the AI Dating Assistant.

---

## 1. End-to-End AI Architecture Pipeline

```
[User Screenshot] 
       │
       ▼
[Client Preprocessing] ── (Resize, JPEG compression, aspect ratio normalization)
       │
       ▼ (HTTPS REST / WebSocket)
[API Gateway / Auth] ── (Rate limit, Auth token, Tier check)
       │
       ▼
[Vision & Dialogue Engine] 
       │
       ├── Pipeline Option A: Direct Multimodal (Vision LLM)
       │     └─ Feed image directly to Gemini 1.5 Flash / GPT-4o-mini
       │
       └── Pipeline Option B: Hybrid (On-Device OCR + Text LLM)
             ├─ Local Apple Vision Framework (VNRecognizeText)
             ├─ Bubble extraction & speaker assignment (User vs Match)
             └─ Lightweight Text LLM (Fast, lowest cost)
       │
       ▼
[Prompt Engineering & Persona Engine]
       │
       ├─ Dating Context Injector (Platform: Hinge/Tinder/Bumble/IG)
       ├─ User Persona & Vibe Rules (Tone: Flirty, Witty, Chill, Bold)
       ├─ Anti-Cringe Guardrails & Safety Filter
       └─ Date Intent Classifier
       │
       ▼
[Response Generation & Formatting]
       │
       ▼ (JSON Structured Output)
[Client Presentation: 3 Tailored Options]
```

---

## 2. Model Evaluation & Benchmark Comparison

For an interactive mobile dating assistant, our primary evaluation criteria are:
1. **Latency**: Time-to-first-token and complete generation must be under 1.5 seconds.
2. **Conversational Nuance**: Understanding Gen Z slang, double entendres, dry sarcasm, and dating emojis.
3. **Multimodal Cost**: Affordable pricing per image scan to maintain high margins.

| Model | Vision Support | Latency (P90) | Cost per 1K Input Tokens | Cost per 1K Output Tokens | Fit for Dating Assistant |
|---|:---:|:---:|:---:|:---:|:---:|
| **Gemini 1.5 Flash** | Native | **~600ms** | **$0.000075** | **$0.0003** | **Primary Recommended** (Fastest, ultra-low cost) |
| **GPT-4o-mini** | Native | ~800ms | $0.00015 | $0.0006 | Excellent Secondary / Fallback |
| **Claude 3.5 Haiku** | Fast | ~700ms | $0.0008 | $0.004 | Strong banter, slightly higher cost |
| **GPT-4o (Full)** | Native | ~1800ms | $0.005 | $0.015 | Overkill for quick replies, higher cost |

---

## 3. Prompt Engineering Strategy

### System Prompt Philosophy
1. **Never sound like ChatGPT**: ChatGPT default voice is polite, formal, overly explanatory, and apologetic—the antithesis of attractive dating banter.
2. **Casual & Punchy**: Keep suggestions to 1–2 sentences maximum. Daters never send paragraphs unless writing an essay.
3. **Contextual Hooks**: Always latch onto a specific detail in the match's message or bio (e.g. their dog, music taste, witty contradiction).
4. **Three Distinct Flavors**:
   - **Vibe A: Safe & Witty**: High-confidence banter, low-risk tease.
   - **Vibe B: Playful & Flirty**: Direct romantic tension, subtle playful challenge.
   - **Vibe C: Bold & Close-Focused**: Steers toward getting off the app (e.g. "We could argue about this over espresso martinis").

### Sample Structured Output Schema
```json
{
  "context_analysis": {
    "platform_detected": "Hinge",
    "match_sentiment": "Playful teasing",
    "interest_score_0_100": 78
  },
  "suggestions": [
    {
      "tone": "Witty",
      "text": "Tell me you didn't just look up that trivia 5 minutes ago."
    },
    {
      "tone": "Flirty",
      "text": "Dangerous game trying to impress me this early, but it's working."
    },
    {
      "tone": "Direct",
      "text": "I respect the confidence. Let's see if your banter holds up over drinks this Thursday."
    }
  ],
  "coaching_tip": "She asked an open question. Avoid answering with just a fact—tease her before answering."
}
```

---

## 4. Cost Modeling & Financial Feasibility

### Unit Economics Per User
- **Assumptions**:
  - Active dating user scans: **15 screenshots / day**.
  - Monthly scans per active user: **450 requests / month**.
  - Image input token weight: ~800 tokens per screenshot.
  - Prompt overhead + history: ~500 tokens.
  - Output tokens: ~150 tokens.
  - Total tokens per scan: ~1,450 tokens.

### Cost Breakdown Using Gemini 1.5 Flash:
- Input cost per scan: `(1,300 tokens / 1,000,000) * $0.075` = **$0.0000975**
- Output cost per scan: `(150 tokens / 1,000,000) * $0.30` = **$0.000045**
- **Total AI API Cost per Request**: **$0.0001425 (~0.014 cents)**
- **Monthly API Cost for Heavy User (450 requests)**: `450 * $0.0001425` = **~$0.064 (6.4 cents / month)**!

### Profit Margin Comparison:
| Metric | Weekly Plan ($7.99/wk) | Monthly Plan ($24.99/mo) |
|---|:---:|:---:|
| **Gross Revenue (Monthly)** | $31.96 | $24.99 |
| **Apple Fee (15% Small Business)** | $4.79 | $3.75 |
| **AI Inference Cost (450 scans)** | $0.06 | $0.06 |
| **Server / Cloud Hosting** | $0.15 | $0.15 |
| **Net Contribution Margin** | **$26.96 (84.3%)** | **$21.03 (84.1%)** |

**Conclusion**: The gross margins on AI Dating Assistants are astronomical (>84% after app store fees and model inference). The model economics are exceptionally viable.
