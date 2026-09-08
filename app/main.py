from fastapi import FastAPI
from app.api.transactions import router as transactions_router

app = FastAPI(title="FRAUD DETECTION API")

app.include_router(transactions_router)

@app.get("/")
def home():
    return {"message": "Fraud Detection API"}