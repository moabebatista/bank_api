from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/auth/login")
async def login(username: str, password: str):
    if username == "user" and password == "pass":
        return {"access_token": "dummy_token", "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Invalid credentials")