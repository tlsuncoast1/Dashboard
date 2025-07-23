# Final Backend

This is a FastAPI backend for your trading bot dashboard.

## Run Locally

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Deploy on Railway

- Make sure `main.py` is inside `backend/`
- Set your start command to:
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```
