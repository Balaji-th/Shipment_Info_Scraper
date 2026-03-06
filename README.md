# 🚢 Ship Information Extractor (FastAPI + Playwright + LLM)

A web application that extracts **shipyard details from vessel pages** using web scraping and an LLM-powered information extractor.

The application scrapes vessel pages from **TrustedDocks**, processes the raw text, and extracts structured ship-building details using a Large Language Model.

Users can simply enter an **IMO number in the web interface** and retrieve:

* IMO Number
* Shipyard Name
* Country
* Hull Number

---

# ✨ Features

* 🌐 **Web Scraping** using Playwright
* 🤖 **LLM-based data extraction** using LangChain + Groq
* ⚡ **FastAPI backend**
* 🖥️ **Simple frontend UI**
* 📦 **Structured JSON output**
* 📊 **Optional Excel export support**

---

# 🏗️ Project Structure

```
ship_app/
│
├── main.py              # FastAPI application
├── scraper.py           # Scraping + LLM extraction logic
│
├── templates/
│     └── index.html     # Frontend UI
│
├── static/
│
├── data/                # Raw scraped text files
├── outputs/             # Excel outputs
│
├── .env                 # API keys
└── README.md
```

---

# ⚙️ Requirements

* Python **3.9+**
* Playwright
* FastAPI
* LangChain
* Groq API key

---

# 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ship-info-extractor.git
cd ship-info-extractor
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install fastapi uvicorn playwright langchain langchain_groq python-dotenv openpyxl jinja2
```

---

### 4️⃣ Install Playwright Browsers

```bash
playwright install
```

---

### 5️⃣ Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

# 🖥️ Using the Application

1. Enter an **IMO number**
2. Click **Search**
3. The system will:

   * Scrape the vessel page
   * Extract raw text
   * Process it with the LLM
   * Display structured ship details

Example in
