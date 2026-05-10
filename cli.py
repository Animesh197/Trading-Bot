import argparse

from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    ValidationError
)


def main():
    """
    Main CLI entry point.
    """

    print("\n=================================")
    print(" Binance Futures Testnet Bot ")
    print("=================================")

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    # CLI arguments
    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (example: BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="Order side: BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="Order type: MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        help="Order quantity (example: 0.001)"
    )

    parser.add_argument(
        "--price",
        required=False,
        help="Limit price (required for LIMIT orders)"
    )

    # Parse arguments
    args = parser.parse_args()

    try:
        # Validate inputs
        symbol = validate_symbol(args.symbol)

        side = validate_side(args.side)

        order_type = validate_order_type(args.type)

        quantity = validate_quantity(args.quantity)

        price = validate_price(args.price, order_type)

        # Initialize order manager
        order_manager = OrderManager()

        print("\n===== ORDER REQUEST SUMMARY =====")

        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if price:
            print(f"Price       : {price}")

        print("=================================\n")

        # Place MARKET order
        if order_type == "MARKET":

            response = order_manager.place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity
            )

        # Place LIMIT order
        else:

            response = order_manager.place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price
            )

        # Handle response
        if response["success"]:

            order_data = response["data"]

            print("===== ORDER RESPONSE =====")

            print(
                f"Order ID       : "
                f"{order_data.get('orderId')}"
            )

            print(
                f"Status         : "
                f"{order_data.get('status')}"
            )

            status = order_data.get("status")

            if status == "NEW":
                print(
                    "Note           : "
                    "Order created and waiting for execution."
                )

            elif status == "FILLED":
                print(
                    "Note           : "
                    "Order executed successfully."
                )

            print(
                f"Executed Qty   : "
                f"{order_data.get('executedQty')}"
            )

            avg_price = order_data.get("avgPrice")

            if avg_price and avg_price != "0.00":
                print(f"Average Price  : {avg_price}")

            print("\nOrder placed successfully!")
            print("Request completed successfully.")

            print("\n=================================")

        else:
            print("\nOrder placement failed.")
            print(response["message"])

    except ValidationError as validation_error:

        print("\n Validation Error")
        print(f"→ {validation_error}")

    except Exception as error:

        print("\n Unexpected Error")
        print(f"→ {str(error)}")


if __name__ == "__main__":
    main()