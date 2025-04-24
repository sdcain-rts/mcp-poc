import pytest
import unittest.mock as mock
from typing import List, Dict, Any, Optional

from app.mcp.tools.order_tools import register_order_tools
from app.services.order_service import OrderService
from models.order import Order


class MockFastMCP:
    """Mock FastMCP client for testing tool registration"""
    
    def __init__(self):
        self.registered_tools = {}
    
    def tool(self, name: str, description: str):
        """Decorator mock that captures the registered function"""
        def decorator(func):
            self.registered_tools[name] = func
            return func
        return decorator


class TestOrderTools:
    """Test suite for MCP order tools"""
    
    @pytest.fixture
    def mcp_mock(self):
        """Create a mock MCP client with registered tools"""
        mcp = MockFastMCP()
        register_order_tools(mcp)
        return mcp
    
    def test_create_order_tool(self, mcp_mock):
        """Test the create_order MCP tool"""
        # Setup mock return from service layer
        mock_order = Order(
            id="test-id-1",
            customer_name="Test Customer",
            item="Test Item",
            quantity=2,
            status="created"
        )
        
        # Mock the service call
        with mock.patch.object(
            OrderService, 'create_order', return_value=mock_order
        ) as mock_service:
            # Get the registered tool function
            create_order_tool = mcp_mock.registered_tools["create_order"]
            
            # Call the tool
            result = create_order_tool("Test Customer", "Test Item", 2)
            
            # Verify service was called with correct args
            mock_service.assert_called_once_with("Test Customer", "Test Item", 2)
            
            # Verify result
            assert result == mock_order
            assert result.id == "test-id-1"
            assert result.customer_name == "Test Customer"
            assert result.item == "Test Item"
            assert result.quantity == 2
    
    def test_get_order_tool(self, mcp_mock):
        """Test the get_order MCP tool"""
        # Setup mock return value
        mock_order = Order(
            id="test-id-2",
            customer_name="Test Customer",
            item="Test Item",
            quantity=1,
            status="created"
        )
        
        # Mock the service call
        with mock.patch.object(
            OrderService, 'get_order', return_value=mock_order
        ) as mock_service:
            # Get the registered tool function
            get_order_tool = mcp_mock.registered_tools["get_order"]
            
            # Call the tool
            result = get_order_tool("test-id-2")
            
            # Verify service was called with correct args
            mock_service.assert_called_once_with("test-id-2")
            
            # Verify result
            assert result == mock_order
    
    def test_get_nonexistent_order_tool(self, mcp_mock):
        """Test the get_order MCP tool when order doesn't exist"""
        # Mock the service call to return None (order not found)
        with mock.patch.object(
            OrderService, 'get_order', return_value=None
        ) as mock_service:
            # Get the registered tool function
            get_order_tool = mcp_mock.registered_tools["get_order"]
            
            # Call the tool
            result = get_order_tool("non-existent-id")
            
            # Verify service was called with correct args
            mock_service.assert_called_once_with("non-existent-id")
            
            # Verify result is None
            assert result is None
    
    def test_update_order_tool(self, mcp_mock):
        """Test the update_order MCP tool"""
        # Setup mock return value
        mock_updated_order = Order(
            id="test-id-3",
            customer_name="Test Customer",
            item="Test Item",
            quantity=1,
            status="shipped"  # Updated status
        )
        
        # Mock the service call
        with mock.patch.object(
            OrderService, 'update_order_status', return_value=mock_updated_order
        ) as mock_service:
            # Get the registered tool function
            update_order_tool = mcp_mock.registered_tools["update_order"]
            
            # Call the tool
            result = update_order_tool("test-id-3", "shipped")
            
            # Verify service was called with correct args
            mock_service.assert_called_once_with("test-id-3", "shipped")
            
            # Verify result
            assert result == mock_updated_order
            assert result.status == "shipped"
    
    def test_delete_order_tool(self, mcp_mock):
        """Test the delete_order MCP tool"""
        # Mock the service call
        with mock.patch.object(
            OrderService, 'delete_order', return_value=True
        ) as mock_service:
            # Get the registered tool function
            delete_order_tool = mcp_mock.registered_tools["delete_order"]
            
            # Call the tool
            result = delete_order_tool("test-id-4")
            
            # Verify service was called with correct args
            mock_service.assert_called_once_with("test-id-4")
            
            # Verify result
            assert result is True
    
    def test_list_orders_tool(self, mcp_mock):
        """Test the list_orders MCP tool"""
        # Setup mock return value - list of orders
        mock_orders = [
            Order(id="test-id-1", customer_name="Customer A", item="Item 1", quantity=1, status="created"),
            Order(id="test-id-2", customer_name="Customer B", item="Item 2", quantity=2, status="shipped"),
            Order(id="test-id-3", customer_name="Customer A", item="Item 3", quantity=3, status="delivered")
        ]
        
        # Mock the service call
        with mock.patch.object(
            OrderService, 'list_orders', return_value=mock_orders
        ) as mock_service:
            # Get the registered tool function
            list_orders_tool = mcp_mock.registered_tools["list_orders"]
            
            # Call the tool without filter
            result = list_orders_tool()
            
            # Verify service was called with correct args
            mock_service.assert_called_with(None)
            
            # Verify result
            assert result == mock_orders
            assert len(result) == 3
    
    def test_list_orders_tool_with_filter(self, mcp_mock):
        """Test the list_orders MCP tool with customer filter"""
        # Setup mock return value - filtered list
        mock_filtered_orders = [
            Order(id="test-id-1", customer_name="Customer A", item="Item 1", quantity=1, status="created"),
            Order(id="test-id-3", customer_name="Customer A", item="Item 3", quantity=3, status="delivered")
        ]
        
        # Mock the service call
        with mock.patch.object(
            OrderService, 'list_orders', return_value=mock_filtered_orders
        ) as mock_service:
            # Get the registered tool function
            list_orders_tool = mcp_mock.registered_tools["list_orders"]
            
            # Call the tool with filter
            result = list_orders_tool("Customer A")
            
            # Verify service was called with correct args
            mock_service.assert_called_with("Customer A")
            
            # Verify result
            assert result == mock_filtered_orders
            assert len(result) == 2
            for order in result:
                assert order.customer_name == "Customer A"