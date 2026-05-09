from bot.orders import OrderManager

order_manager = OrderManager()

print("\n===== MARKET ORDER TEST =====")

response = order_manager.place_market_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001
)

if response["success"]:

    order_data = response["data"]

    print("Order placed successfully!")
    print(f"Order ID: {order_data.get('orderId')}")
    print(f"Status: {order_data.get('status')}")
    print(f"Executed Qty: {order_data.get('executedQty')}")

else:
    print("Order failed.")
    print(response["message"])