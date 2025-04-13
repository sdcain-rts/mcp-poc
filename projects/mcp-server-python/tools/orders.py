from typing import Optional
from modelcontext import define_tool

# In-memory store for orders
orders = {}

@define_tool
def create_order(customer_name: str, item: str, quantity: int):
    """
    Create a new order.
    """
    order_id = str(len(orders) + 1)
    order = {
        "id": order_id,
        "customer_name": customer_name,
        "item": item,
        "quantity": quantity,
        "status": "created"
    }
    orders[order_id] = order
    return order

@define_tool
def get_order(order_id: str):
    """
    Retrieve an order by ID.
    """
    return orders.get(order_id, {"error": "Order not found"})

@define_tool
def update_order(order_id: str, status: str):
    """
    Update the status of an order.
    """
    if order_id in orders:
        orders[order_id]["status"] = status
        return orders[order_id]
    return {"error": "Order not found"}

@define_tool
def delete_order(order_id: str):
    """
    Delete an order by ID.
    """
    if order_id in orders:
        del orders[order_id]
        return {"success": True}
    return {"error": "Order not found"}

@define_tool
def list_orders(customer_name: Optional[str] = None):
    """
    List all orders, optionally filtered by customer name.
    """
    if customer_name:
        return [order for order in orders.values() if order["customer_name"] == customer_name]
    return list(orders.values())

# List of tools to be included in the MCP app
tools = [
    create_order,
    get_order,
    update_order,
    delete_order,
    list_orders
]