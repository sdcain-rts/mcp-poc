import logging
from typing import List, Optional, Dict, Any

from models.order import Order, OrderCreate, OrderUpdate
from repositories.order_repository import OrderRepository

# Configure logging
logger = logging.getLogger("order_service")

class OrderService:
    """Service for order business logic"""
    
    @staticmethod
    def create_order(customer_name: str, item: str, quantity: int) -> Order:
        """Create a new order with the given details"""
        logger.info(f"Creating order - Customer: {customer_name}, Item: {item}, Quantity: {quantity}")
        
        # Validate and create order
        order_data = OrderCreate(
            customer_name=customer_name,
            item=item,
            quantity=quantity
        )
        
        # Use repository to create the order
        order = OrderRepository.create(order_data)
        return order
    
    @staticmethod
    def get_order(order_id: str) -> Dict[str, Any]:
        """Get an order by ID or return error"""
        logger.info(f"Getting order - ID: {order_id}")
        
        order = OrderRepository.get(order_id)
        if order:
            return order.dict()
        return {"error": "Order not found"}
    
    @staticmethod
    def update_order_status(order_id: str, status: str) -> Dict[str, Any]:
        """Update an order's status"""
        logger.info(f"Updating order - ID: {order_id}, Status: {status}")
        
        # Validate and update order
        order_update = OrderUpdate(status=status)
        
        # Use repository to update the order
        updated_order = OrderRepository.update(order_id, order_update)
        if updated_order:
            return updated_order.dict()
        return {"error": "Order not found"}
    
    @staticmethod
    def delete_order(order_id: str) -> Dict[str, Any]:
        """Delete an order by ID"""
        logger.info(f"Deleting order - ID: {order_id}")
        
        result = OrderRepository.delete(order_id)
        if result:
            return {"success": True}
        return {"error": "Order not found"}
    
    @staticmethod
    def list_orders(customer_name: Optional[str] = None) -> List[Dict[str, Any]]:
        """List all orders, optionally filtered by customer"""
        if customer_name:
            logger.info(f"Listing orders for customer: {customer_name}")
            orders = OrderRepository.list_by_customer(customer_name)
        else:
            logger.info("Listing all orders")
            orders = OrderRepository.list_all()
            
        # Convert to dict for serialization
        return [order.dict() for order in orders]