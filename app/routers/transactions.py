from fastapi import APIRouter

router = APIRouter()

# Defina suas rotas aqui, por exemplo:
@router.get("/transactions")
async def read_accounts():
    return {"message": "List of transactions"}