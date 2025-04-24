import logging
from typing import Optional
from fastmcp import FastMCP

from app.services.order_service import OrderService

# Configure logging
logger = logging.getLogger("mcp_order_tools")

def register_order_tools(mcp: FastMCP):
    """Register order-related MCP tools"""
    
    @mcp.tool(
        name="create_order",
        description="Create a new order for a specific customer with a given item and quantity."
    )
    def create_order(customer_name: str, item: str, quantity: int):
        logger.info(f"MCP Tool called: create_order - Customer: {customer_name}, Item: {item}, Quantity: {quantity}")
        # Reuse the service layer for business logic
        return OrderService.create_order(customer_name, item, quantity)

    @mcp.tool(
        name="get_order",
        description="Retrieve an order by its ID."
    )
    def get_order(order_id: str):
        logger.info(f"MCP Tool called: get_order - Order ID: {order_id}")
        # Reuse the service layer
        return OrderService.get_order(order_id)

    @mcp.tool(
        name="update_order",
        description="Update the status of an existing order by ID. Example statuses: 'shipped', 'cancelled', etc."
    )
    def update_order(order_id: str, status: str):
        logger.info(f"MCP Tool called: update_order - Order ID: {order_id}, New Status: {status}")
        # Reuse the service layer
        return OrderService.update_order_status(order_id, status)

    @mcp.tool(
        name="delete_order",
        description="Delete an order by its ID."
    )
    def delete_order(order_id: str):
        logger.info(f"MCP Tool called: delete_order - Order ID: {order_id}")
        # Reuse the service layer
        return OrderService.delete_order(order_id)

    @mcp.tool(
        name="list_orders",
        description="List all orders. Optionally filter by customer name using the 'customer_name' argument."
    )
    def list_orders(customer_name: Optional[str] = None):
        logger.info(f"MCP Tool called: list_orders - Filter by customer: {customer_name if customer_name else 'None'}")
        # Reuse the service layer
        return OrderService.list_orders(customer_name)