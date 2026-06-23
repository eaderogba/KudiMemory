# PRD — WhatsApp-Native AI Expense Tracker for Nigerians

## Working Title

Possible names:

* KudiMemory
* KudiTrack
* NairaNote
* CashFlowAI
* KudiLens
* SpendPal
* KoloAI
* TrackAm

---

# 1. Product Overview

## Product Summary

A WhatsApp-native AI assistant that helps Nigerians track and understand their spending by simply sending:

* receipt photos
* POS slips
* transfer screenshots
* SMS debit alerts
* voice notes
* typed expenses

The assistant automatically extracts spending information, categorizes transactions, stores expense history, and sends intelligent weekly/monthly summaries.

The goal is to remove the friction of manual expense tracking and make financial awareness effortless for everyday Nigerians.

---

# 2. Problem Statement

Most Nigerians do not track their expenses consistently because:

* manual entry is stressful
* budgeting apps are too complex
* many expenses are cash-based
* bank-sync solutions miss transactions
* existing tools are not built for Nigerian financial behavior
* users lack discipline for traditional finance apps

As a result:

* people underestimate spending
* savings become difficult
* users have poor visibility into spending patterns
* small leakages accumulate unnoticed

---

# 3. Vision

To become the easiest and most conversational financial memory assistant for Africans.

The product should feel less like accounting software and more like:

> “An AI companion that remembers where your money goes.”

---

# 4. Target Users

## Primary Users

### Young Professionals

* Salary earners
* Gig workers
* Remote workers
* Freelancers
* Tech workers

Pain points:

* “I don’t know where my salary goes.”
* irregular tracking habits
* impulsive spending

---

### Students

* allowance management
* food and transport tracking
* frequent low-value transactions

---

### SME Owners / Side Hustlers

* separate personal vs business expenses
* informal bookkeeping
* daily cashflow visibility

---

### Families / Couples

* shared household spending
* grocery and transport budgeting

---

# 5. Core Product Principles

## 1. Frictionless

The user should never need to fill long forms.

---

## 2. Conversational

Interactions should feel natural and human.

---

## 3. Nigerian-First

The product should understand:

* Nigerian merchants
* POS slips
* transfer alerts
* local spending patterns
* Nigerian slang and context

---

## 4. Mobile-First

Most usage will happen on WhatsApp.

---

## 5. Insight-Driven

The product should not only store expenses but help users understand their behavior.

---

# 6. MVP Scope

## Core User Flow

### Step 1 — User sends expense input

Accepted formats:

* receipt image
* POS receipt image
* bank transfer screenshot
* debit SMS screenshot
* typed text
* voice note

Examples:

* “Spent 5k on fuel”
* receipt image
* screenshot of debit alert
* voice note: “Paid 3500 for transport today”

---

### Step 2 — AI extracts structured transaction

System extracts:

* merchant
* amount
* date
* transaction type
* category
* optional items

Example output:

```json
{
  "merchant": "Shoprite",
  "amount": 15700,
  "category": "Groceries",
  "date": "2026-05-19"
}
```

---

### Step 3 — Confirmation message

Bot replies:

> ₦15,700 saved under Groceries 🛒

---

### Step 4 — Expense storage

Transaction saved to user timeline.

---

### Step 5 — Summary generation

Users receive:

* weekly summaries
* monthly summaries
* trend insights
* top spending categories

---

# 7. MVP Features

## A. Receipt Scanning

### Capabilities

* OCR extraction
* total amount detection
* merchant extraction
* date extraction
* item parsing (optional MVP)

### Supported Inputs

* supermarket receipts
* restaurant receipts
* pharmacy receipts
* fuel station receipts
* POS receipts

---

## B. Smart Categorization

### Initial Categories

* Food & Groceries
* Transport
* Airtime & Data
* Shopping
* Health
* Utilities
* Entertainment
* Giving
* Family Support
* Bills
* Miscellaneous

---

## C. Manual Expense Logging

Examples:

* “Spent 3k on fuel”
* “Paid 10k for data”
* “Transport 2500”

AI should infer:

* amount
* category
* intent

---

## D. Voice Note Logging

User sends voice note.

Speech-to-text converts message.

AI extracts expense.

---

## E. Weekly Summary

Example:

> 📊 Weekly Spending Summary
>
> Total Spent: ₦82,400
>
> 🍛 Food — ₦35,000
> 🚕 Transport — ₦15,000
> 🛒 Shopping — ₦12,000
>
> Biggest Merchant:
> Shoprite

---

## F. Monthly Summary

Features:

* total monthly spend
* spending trend comparison
* top merchants
* top categories
* spending spikes

---

## G. Spending Insights

Examples:

* “You spent more on transport this week than last week.”
* “Your food spending increased by 18%.”
* “Bolt rides accounted for 22% of your transport spending.”
* “You bought shawarma 9 times this month 😅”

Tone should feel conversational and relatable.

---

# 8. Future Features (Post-MVP)

## Smart Financial Intelligence

* monthly burn rate
* savings recommendations
* spending predictions
* anomaly detection
* recurring expense detection

---

## Financial Goals

* savings goals
* event budgeting
* debt tracking

---

## Family Accounts

* shared household tracking
* couple mode
* group expenses

---

## Merchant Intelligence

* favorite stores
* merchant spend rankings
* location-based spending

