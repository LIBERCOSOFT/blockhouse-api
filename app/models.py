import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    symbol = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Float)
    order_type = Column(String)  # "buy" or "sell"
    status = Column(String, default="pending")  # pending, filled, canceled
    created_at = Column(DateTime, default=datetime.utcnow)
