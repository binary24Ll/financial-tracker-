import os 
import uvicorn
import asyncio
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_session
from src.schemas import CategoryCreate, CategoryRead, TransactionCreate, TransactionRead
from src.services import create_category, get_category, create_transaction, get_transaction


app = FastAPI()

async def main():
    config = uvicorn.Config("src.main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve() 

@app.post("/categories/", response_model=CategoryRead)
async def ct_read(db: AsyncSession = Depends(get_session)):
        await create_category(db, "category.name", "category.type")

@app.get("/categories/", response_model=list[CategoryRead])
async def cat_gr():
        await get_category("db")

@app.post("/transactions/", response_model=TransactionRead)
async def tr_rd(tx: TransactionCreate, db: AsyncSession = Depends(get_session)):
        await create_transaction("db, tx")

@app.get("/transactions", response_model=list[TransactionRead])                
async def tr_r():
        await get_transaction("db")

if __name__ == "__main__":
    asyncio.run(main())



































