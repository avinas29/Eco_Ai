"""
GramUrja-AI FastAPI Backend
Smart Energy Management System for households with solar and smart meters.
"""

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from backend.services.energy_service import get_live_energy
from backend.model.demand_forecast import get_next_day_demand_forecast
from backend.model.solar_forecast import get_next_day_solar_forecast
from backend.optimizer.scheduler import optimize_schedule
from backend.services.analytics_service import get_analytics_summary
from backend.services.assistant_service import assistant_response, get_supported_languages

app = FastAPI(title="GramUrja-AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Health / Home
# -------------------------
@app.get("/")
def home():
    return {"message": "GramUrja-AI Backend Running"}


# -------------------------
# Live Energy
# -------------------------
@app.get("/energy/live")
def live_energy():
    """Returns live home energy state (simulated from smart_meter + IoT variation)."""
    return get_live_energy()


# -------------------------
# Energy Forecast
# -------------------------
@app.get("/energy/forecast")
def energy_forecast():
    """Returns next-day demand and solar forecast."""
    demand_data = get_next_day_demand_forecast()
    solar_data = get_next_day_solar_forecast()
    return {
        "predicted_demand_kw": demand_data["predicted_avg_demand_kw"],
        "predicted_solar_kw": solar_data["predicted_peak_solar_kw"],
        "predicted_daily_demand_kwh": demand_data["predicted_daily_demand_kwh"],
        "predicted_solar_kwh": solar_data["predicted_solar_kwh"],
    }


# -------------------------
# Smart Schedule
# -------------------------
@app.get("/schedule/optimize")
def schedule_optimize():
    """Returns recommended appliance schedule based on solar and tariffs."""
    return optimize_schedule()


# -------------------------
# Analytics
# -------------------------
@app.get("/analytics/summary")
def analytics_summary():
    """Returns daily consumption, monthly cost estimate, top appliance."""
    return get_analytics_summary()


# -------------------------
# AI Assistant
# -------------------------
@app.post("/assistant/query")
def assistant_query(query: dict = Body(...)):
    """Handles AI assistant text/voice queries. Pass language code for response in that language."""
    message = query.get("message", "")
    language = query.get("language", "en")
    response = assistant_response(message, language=language)
    return {"response": response}


@app.get("/assistant/languages")
def assistant_languages():
    """Returns supported languages (English + 10 Indian languages)."""
    return {"languages": get_supported_languages()}


# -------------------------
# Tariff Prices (optional, for frontend)
# -------------------------
@app.get("/tariff/prices")
def tariff_prices():
    """Returns hourly tariff prices."""
    import pandas as pd
    from pathlib import Path
    path = Path(__file__).resolve().parent / "data" / "tariffs.csv"
    df = pd.read_csv(path)
    return {"tariffs": df[["hour", "price_per_kwh"]].to_dict(orient="records")}
