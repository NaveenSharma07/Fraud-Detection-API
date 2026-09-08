from pydantic import BaseModel

class Transaction(BaseModel):
    amount: float
    country: str
    device: str
    