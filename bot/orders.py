from binance.exceptions import BinanceAPIException

from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logger

# Initialize logger
logger = setup_logger()


class OrderManager:
    """
    Handles Binance Futures order placement logic.
    """

    def __init__(self):
        """
        Initialize Binance client.
        """

        self.client = BinanceFuturesClient().get_client()

    def place_market_order(
        self,
        symbol: str,
        side: str,
        quantity: float
    ):
        """
        Place MARKET order.
        """

        try:
            logger.info(
                f"Sending MARKET order | "
                f"Symbol={symbol} | "
                f"Side={side} | "
                f"Quantity={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(
                f"MARKET order successful | "
                f"OrderID={response.get('orderId')} | "
                f"Status={response.get('status')}"
            )

            return {
                "success": True,
                "data": response
            }

        except BinanceAPIException as api_error:

            logger.error(
                f"Binance API Error while placing MARKET order: "
                f"{str(api_error)}"
            )

            return {
                "success": False,
                "message": f"Binance API Error: {str(api_error)}"
            }

        except Exception as error:

            logger.error(
                f"Unexpected Error while placing MARKET order: "
                f"{str(error)}"
            )

            return {
                "success": False,
                "message": f"Unexpected Error: {str(error)}"
            }

    def place_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float
    ):
        """
        Place LIMIT order.
        """

        try:
            logger.info(
                f"Sending LIMIT order | "
                f"Symbol={symbol} | "
                f"Side={side} | "
                f"Quantity={quantity} | "
                f"Price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(
                f"LIMIT order successful | "
                f"OrderID={response.get('orderId')} | "
                f"Status={response.get('status')}"
            )

            return {
                "success": True,
                "data": response
            }

        except BinanceAPIException as api_error:

            logger.error(
                f"Binance API Error while placing LIMIT order: "
                f"{str(api_error)}"
            )

            return {
                "success": False,
                "message": f"Binance API Error: {str(api_error)}"
            }

        except Exception as error:

            logger.error(
                f"Unexpected Error while placing LIMIT order: "
                f"{str(error)}"
            )

            return {
                "success": False,
                "message": f"Unexpected Error: {str(error)}"
            }