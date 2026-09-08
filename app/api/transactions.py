from fastapi import APIRouter
from app.schema.transactions import Transaction
from app.services.fraud_service import predict_transaction

router = APIRouter(prefix="/transactions",tags=["Transactions"])

@router.post("/")
async def check_transaction(tx:Transaction):
    result = predict_transaction(tx)
    return result