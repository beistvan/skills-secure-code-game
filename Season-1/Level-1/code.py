from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ORDER_AMOUNT = 1e6

def validorder(order: Order):
    total_payments = 0.0
    total_products = 0.0

    for item in order.items:
        if item.type == 'payment':
            total_payments += float(item.amount)
        elif item.type == 'product':
            if item.amount < 0 or item.quantity < 0:
                return "Invalid product amount or quantity"
            total_products += float(item.amount) * int(item.quantity)
        else:
            return f"Invalid item type: {item.type}"

    if total_products > MAX_ORDER_AMOUNT:
        return "Total amount payable for an order exceeded"

    net = total_payments - total_products

    if abs(net) > 0.001:
        return f"Order ID: {order.id} - Payment imbalance: ${net:.2f}"
    else:
        return f"Order ID: {order.id} - Full payment received!"