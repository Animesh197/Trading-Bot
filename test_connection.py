from bot.client import BinanceFuturesClient

# Initialize client
binance_client = BinanceFuturesClient()

# Test server connection
result = binance_client.ping_server()

print("\n===== CONNECTION TEST =====")

if result["success"]:
    print("STATUS: SUCCESS")
    print(result["message"])
else:
    print("STATUS: FAILED")
    print(result["message"])