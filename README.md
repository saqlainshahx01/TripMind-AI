# ✈️ TripMind AI — Intelligent Multi-Agent Travel Planner

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-red)
![Groq](https://img.shields.io/badge/Groq-LLaMA3.1-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

> Plan your perfect trip in minutes using the power of AI! TripMind AI uses 9 specialized AI agents to create a complete personalized travel experience.

---

## 🤖 How It Works

```
User Input → 9 AI Agents → Complete Trip Plan
     ↓
Travel Type, Interests, Budget, Season, Duration
     ↓
City Selection → Research → Itinerary → Budget → Weather → Safety → Language → Hotels → Flights
```

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 🏙️ City Selector | AI recommends 3 best cities based on preferences |
| 🔍 Local Expert | Detailed city info, attractions & restaurants |
| 📅 Travel Planner | Day-by-day itinerary with meal suggestions |
| 💰 Budget Manager | Complete budget breakdown in table format |
| 🌤️ Weather Expert | Seasonal weather guide & packing list |
| 🚨 Safety Expert | Emergency contacts & safety tips |
| 🗣️ Language Guide | 20 essential local phrases |
| 🏨 Hotel Expert | Hotels across all budget ranges |
| ✈️ Flight Expert | Flight info & airport transfers |

---

## 🧠 Multi-Agent Architecture

```
                    ┌─────────────────┐
                    │   User Input    │
                    └────────┬────────┘
                             │
              ┌──────────────▼──────────────┐
              │      City Selector Agent     │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │      Local Expert Agent      │
              └──────────────┬──────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
┌────────▼───────┐  ┌────────▼───────┐  ┌───────▼────────┐
│ Travel Planner │  │ Budget Manager │  │ Weather Expert │
└────────────────┘  └────────────────┘  └────────────────┘
         │                   │                   │
┌────────▼───────┐  ┌────────▼───────┐  ┌───────▼────────┐
│ Safety Expert  │  │ Language Guide │  │  Hotel Expert  │
└────────────────┘  └────────────────┘  └────────────────┘
                             │
              ┌──────────────▼──────────────┐
              │       Flight Expert          │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │      Complete Trip Plan      │
              └─────────────────────────────┘
```

---

## 🛠️ Tech Stack

- **Python 3.12** — Core development
- **Streamlit** — Interactive web interface
- **Groq API** — Ultra-fast LLaMA 3.1 inference
- **Prompt Engineering** — Specialized agent behavior
- **python-dotenv** — Environment management

---

## ⚙️ Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/saqlainshahx01/TripMind-AI.git
cd TripMind-AI
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Get Free Groq API Key
- Go to [console.groq.com](https://console.groq.com)
- Sign up for free
- Create API key

### 5️⃣ Add Environment Variables
```bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```

### 6️⃣ Run Application
```bash
streamlit run main.py
```

---

## 📁 Project Structure

```
TripMind-AI/
│
├── 📄 main.py          # Streamlit UI
├── 🤖 agents.py        # 9 AI Agents
├── 📋 requirements.txt # Dependencies
├── 📖 README.md        # Documentation
└── 🔒 .env             # API Keys (not uploaded)
```

---

## 🎯 Use Cases

- Solo travel planning
- Family trip organization
- Budget travel optimization
- Cultural exploration
- Adventure trip planning

---

## 📚 Academic Context

This project is part of **NLP Course** exploring:
- Large Language Models (LLMs)
- Multi-Agent AI Systems
- Advanced Prompt Engineering
- Conversational AI Development

---

## 🔮 Future Improvements

- [ ] RAG with ChromaDB for accurate data
- [ ] Urdu language support
- [ ] PDF trip plan export
- [ ] Real-time hotel & flight prices
- [ ] Map integration

---

## 👨‍💻 Author

**Saqlain Shah**

[![GitHub](https://img.shields.io/badge/GitHub-saqlainshahx01-black)](https://github.com/saqlainshahx01)

---

*Built with ❤️ using Python & Groq AI*

⭐ If you found this helpful, please give it a star!
