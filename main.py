
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

DATA_FILE = "data.json"
STATUS_FILE = "status.txt"

# CORS for local frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Utility to load data
def read_json():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

@app.get("/status")
def get_status():
    data = read_json()
    return {
        "active": get_bot_status(),
        "rsi": data.get("rsi"),
        "divergence": data.get("divergence"),
        "last_trade": data.get("last_trade")
    }

@app.post("/pause")
def pause_bot():
    with open(STATUS_FILE, "w") as f:
        f.write("paused")
    return {"message": "Bot paused."}

@app.post("/resume")
def resume_bot():
    with open(STATUS_FILE, "w") as f:
        f.write("running")
    return {"message": "Bot resumed."}

@app.get("/is_active")
def get_bot_status():
    if not os.path.exists(STATUS_FILE):
        return True
    with open(STATUS_FILE, "r") as f:
        return f.read().strip() != "paused"
