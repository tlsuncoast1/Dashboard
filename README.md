# Bot Dashboard

This repo contains a FastAPI backend for monitoring and controlling your trading bot.

## To Run Locally
```
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## To Deploy on Railway
- Use `/backend/main.py` as entry
- Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port 8000`
