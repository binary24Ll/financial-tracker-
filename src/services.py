import asyncio
from sqlalchemy import select 
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)    
from src.db import AsyncSessionLocal
from src.models import Category, Transaction
from src.schemas import TransactionCreate

async def create_category(session: AsyncSession, name: str, create_type: str)-> Category:
    new_category = Category(name=name, type=create_type)
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    return new_category 

async def get_category(session: AsyncSession)-> list[Category]:
    r = await session.execute(select(Category))
    return list(r.scalars().all())

async def create_transaction(session: AsyncSession, tx_data: TransactionCreate)-> Transaction:
    new_tx = Transaction(**tx_data.model_dump())
    session.add(new_tx)
    await session.commit()
    await session.refresh(new_tx)
    return new_tx

async def get_transaction(session: AsyncSession)-> list[Transaction]:
    rs = await session.execute(select(Transaction))
    return list(rs.scalars().all())

