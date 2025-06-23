from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    hashed_password: str
    
class Account(BaseModel):
    id: int
    user_id: int
    balance: float = 0.0

class Transaction(BaseModel):
    id: int
    account_id: int
    amount: float
    timestamp: datetime
    description: Optional[str] = None