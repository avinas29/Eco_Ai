# Eco_Smart AI ⚡

## Overview
Eco_Smart AI is an intelligent energy management system that leverages AI to optimize electricity usage in smart homes. The system uses real-time data, predictive analytics, and intelligent scheduling to reduce energy costs and improve sustainability.

It is designed as a prototype for AI-driven energy optimization, integrating concepts like smart meters, solar forecasting, and automated appliance scheduling.

---

## 🚀 Features

### ⚡ Live Energy Monitoring
- Tracks real-time:
  - Solar generation
  - Home consumption
  - Grid export
  - Battery status

### 📊 AI Forecasting
- Predicts future electricity demand
- Estimates solar energy generation based on patterns

### 🧠 Smart Scheduling
- Suggests optimal time to run appliances
- Uses tariff pricing + solar availability

### 💰 Cost Optimization
- Helps reduce electricity bills using Time-of-Day (ToD) pricing

### 🤖 AI Assistant (Voice Enabled)
- Answers user queries about energy usage
- Provides smart recommendations
- Supports voice output (prototype)

---

## 🛠 Tech Stack

- Frontend: HTML + React (CDN) + Tailwind CSS  
- Backend: FastAPI (Python)  
- Data Processing: Pandas, NumPy  
- Machine Learning: Basic forecasting models  
- Voice: Browser Speech API (prototype for Azure Speech)

---

## 📂 Project Structure

backend/
├── data/
│   ├── appliances.csv
│   ├── smart_meter.csv
│   └── tariffs.csv
│
├── model/
│   ├── demand_forecast.py
│   └── solar_forecast.py
│
├── optimizer/
│   └── scheduler.py
│
├── services/
│   ├── analytics_service.py
│   ├── assistant_service.py
│   └── energy_service.py
│
└── main.py

---

## ⚙️ Installation

### 1. Clone the repository
git clone https://github.com/avinas29/Eco_Ai.git
cd Eco_Ai

### 2. Create virtual environment
python -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install fastapi uvicorn pandas numpy scikit-learn

---

## ▶️ Running the Project

### Start Backend
uvicorn backend.main:app --reload --port 8001

### Run Frontend
Open index.html in your browser

---

## 🔗 API Endpoints

- /energy/live → Real-time energy data  
- /energy/forecast → Demand & solar prediction  
- /schedule/optimize → Appliance scheduling  
- /assistant/query → AI assistant responses  

---

## 🌍 Future Enhancements

- Azure Maps API → Weather-based solar prediction  
- Azure IoT Hub → Smart meter integration  
- Azure Speech API → Multilingual voice assistant  

---

## 🤝 Contributing
Contributions are welcome! Feel free to improve models, UI, or integrations.

---

## 📄 License
This project is licensed under the MIT License.

---

## 🙌 Acknowledgements
- Microsoft AI Hackathon inspiration  
- Open-source AI and energy research community  

---

## 📬 Contact
Avinash Bishnoi  
IIT Guwahati  
## Last Updated
This README was last updated on 2026-03-20.
