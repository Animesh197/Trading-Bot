# Binance Futures Testnet Trading Bot

A simplified Python-based trading bot for Binance Futures Testnet (USDT-M) that supports MARKET and LIMIT orders through a command-line interface.

---

# Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL sides
- Binance Futures Testnet integration
- Input validation
- Structured logging
- Exception handling
- Clean modular architecture
- Command-line interface using argparse

---

# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   ├── market_order.log
│   └── limit_order.log
│
├── cli.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-github-repo-url>
cd trading_bot
```

---

## 2. Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in project root:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

Use Binance Futures Testnet credentials:
https://testnet.binancefuture.com

---

# Usage

## MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

---

# Sample Output

```text
===== ORDER REQUEST SUMMARY =====

Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001

=================================

===== ORDER RESPONSE =====

Order ID       : 13124312473
Status         : NEW
Note           : Order created and waiting for execution.
Executed Qty   : 0.0000

Order placed successfully!
```

---

# Logging

Logs are stored inside:

```text
logs/
```

The application logs:
- API requests
- successful responses
- validation errors
- Binance API errors
- unexpected exceptions

---

# Assumptions

- Only Binance Futures Testnet (USDT-M) is supported
- Only MARKET and LIMIT orders are implemented
- Only USDT trading pairs are validated

---

# Tech Stack

- Python 3.x
- python-binance
- argparse
- python-dotenv
- logging

---

# Author

Animesh Kumar Rai