import pytest
from fastapi import FastAPI, status
from httpx import AsyncClient
from typing import Dict, Any

from app.api.routes import setup_routes
from app.mcp.registry import create_mcp_registry
from repositories.order_repository import OrderRepository
from models.order import Order, OrderCreate


class TestOrderIntegration:
    """Integration tests covering the full stack of order functionality"""
    
    @pytest.fixture
    def app(self) -> FastAPI:
        """Create a fresh FastAPI application for testing."""
        app = FastAPI()
        setup_routes(app)
        return app
    
    @pytest.fixture
    async def mcp_client(self):
        """Create and return an MCP client registry for testing"""
        registry = create_mcp_registry()
        return registry
    
    def setup_method(self):
        """Reset repository before each test"""
        OrderRepository._orders = {}
    
    def teardown_method(self):
        """Clean up after each test"""
        OrderRepository._orders = {}
    
    @pytest.mark.asyncio
    async def test_create_order_integration(self, app: FastAPI, async_client: AsyncClient, mcp_client):
        """Test full flow: MCP tool creates order, then API retrieves it"""
        # Create order via MCP tool
        customer_name = "Integration Test Customer"
        item = "Integration Test Item"
        quantity = 5
        
        # Call MCP create_order tool
        create_order_tool = mcp_client.create_order
        order = create_order_tool(customer_name, item, quantity)
        
        # Verify order was created and has valid ID
        assert order.id is not None
        assert order.customer_name == customer_name
        
        # Then retrieve via API to ensure consistency
        response = await async_client.get(f"/orders/{order.id}")
        
        # Verify API response matches what MCP tool created
        assert response.status_code == status.HTTP_200_OK
        api_order = response.json()
        assert api_order["id"] == order.id
        assert api_order["customer_name"] == customer_name
        assert api_order["item"] == item
        assert api_order["quantity"] == quantity
    
    @pytest.mark.asyncio
    async def test_update_order_integration(self, app: FastAPI, async_client: AsyncClient, mcp_client):
        """Test updating order status via MCP and confirming via API"""
        # First create order via API
        order_data = {
            "customer_name": "Integration Update Test",
            "item": "Test Product",
            "quantity": 2
        }
        
        # Create via API
        response = await async_client.post("/orders/", json=order_data)
        assert response.status_code == status.HTTP_201_CREATED
        order_id = response.json()["id"]
        
        # Update via MCP tool
        new_status = "delivered"
        update_order_tool = mcp_client.update_order
        updated_order = update_order_tool(order_id, new_status)
        
        # Verify update happened correctly through MCP
        assert updated_order.status == new_status
        
        # Then verify API reflects the change
        response = await async_client.get(f"/orders/{order_id}")
        assert response.status_code == status.HTTP_200_OK
        api_order = response.json()
        assert api_order["status"] == new_status
    
    @pytest.mark.asyncio
    async def test_list_orders_integration(self, app: FastAPI, async_client: AsyncClient, mcp_client):
        """Test creating orders via API and listing via MCP tool"""
        # Create several orders via API
        test_customers = ["Customer A", "Customer B", "Customer A"]
        
        for i, customer in enumerate(test_customers):
            order_data = {
                "customer_name": customer,
                "item": f"Item {i}",
                "quantity": i + 1
            }
            response = await async_client.post("/orders/", json=order_data)
            assert response.status_code == status.HTTP_201_CREATED
        
        # List all orders via MCP tool
        list_orders_tool = mcp_client.list_orders
        all_orders = list_orders_tool()
        
        # Verify we get all orders
        assert len(all_orders) == 3
        
        # Filter orders for Customer A
        filtered_orders = list_orders_tool("Customer A")
        
        # Verify filter works
        assert len(filtered_orders) == 2
        for order in filtered_orders:
            assert order.customer_name == "Customer A"
    
    @pytest.mark.asyncio
    async def test_delete_order_integration(self, app: FastAPI, async_client: AsyncClient, mcp_client):
        """Test deleting an order via MCP tool and confirming via API"""
        # Create order via API
        order_data = {
            "customer_name": "Delete Test Customer",
            "item": "Test Item",
            "quantity": 1
        }
        
        # Create via API
        response = await async_client.post("/orders/", json=order_data)
        assert response.status_code == status.HTTP_201_CREATED
        order_id = response.json()["id"]
        
        # Verify order exists via API
        response = await async_client.get(f"/orders/{order_id}")
        assert response.status_code == status.HTTP_200_OK
        
        # Delete via MCP tool
        delete_order_tool = mcp_client.delete_order
        result = delete_order_tool(order_id)
        
        # Verify deletion reported success
        assert result is True
        
        # Verify deletion via API
        response = await async_client.get(f"/orders/{order_id}")
        assert response.status_code == status.HTTP_404_NOT_FOUND