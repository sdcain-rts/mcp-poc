from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class OrderBase(BaseModel):
    """Base schema for Order data"""
    customer_name: str = Field(..., description="Name of the customer placing the order")
    item: str = Field(..., description="Name of the ordered item")
    quantity: int = Field(..., gt=0, description="Quantity of the ordered item")


class OrderCreate(OrderBase):
    """Schema for creating a new order"""
    pass


class OrderUpdate(BaseModel):
    """Schema for updating an existing order"""
    status: str = Field(..., description="New status for the order")


class Order(OrderBase):
    """Schema for a complete order record"""
    id: str = Field(..., description="Unique identifier for the order")
    status: str = Field(default="created", description="Current status of the order")
    created_at: datetime = Field(default_factory=datetime.now, description="When the order was created")

    class Config:
        """Pydantic configuration"""
        schema_extra = {
            "example": {
                "id": "1",
                "customer_name": "John Doe",
                "item": "Widget",
                "quantity": 3,
                "status": "created",
                "created_at": "2025-04-23T15:30:00"
            }
        }


class OrderResponse(Order):
    """Schema for API responses"""
    pass