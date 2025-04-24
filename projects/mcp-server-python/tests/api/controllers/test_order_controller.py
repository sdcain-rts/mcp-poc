import pytest
import json
from httpx import AsyncClient
from fastapi import status

from models.order import OrderCreate, OrderUpdate, Order
from repositories.order_repository import OrderRepository


class TestOrderController:
    """Test cases for Order Controller endpoints"""
    
    @pytest.mark.asyncio
    async def test_create_order(self, async_client: AsyncClient):
        """Test creating an order through the API endpoint"""
        # Reset orders for this test
        OrderRepository._orders = {}
        
        # Prepare test data
        order_data = {
            "customer_name": "Jane Smith",
            "item": "Test Product",
            "quantity": 3
        }
        
        # Make API request
        response = await async_client.post("/orders/", json=order_data)
        
        # Assertions
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert "id" in data
        assert data["customer_name"] == order_data["customer_name"]
        assert data["item"] == order_data["item"]
        assert data["quantity"] == order_data["quantity"]
        assert data["status"] == "created"
        
        # Check if the order is in the repository
        order_id = data["id"]
        stored_order = OrderRepository.get(order_id)
        assert stored_order is not None
        assert stored_order.id == order_id
    
    @pytest.mark.asyncio
    async def test_get_order(self, async_client: AsyncClient, sample_order: Order):
        """Test getting an order by ID"""
        # Make API request
        response = await async_client.get(f"/orders/{sample_order.id}")
        
        # Assertions
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == sample_order.id
        assert data["customer_name"] == sample_order.customer_name
        assert data["item"] == sample_order.item
        assert data["quantity"] == sample_order.quantity
    
    @pytest.mark.asyncio
    async def test_get_nonexistent_order(self, async_client: AsyncClient):
        """Test getting a non-existent order"""
        # Reset orders for this test
        OrderRepository._orders = {}
        
        # Make API request for non-existent ID
        response = await async_client.get("/orders/999")
        
        # Assertions
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    @pytest.mark.asyncio
    async def test_update_order(self, async_client: AsyncClient, sample_order: Order):
        """Test updating an order"""
        # Prepare update data
        update_data = {"status": "processing"}
        
        # Make API request
        response = await async_client.put(f"/orders/{sample_order.id}", json=update_data)
        
        # Assertions
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == sample_order.id
        assert data["status"] == update_data["status"]
        
        # Check if the order is updated in the repository
        stored_order = OrderRepository.get(sample_order.id)
        assert stored_order.status == update_data["status"]
    
    @pytest.mark.asyncio
    async def test_update_nonexistent_order(self, async_client: AsyncClient):
        """Test updating a non-existent order"""
        # Reset orders for this test
        OrderRepository._orders = {}
        
        # Prepare update data
        update_data = {"status": "processing"}
        
        # Make API request for non-existent ID
        response = await async_client.put("/orders/999", json=update_data)
        
        # Assertions
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    @pytest.mark.asyncio
    async def test_delete_order(self, async_client: AsyncClient, sample_order: Order):
        """Test deleting an order"""
        # Make API request
        response = await async_client.delete(f"/orders/{sample_order.id}")
        
        # Assertions
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
        # Check if the order is deleted from the repository
        stored_order = OrderRepository.get(sample_order.id)
        assert stored_order is None
    
    @pytest.mark.asyncio
    async def test_delete_nonexistent_order(self, async_client: AsyncClient):
        """Test deleting a non-existent order"""
        # Reset orders for this test
        OrderRepository._orders = {}
        
        # Make API request for non-existent ID
        response = await async_client.delete("/orders/999")
        
        # Assertions
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    @pytest.mark.asyncio
    async def test_list_orders(self, async_client: AsyncClient):
        """Test listing all orders"""
        # Reset orders for this test
        OrderRepository._orders = {}
        
        # Create test orders
        for i in range(3):
            order_data = OrderCreate(
                customer_name=f"Customer {i}",
                item=f"Item {i}",
                quantity=i + 1
            )
            OrderRepository.create(order_data)
        
        # Make API request
        response = await async_client.get("/orders/")
        
        # Assertions
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 3
    
    @pytest.mark.asyncio
    async def test_list_orders_filtered(self, async_client: AsyncClient):
        """Test listing orders with filter parameters"""
        # Reset orders for this test
        OrderRepository._orders = {}
        
        # Create test orders with different customer names
        target_customer = "Target Customer"
        
        # Create orders with target customer name
        for i in range(2):
            OrderRepository.create(OrderCreate(
                customer_name=target_customer,
                item=f"Target Item {i}",
                quantity=i + 1
            ))
        
        # Create orders with different customer name
        for i in range(3):
            OrderRepository.create(OrderCreate(
                customer_name=f"Other Customer {i}",
                item=f"Other Item {i}",
                quantity=i + 1
            ))
        
        # Make API request with query parameter
        response = await async_client.get(f"/orders/?customer_name={target_customer}")
        
        # Assertions
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        for order in data:
            assert order["customer_name"] == target_customer