---

## WhatsApp Mini App

* charts
* dashboards
* spend analytics

---

## AI Financial Coach

Examples:

* “Your spending pattern suggests impulse purchases on weekends.”
* “You may exceed your usual monthly spending trend.”

---

# 9. User Experience Principles

## Desired Feeling

The product should feel:

* lightweight
* friendly
* conversational
* intelligent
* non-judgmental

Avoid:

* accounting complexity
* finance jargon
* spreadsheet aesthetics

---

## UX Style

Preferred tone:

* warm
* witty
* Nigerian-friendly
* encouraging

Examples:

* “Bolt is collecting rent from you this month 😅”
* “Food spending don high small 👀”
* “Weekend spending activated again 😂”

---

# 10. Technical Architecture

## Frontend

Primary Interface:

* WhatsApp

Optional Future:

* lightweight dashboard web app
* mobile companion app

---

## Backend

Suggested Stack:

* Next.js
* FastAPI (optional AI service)
* PostgreSQL
* Supabase
* Redis / Upstash
* Queue workers

---

## WhatsApp Layer

Possible options:

* Meta WhatsApp Cloud API
* Twilio
* Termii

Recommended:

* Meta Cloud API directly

---

## OCR Layer

Possible options:

* OpenAI Vision
* Google Vision API
* AWS Textract

Recommended MVP:

* OpenAI Vision

---

## AI Layer Responsibilities

The AI layer should:

* parse OCR output
* identify merchant
* normalize merchant names
* categorize transactions
* extract totals
* detect duplicates
* generate insights

---

# 11. Data Model

## User

* id
* phone_number
* name
* timezone
* created_at

---

## Transaction

* id
* user_id
* merchant
* amount
* category
* source_type
* raw_text
* created_at
* transaction_date

---

## Merchant

* id
* normalized_name
* aliases
* category_defaults

---

## Summary

* id
* user_id
* type (weekly/monthly)
* generated_text
* created_at

---

# 12. AI Challenges

## Receipt Inconsistency

Nigerian receipts vary heavily:

* faded prints
* poor formatting
* abbreviations
* incomplete details
* inconsistent merchant naming

Examples:

* SHPRT
* SHOPRITE
* SHOPRITE IKEJA

Need:

* merchant normalization
* fuzzy matching
* fallback categorization

---

## Duplicate Detection

Users may send:

* same receipt twice
* receipt + bank alert

Need duplicate logic.

---

## Low-Quality Images

Need graceful handling for:

* blurry images
* dark photos
* folded receipts

---

# 13. Privacy & Trust

This is critical.

Users are sharing financial information.

Requirements:

* encrypted storage
* secure media handling
* delete raw images after extraction (optional)
* transparent privacy policy
* no selling identifiable financial data

Potential trust messaging:

> “Your financial data stays private and secure.”

---

# 14. Monetization

## Free Plan

* limited monthly scans
* weekly summaries
* basic categorization

---

## Premium Plan

Possible pricing:

* ₦1,500–₦3,000/month

Features:

* unlimited scans
* advanced insights
* exports
* family accounts
* predictive analytics

---

## Future B2B Opportunity

Anonymous consumer spending intelligence.

Potential customers:

* FMCGs
* banks
* retail analytics firms
* market research companies

Only anonymized and aggregated insights.

---

# 15. Go-To-Market Strategy

## Phase 1 — Early Users

Target:

* tech Twitter/X
* WhatsApp groups
* university communities
* young professionals

---

## Viral Loop

Users share:

* funny summaries
* spending insights
* monthly recap cards

This creates organic growth.

---

## Distribution Positioning

Not:

> “Expense tracking app.”

Instead:

> “The AI on WhatsApp that remembers where your money goes.”

---

# 16. Key Metrics

## Activation Metrics

* first receipt sent
* first expense logged
* first summary delivered

---

## Retention Metrics

* weekly active users
* receipts per user
* monthly active conversations
* summary open rate

---

## Product Quality Metrics

* OCR accuracy
* categorization accuracy
* duplicate detection rate
* failed extraction rate

---

# 17. Risks

## User Retention

Users may stop sending receipts.

Need:

* delightful UX
* lightweight interactions
* useful summaries

---

## OCR Accuracy

Poor extraction reduces trust.

Need:

* strong fallback flows
* confirmation UX

---

## WhatsApp Costs

Message delivery costs may increase.

Need:

* efficient notification strategy
* monetization alignment

---

# 18. Competitive Advantage

Potential moats:

* Nigerian receipt dataset
* merchant normalization engine
* conversational UX
* WhatsApp-native behavior
* localized financial intelligence

The moat is NOT OCR.

The moat is:

> local understanding + habit retention.

---

# 19. MVP Launch Recommendation

## Build Order

### Phase 1

* WhatsApp bot
* image upload
* OCR extraction
* transaction storage
* simple summaries

---

### Phase 2

* voice notes
* transfer screenshot parsing
* AI insights
* merchant normalization

---

### Phase 3

* dashboards
* predictive analytics
* family mode
* financial coaching

---

# 20. Success Definition

The product succeeds if users begin naturally forwarding receipts and spending information to the assistant as part of daily life.

The long-term behavioral goal is:

> “Whenever I spend money, I send it to the bot.”

Once that habit forms, the assistant becomes the user’s financial memory layer.
