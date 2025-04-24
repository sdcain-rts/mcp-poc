import logging
from fastmcp import FastMCP
from app.mcp.tools.order_tools import register_order_tools

# Configure logging
logger = logging.getLogger("mcp_registry")

def register_all_tools(mcp: FastMCP):
    """Register all MCP tools from various modules"""
    logger.info("Registering all MCP tools")
    
    # Register order tools
    register_order_tools(mcp)
    logger.info("Order tools registered")
    
    # Register additional tool sets as needed
    # register_user_tools(mcp)
    # register_product_tools(mcp)
    
    logger.info("All MCP tools registered successfully")