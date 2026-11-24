from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from datetime import datetime 

class CategoryCreate(BaseModel):
    name: str
    type: str 

class CategoryRead(BaseModel):
    id: int 
    name: str
    type: str 
    model_config = ConfigDict(from_attributes=True)

class TransactionCreate(BaseModel):
    amount: Decimal
    description: str | None = None 
    category_id: int      

class TransactionRead(BaseModel):
    id: int 
    amount: Decimal 
    description: str | None = None 
    created_at: datetime
    category_id: int 
    model_config = ConfigDict(from_attributes=True)


