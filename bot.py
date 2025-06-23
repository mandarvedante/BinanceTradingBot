from binance.client import Client
from binance.enums import *
from logger import get_logger

class BasicBot:
    def __init__(self, api_key, api_secret, testnet = True):
        self.logger = get_logger()
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        self.logger.info("Bot initialized")
    def place_order(self, symbol, side, order_type, quantity, price = None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol = symbol,
                    side = SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type = ORDER_TYPE_MARKET,
                    quantity = quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol = symbol,
                    side = SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type = ORDER_TYPE_LIMIT,
                    quantity = quantity,
                    price = price,
                    timeInForce=TIME_IN_FORCE_GTC
                )
            else:
                self.logger.error("Invalid order type.")
                return None
            self.logger.info(f"Order placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Error placing order: {str(e)}")
            return None