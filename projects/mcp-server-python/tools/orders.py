from typing import Optional
from mcp.server.fastmcp import FastMCP, Context

# In-memory store
orders = {}

def register_tools(mcp: FastMCP):
    @mcp.tool(
        name="create_order",
        description="Create a new order for a specific customer with a given item and quantity."
    )
    def create_order(ctx: Context, customer_name: str, item: str, quantity: int):
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

    @mcp.tool(
        name="get_order",
        description="Retrieve an order by its ID."
    )
    def get_order(ctx: Context, order_id: str):
        return orders.get(order_id, {"error": "Order not found"})

    @mcp.tool(
        name="update_order",
        description="Update the status of an existing order by ID. Example statuses: 'shipped', 'cancelled', etc."
    )
    def update_order(ctx: Context, order_id: str, status: str):
        if order_id in orders:
            orders[order_id]["status"] = status
            return orders[order_id]
        return {"error": "Order not found"}

    @mcp.tool(
        name="delete_order",
        description="Delete an order by its ID."
    )
    def delete_order(ctx: Context, order_id: str):
        if order_id in orders:
            del orders[order_id]
            return {"success": True}
        return {"error": "Order not found"}

    @mcp.tool(
        name="list_orders",
        description="List all orders. Optionally filter by customer name using the 'customer_name' argument."
    )
    def list_orders(ctx: Context, customer_name: Optional[str] = None):
        if customer_name:
            return [o for o in orders.values() if o["customer_name"].lower() == customer_name.lower()]
        return list(orders.values())
