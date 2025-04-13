def create_order(orders, customer_name, item, quantity):
    order_id = str(len(orders) + 1)
    orders[order_id] = {
        "customer_name": customer_name,
        "item": item,
        "quantity": quantity
    }
    return {"order_id": order_id, "status": "created"}

def get_order(orders, order_id):
    return orders.get(order_id, {"error": "Order not found"})