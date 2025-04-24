import logging
from typing import Dict, List, Optional, Any
from models.order import Order, OrderCreate, OrderUpdate

# Configure logging
logger = logging.getLogger("order_repository")

class OrderRepository:
    """Repository for order data operations"""
    
    # In-memory store (would be replaced with a database in production)
    _orders: Dict[str, Dict[str, Any]] = {}
    
    @classmethod
    def create(cls, order_data: OrderCreate) -> Order:
        """Create a new order in the repository"""
        order_id = str(len(cls._orders) + 1)
        
        # Convert to dict for storage
        order_dict = order_data.dict()
        order_dict["id"] = order_id
        order_dict["status"] = "created"
        
        # Store in repository
        cls._orders[order_id] = order_dict
        logger.info(f"Order created: {order_dict}")
        
        # Return as Pydantic model
        return Order(**order_dict)
    
    @classmethod
    def get(cls, order_id: str) -> Optional[Order]:
        """Get an order by ID"""
        order_dict = cls._orders.get(order_id)
        if order_dict:
            logger.info(f"Order retrieved: {order_dict}")
            return Order(**order_dict)
        logger.warning(f"Order not found: {order_id}")
        return None
    
    @classmethod
    def update(cls, order_id: str, order_update: OrderUpdate) -> Optional[Order]:
        """Update an order's status"""
        if order_id in cls._orders:
            # Update only the status field
            cls._orders[order_id]["status"] = order_update.status
            updated_order = cls._orders[order_id]
            logger.info(f"Order updated: {updated_order}")
            return Order(**updated_order)
        logger.warning(f"Order not found for update: {order_id}")
        return None
    
    @classmethod
    def delete(cls, order_id: str) -> bool:
        """Delete an order by ID"""
        if order_id in cls._orders:
            del cls._orders[order_id]
            logger.info(f"Order deleted: {order_id}")
            return True
        logger.warning(f"Order not found for deletion: {order_id}")
        return False
    
    @classmethod
    def list_all(cls) -> List[Order]:
        """List all orders"""
        orders = [Order(**order) for order in cls._orders.values()]
        logger.info(f"All orders retrieved, count: {len(orders)}")
        return orders
    
    @classmethod
    def list_by_customer(cls, customer_name: str) -> List[Order]:
        """List orders for a specific customer"""
        orders = [
            Order(**order) 
            for order in cls._orders.values() 
            if order["customer_name"].lower() == customer_name.lower()
        ]
        logger.info(f"Orders filtered by customer: {customer_name}, found {len(orders)} orders")
        return orders