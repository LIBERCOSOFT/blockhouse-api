from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    order_type = Column(String)  # "buy" or "sell"
    status = Column(String, default="pending")  # pending, filled, canceled
    created_at = Column(DateTime, default=datetime.utcnow)
