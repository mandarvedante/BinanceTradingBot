import argparse 
from bot import BasicBot
def get_user_input():
    parser = argparse.ArgumentParser(description = "Binance Trading Bot")
    parser.add_argument('--key',required = True)
    parser.add_argument('--secret', required = True)
    parser.add_argument('--symbol', default = 'BTCUSDT')
    parser.add_argument('--side', choices = ['BUY', 'SELL'], required = True)
    parser.add_argument('--type', choices = ['MARKET', 'LIMIT'], required = True)
    parser.add_argument('--quantity', type = float, required = True)
    parser.add_argument('--price', type = float, help = "Required for LIMIT orders")
    return parser.parse_args()
if __name__ == '__main__':
    args = get_user_input()

    bot = BasicBot(args.key, args.secret)
    result = bot.place_order(args.symbol, args.side, args.type, args.qty, args.price)
    if result:
        print(" ✅ Order placed successfully")
    else:
        print(" ❌ Failed to place order.")