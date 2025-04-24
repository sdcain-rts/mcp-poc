from fastapi import APIRouter, HTTPException, status, Path, Query
from typing import List, Optional

from models.order import OrderCreate, OrderUpdate, OrderResponse
from app.services.order_service import OrderService

# Create router for order endpoints
router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Order not found"}}
)

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    """
    Create a new order with the provided details
    """
    result = OrderService.create_order(
        customer_name=order.customer_name, 
        item=order.item, 
        quantity=order.quantity
    )
    return result

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str = Path(..., title="The ID of the order to retrieve")):
    """
    Retrieve an order by its ID
    """
    result = OrderService.get_order(order_id)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return result

@router.put("/{order_id}", response_model=OrderResponse)
async def update_order(
    order_update: OrderUpdate,
    order_id: str = Path(..., title="The ID of the order to update")
):
    """
    Update an order's status
    """
    result = OrderService.update_order_status(order_id, order_update.status)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return result

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: str = Path(..., title="The ID of the order to delete")):
    """
    Delete an order by ID
    """
    result = OrderService.delete_order(order_id)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return None

@router.get("/", response_model=List[OrderResponse])
async def list_orders(
    customer_name: Optional[str] = Query(None, title="Filter orders by customer name")
):
    """
    List all orders, optionally filtered by customer name
    """
    return OrderService.list_orders(customer_name)