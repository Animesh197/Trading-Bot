import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Load environment variables from .env
load_dotenv()


class BinanceFuturesClient:
    """
    Handles Binance Futures Testnet client setup and connection.
    """

    def __init__(self):
        """
        Initialize Binance client using API credentials.
        """

        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        # Validate credentials
        if not self.api_key or not self.api_secret:
            raise ValueError(
                "Missing Binance API credentials. Check your .env file."
            )

        # Initialize Binance client
        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
            testnet=True
        )

        # Configure Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def ping_server(self):
        """
        Test connectivity with Binance server.
        """

        try:
            response = self.client.futures_ping()
            return {
                "success": True,
                "message": "Successfully connected to Binance Futures Testnet.",
                "response": response
            }

        except BinanceAPIException as api_error:
            return {
                "success": False,
                "message": f"Binance API Error: {str(api_error)}"
            }

        except Exception as error:
            return {
                "success": False,
                "message": f"Unexpected Error: {str(error)}"
            }

    def get_client(self):
        """
        Return initialized Binance client instance.
        """
        return self.client