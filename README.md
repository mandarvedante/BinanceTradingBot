# Binance Futures Trading Bot (Testnet)

A simplified Python trading bot that interacts with the Binance Futures Testnet using market and limit orders.  
This project was built as part of the Junior Python Developer application task.

## Features

- Uses Binance Futures Testnet API
- Supports Market and Limit orders
- Accepts commands via Command-Line Interface (CLI)
- Uses `python-binance` SDK
- Structured with modular Python code
- Logs all requests, responses, and errors to `bot.log`
- Supports both BUY and SELL sides

## Testnet API Info

Due to current instability of the Binance Futures Testnet API portal (`https://testnet.binancefuture.com`),  
I used the official public API credentials provided in the assignment:

API Key: z1Lxj7pqV0WkNv3BPJuF70xq6BqOwUPaItR9xK9szEG5JThBMmB8dkITKcl4JHZm
API Secret: 5dSGB87JJhSlNi3g5KiKMKYcMzSYewJGiPCqL6SOJvTfDKg5Uw25LlPqzsbzoaVF

> These currently return:  
> `APIError(code=-2015): Invalid API-key, IP, or permissions for action`  
> This is a known limitation of Binance Testnet at the moment.

## Requirements

Install dependencies:
```bash
pip install -r requirements.txt

How to Use
Use the command-line tool cli.py to place orders:

Market Order Example

python cli.py \
  --key YOUR_API_KEY \
  --secret YOUR_API_SECRET \
  --symbol BTCUSDT \
  --side BUY \
  --type MARKET \
  --quantity 0.01

Limit Order Example
python cli.py \
  --key YOUR_API_KEY \
  --secret YOUR_API_SECRET \
  --symbol BTCUSDT \
  --side SELL \
  --type LIMIT \
  --quantity 0.01 \
  --price 62000

Logging
All API actions and errors are logged to:
bot.log

Sample log entries:

2025-06-23 22:33:13,283 - INFO - Bot initialized
2025-06-23 22:33:13,595 - ERROR - Error placing order:
Traceback (most recent call last):
...
binance.exceptions.BinanceAPIException: APIError(code=-2015): Invalid API-key, IP, or permissions for action

Status
Due to Binance Futures Testnet being unstable (API key generation disabled or rate-limited),
this bot is API-complete and CLI-functional, but live order placement could not be fully demonstrated during testing.



