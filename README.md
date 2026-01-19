#  FinDroid – Automated UPI Transaction Extractor

FinDroid is an **AI-powered Android automation system** that extracts daily UPI transactions from popular payment applications and stores them in a **single, continuously updated CSV file**.

It eliminates the manual, repetitive, and error-prone process of checking transaction histories across multiple apps—making it ideal for merchants and high-frequency UPI users.

---

##  Table of Contents

- [Introduction](#Introduction)
- [Problem Statement](#Problem-Statement)
- [What FinDroid Does](#What-FinDroid-Does)
- [System Architecture](#-System-Architecture)
- [Tech Stack](#Tech-Stack)
- [LLMs Used](#LLMs-Used)
- [Project Structure](#Project-Structure)
- [Setup Instructions](#Setup-Instructions)
- [How to Run FinDroid](#How-to-Run-FinDroid)
- [Output Format](#Output-Format)
- [Security and Privacy](#Security-and-Privacy)
- [Use Cases](#Use-Cases)
- [Known Limitations](#Known-Limitations)
- [Future Enhancements](#Future-Enhancements)
- [Author](#Author)

---

##  Introduction

Merchant users handle **dozens or hundreds of UPI transactions daily** across multiple payment apps.  
FinDroid automates transaction extraction using **LLM-driven Android UI reasoning**, consolidating all transactions into a reusable CSV file.

---

##  Problem Statement

Manually opening each payment application, navigating transaction histories, and maintaining financial records is:

- Time-consuming  
- Inefficient  
- Error-prone  

**FinDroid** automates this workflow to reduce manual effort and improve accuracy.

---

##  What FinDroid Does

- Automates Android UI interactions using **LLM-driven reasoning**
- Extracts transactions from:
  - PhonePe
  - Google Pay
  - Paytm
- Accepts interactive user input:
  - Target date (default: today)
  - Target application
- Saves all transactions into **one CSV file**
- Appends data if the file exists, otherwise creates a new file
- Avoids brittle UI scripts using **agent-based navigation**

---

##  System Architecture

```
User Input (Date + App)
        ↓
Prompt Instructions (prompt.py)
        ↓
DroidRun Agent
        ↓
LLM-Guided Android UI Automation
        ↓
Transaction Extraction
        ↓
Single CSV File (Create / Append)
```

---

##  Tech Stack

### Core Technologies

- Python 3.10+
- DroidRun – Android UI automation framework
- OpenRouter – LLM gateway
- Colorama – CLI styling and banners

---

##  LLMs Used

- `mistralai/devstral-2512:free` (via OpenRouter)

The LLM is responsible for:
- UI understanding
- Navigation and decision-making
- Robust interaction with dynamic Android interfaces

---

##  Project Structure

```
findroid/
│
├── main.py
├── prompt.py
├── all_upi_transactions.csv
│
├── .venv/
└── README.md
```

---

##  Setup Instructions

### Clone Repository

```bash
git clone https://github.com/yourusername/findroid.git
cd findroid
```

### Install & Run

```bash
python -m venv .venv
source .venv/bin/activate

pip install droidrun llama-index colorama python-dotenv
python main.py
```

---

##  Output Format

```csv
merchant_name,datetime,amount,direction,app
Amazon,2026-01-16 10:32,499,debit,googlepay
```

---

##  Security

- No credentials hardcoded
- Local-only processing
- Secure environment variables

---

##  Author

FinDroid was built to automate financial record-keeping using LLM-driven Android UI automation.
- [Rohit Kumar](https://github.com/rohit-447)
- [Swetankan Kumar Sinha](https://github.com/Swetankan)
- [Harsh Kartik Singh](https://github.com/HARSH-KARTIK-SINGH)