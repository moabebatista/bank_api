from fastapi import FastAPI
from app.routers import auth, accounts, transactions

app = FastAPI()

# from app.routers import accounts
# depois
app.include_router(accounts.router)

app.include_router(auth.router)
app.include_router(accounts.router)
app.include_router(transactions.router)

@app.get("/")
async def root():
    return {"message": "API de Banco Virtual"}