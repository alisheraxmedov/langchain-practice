from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Optional

class OrderItem(BaseModel):
    name: str = Field(description="Name of the product")
    quantity: int = Field(description="Quantity ordered")

class OrderDetails(BaseModel):
    order_id: str = Field(description="The unique ID of the order")
    status: str = Field(description="Current status: Processing, Shipped, Delivered")
    items: List[OrderItem] = Field(description="List of items in the order")
    eta: Optional[str] = Field(description="Estimated time of arrival if available")

class UserProfile(BaseModel):
    user_id: str = Field(description="Unique user ID")
    name: str = Field(description="Full name of the user")
    is_premium: bool = Field(description="Whether the user has premium status")
