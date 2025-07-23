from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running ✅"}

@app.get("/status")
def status():
    return {
        "active": True,
        "rsi": 42.0,
        "divergence": "none",
        "last_trade": {
            "side": "buy",
            "price": 43000,
            "ts": 1722241000
        }
    }
}