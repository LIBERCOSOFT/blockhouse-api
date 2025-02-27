from datetime import datetime
from pydantic import BaseModel

class OrderBase(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
