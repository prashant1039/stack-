import yfinance as yf

def fetch_stock(symbol, days=30):
    print(f"Fetching data for: {symbol}")

    data = yf.download(symbol, period="90d", interval="1d", progress=False)

    # Fix: squeeze to ensure it's a Series before tolist()
    prices = data['Close'].dropna().squeeze().astype(int).tolist()[-days:]

    with open("stock_data.txt", "w") as f:
        for i, price in enumerate(prices):
            f.write(f"{i} {price}\n")

    print(f" Fetched {len(prices)} trading days for {symbol}")
