import pytest
from typing import Dict, List, Optional

from models.order import OrderCreate, OrderUpdate, Order
from app.services.order_service import OrderService
from repositories.order_repository import OrderRepository


class TestOrderService:
    """Test cases for Order Service"""
    
    def setup_method(self):
        """Reset the repository before each test"""
        OrderRepository._orders = {}
    
    def teardown_method(self):
        """Clean up after each test"""
        OrderRepository._orders = {}
    
    def test_create_order(self):
        """Test creating an order through the service"""
        # Prepare test data
        order_data = OrderCreate(
            customer_name="Jane Smith",
            item="Test Product",
            quantity=3
        )
        
        # Create order through service
        order = OrderService.create_order(order_data)
        
        # Assertions
        assert order.id is not None
        assert order.customer_name == order_data.customer_name
        assert order.item == order_data.item
        assert order.quantity == order_data.quantity
        assert order.status == "created"
        
        # Check if the order is in the repository
        stored_order = OrderRepository.get(order.id)
        assert stored_order is not None
        assert stored_order.id == order.id
    
    def test_get_order(self):
        """Test retrieving an order by ID"""
        # Create a test order
        order_data = OrderCreate(
            customer_name="Test Customer",
            item="Test Item",
            quantity=1
        )
        created_order = OrderRepository.create(order_data)
        
        # Get the order through the service
        order = OrderService.get_order(created_order.id)
        
        # Assertions
        assert order is not None
        assert order.id == created_order.id
        assert order.customer_name == created_order.customer_name
        assert order.item == created_order.item
        assert order.quantity == created_order.quantity
    
    def test_get_nonexistent_order(self):
        """Test retrieving a non-existent order"""
        # Try to get a non-existent order
        order = OrderService.get_order(999)
        
        # Assertion
        assert order is None
    
    def test_update_order(self):
        """Test updating an order"""
        # Create a test order
        order_data = OrderCreate(
            customer_name="Test Customer",
            item="Test Item",
            quantity=1
        )
        created_order = OrderRepository.create(order_data)
        
        # Update data
        update_data = OrderUpdate(status="processing")
        
        # Update the order through the service
        updated_order = OrderService.update_order(created_order.id, update_data)
        
        # Assertions
        assert updated_order is not None
        assert updated_order.id == created_order.id
        assert updated_order.status == "processing"
        
        # Check if the order is updated in the repository
        stored_order = OrderRepository.get(created_order.id)
        assert stored_order.status == "processing"
    
    def test_delete_order(self):
        """Test deleting an order"""
        # Create a test order
        order_data = OrderCreate(
            customer_name="Test Customer",
            item="Test Item",
            quantity=1
        )
        created_order = OrderRepository.create(order_data)
        
        # Delete the order through the service
        result = OrderService.delete_order(created_order.id)
        
        # Assertions
        assert result is True
        
        # Check if the order is deleted from the repository
        stored_order = OrderRepository.get(created_order.id)
        assert stored_order is None
    
    def test_list_orders(self):
        """Test listing all orders"""
        # Create test orders
        for i in range(3):
            order_data = OrderCreate(
                customer_name=f"Customer {i}",
                item=f"Item {i}",
                quantity=i + 1
            )
            OrderRepository.create(order_data)
        
        # List orders through the service
        orders = OrderService.list_orders()
        
        # Assertions
        assert len(orders) == 3
        
    def test_list_orders_filtered(self):
        """Test listing orders with filter"""
        # Create test orders with different customer names
        target_customer = "Target Customer"
        
        # Create orders with target customer name
        for i in range(2):
            order_data = OrderCreate(
                customer_name=target_customer,
                item=f"Target Item {i}",
                quantity=i + 1
            )
            OrderRepository.create(order_data)
        
        # Create orders with different customer name
        for i in range(3):
            order_data = OrderCreate(
                customer_name=f"Other Customer {i}",
                item=f"Other Item {i}",
                quantity=i + 1
            )
            OrderRepository.create(order_data)
        
        # List orders with filter
        filtered_orders = OrderService.list_orders(customer_name=target_customer)
        
        # Assertions
        assert len(filtered_orders) == 2
        for order in filtered_orders:
            assert order.customer_name == target_customer