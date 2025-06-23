from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

class AccountCreate(BaseModel):
    initial_deposit: float = 0.0

class AccountOut(BaseModel):
    id: int
    balance: float