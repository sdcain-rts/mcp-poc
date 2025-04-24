import logging
from fastapi import FastAPI
from fastmcp import FastMCP

from app.api.routes import api_router
from app.mcp.registry import register_all_tools

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("main")

# Create FastAPI application
app = FastAPI(
    title="Order Management API",
    description="REST API with MCP integration for order management",
    version="1.0.0"
)

# Include API routers
app.include_router(api_router, prefix="/api")

# Create and configure MCP instance
mcp = FastMCP(app)

# Register all MCP tools
register_all_tools(mcp)

@app.get("/")
async def root():
    """Root endpoint for API health check"""
    return {"status": "online", "service": "Order Management API"}

# Startup event
@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the Order Management API service")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down the Order Management API service")