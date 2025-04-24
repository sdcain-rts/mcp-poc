from fastapi import APIRouter, FastAPI
from app.api.controllers.order_controller import router as order_router

# Main API router
api_router = APIRouter()

# Include all controllers
api_router.include_router(order_router)

# Add more controllers as needed
# api_router.include_router(user_router)
# api_router.include_router(product_router)

def setup_routes(app: FastAPI) -> None:
    """
    Configure routes for the FastAPI application.
    This function is used by the test fixtures.
    """
    app.include_router(api_router)
    return app