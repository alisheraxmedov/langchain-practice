from langchain_core.tools import tool

@tool
def search_order(order_id: str) -> str:
    """
    Search for an order status and details by its Order ID.
    Useful for checking shipping status or item details.
    """
    mock_orders = {
        "ORD-001": "Order ORD-001: Shipped. Items: Wireless Keyboard. ETA: 2 days.",
        "ORD-002": "Order ORD-002: Processing. Items: Gaming Mouse. ETA: Unknown.",
        "ORD-003": "Order ORD-003: Delivered. Items: Monitor 24-inch.",
    }
    return mock_orders.get(order_id, f"Order {order_id} not found.")

@tool
def get_user_info(user_id: str) -> str:
    """
    Retrieve user profile information by User ID.
    Useful for personalizing responses or verifying identity.
    """
    mock_users = {
        "U101": "User: Alisher (Premium). Email: alisher@example.com",
        "U102": "User: John Doe (Standard). Email: john@test.com",
    }
    return mock_users.get(user_id, f"User {user_id} not found.")
