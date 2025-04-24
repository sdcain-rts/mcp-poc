import pytest
from httpx import AsyncClient
from typing import AsyncGenerator
from fastapi import FastAPI

from models.order import OrderCreate, Order
from app.api.routes import setup_routes
from repositories.order_repository import OrderRepository


@pytest.fixture
def app() -> FastAPI:
    """
    Create a fresh FastAPI application for testing.
    """
    app = FastAPI()
    setup_routes(app)
    return app


@pytest.fixture
async def async_client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """
    Create an async test client that uses the FastAPI app.
    """
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client


@pytest.fixture
def sample_order() -> Order:
    """
    Create and return a sample order for testing.
    """
    # Clear the repository to ensure clean state
    OrderRepository._orders = {}
    
    # Create a sample order
    order_data = OrderCreate(
        customer_name="Test Customer",
        item="Test Item",
        quantity=2
    )
    order = OrderRepository.create(order_data)
    return order