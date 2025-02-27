from typing import List, Optional, cast
import json
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import OrderModel
from app.schemas import Order, OrderCreate
from app.ws_manager import manager

router = APIRouter()

@router.post("/orders", response_model=Order, status_code=201)
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    # Check if the symbol already exists in the orders table
    existing_order = db.query(OrderModel).filter_by(symbol=order.symbol).first()
    if existing_order:
        raise HTTPException(
            status_code=400,
            detail=f"Order for symbol '{order.symbol}' already exists. Duplicate orders are not allowed."
        )

    # Create the order if the symbol does not exist
    db_order = OrderModel(
        symbol=order.symbol,
        price=order.price,
        quantity=order.quantity,
        order_type=order.order_type
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    # Notify WebSocket clients
    await manager.broadcast(
        json.dumps({
            "event": "new_order",
            "data": {
                "id": db_order.id,
                "symbol": db_order.symbol,
                "status": db_order.status
            }
        })
    )

    return db_order

@router.get("/orders", response_model=List[Order])
def get_orders(
    skip: int = 0,
    limit: int = 20,
    symbol: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(OrderModel)
    if symbol:
        query = query.filter(OrderModel.symbol == symbol)
    return query.offset(skip).limit(limit).all()

@router.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: str, db: Session = Depends(get_db)):
    db_order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.put("/orders/{order_id}/status", response_model=Order)
async def update_order_status(order_id: str, status: str, db: Session = Depends(get_db)):
    db_order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    if status not in ["pending", "fulfilled", "canceled"]:
        raise HTTPException(status_code=400, detail="Invalid status")

    setattr(db_order, "status", status)

    db.commit()
    db.refresh(db_order)

    # Notify WebSocket clients
    await manager.broadcast(
        json.dumps({
            "event": "status_update",
            "data": {
                "id": db_order.id,
                "symbol": db_order.symbol,
                "status": db_order.status
            }
        })
    )

    return db_order

@router.websocket("/ws/orders")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        await websocket.send_text(json.dumps({"event": "connected", "message": "Connected to order updates"}))
        while True:
            # Keep the connection alive
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
