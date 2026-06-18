# 🔍 FactCheck Agent

AI-powered Fact Checking Web Application that automatically verifies factual claims from PDF documents using **Groq Llama AI + Live Web Search**.


---

## 🚀 Overview

Marketing documents, reports, and articles often contain outdated statistics, hallucinated facts, or incorrect information.

FactCheck Agent works as a **Truth Layer** that:

- Reads PDF documents
- Extracts factual claims automatically
- Cross-checks claims with live web data
- Detects outdated or false information
- Provides corrected facts

---

## ✨ Features

- 📄 PDF Upload Support
- 🧠 AI Claim Extraction
- 🌐 Live Web Verification
- 📊 Statistics & Date Checking
- 💰 Financial Claim Verification
- ⚙️ Technical Fact Validation

---

## 🏷️ Verification Results

| Status | Meaning |
|------|---------|
| ✅ Verified | Claim matches trusted web evidence |
| ⚠️ Inaccurate | Claim contains outdated/wrong details |
| ❌ False | Evidence contradicts the claim |
| ❓ Unverifiable | Not enough evidence available |

---

## 🏗️ System Architecture


PDF Upload

↓

PDF Text Extraction (pypdf)

↓

Groq Llama AI

↓

Claim Extraction

↓

Serper Google Search API

↓

Evidence Collection

↓

Groq Fact Verification

↓

Final Report


---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| AI Model | Groq Llama 3.3 |
| Web Search | Serper Google Search API |
| PDF Processing | pypdf |
| Backend | Python |

---

## 📂 Project Structure

```text
FactCheck-Agent/

├── app.py
├── requirements.txt
├── README.md

```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/rc94087/FactCheck-Agent.git

cd FactCheck-Agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Keys Required

### Groq API

Create free API key:

https://console.groq.com/keys


### Serper API

Create free API key:

https://serper.dev


Enter both keys inside the Streamlit sidebar.

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🌐 Deployment

The app can be deployed using Streamlit Community Cloud.

Steps:

1. Push project to GitHub
2. Open Streamlit Cloud
3. Select repository
4. Select `app.py`
5. Deploy

---

## 📸 Demo Flow

1. Upload PDF document
2. Click "Run Fact Check"
3. AI extracts factual claims
4. Claims are verified using live web data
5. Results displayed with explanations

---

## Example Output

```json
{
 "claim": "ChatGPT launched in 2022",
 "verdict": "Verified",
 "confidence": "High",
 "explanation": "The claim matches available sources.",
 "real_fact": null
}
```

---

## 🎯 Evaluation Handling

Designed to detect:

- Fake statistics
- Wrong dates
- Outdated numbers
- Incorrect company facts
- Misleading technical claims

The system highlights false information and provides corrected facts.

---

## 👨‍💻 Author

**Rahul Chauhan**

