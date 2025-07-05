import matplotlib
matplotlib.use('Agg')  #  Force matplotlib to work without GUI

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def load_data():
    days, prices = [], []
    try:
        with open("stock_data.txt", "r") as f:
            for line in f:
                d, p = line.strip().split()
                days.append(int(d))
                prices.append(int(p))
    except FileNotFoundError:
        print(" stock_data.txt missing.")
    return days, prices

def load_trades():
    buys, sells = [], []
    try:
        with open("trades.txt", "r") as f:
            for line in f:
                b, s = line.strip().split()
                buys.append(int(b))
                sells.append(int(s))
    except FileNotFoundError:
        print(" trades.txt not found.")
    return buys, sells

def load_prediction():
    try:
        with open("predicted.txt", "r") as f:
            return int(f.read().strip())
    except:
        return None

def load_symbol():
    try:
        with open("symbol.txt", "r") as f:
            return f.read().strip().upper()
    except:
        return "Unknown"

def plot_graph():
    days, prices = load_data()
    buys, sells = load_trades()
    predicted = load_prediction()
    symbol = load_symbol()

    plt.figure(figsize=(12, 6))
    plt.plot(days, prices, color='blue', linewidth=2, label='Stock Price')
    plt.grid(True, linestyle='--', alpha=0.6)

    # Plot Buy points
    for b in buys:
        plt.scatter(b, prices[b], color='green', s=120, marker='^', label=f'Buy ₹{prices[b]}' if b == buys[0] else "")
        plt.text(b, prices[b]+2, f'₹{prices[b]}', color='green', fontsize=9, ha='center')

    # Plot Sell points
    for s in sells:
        plt.scatter(s, prices[s], color='red', s=120, marker='v', label=f'Sell ₹{prices[s]}' if s == sells[0] else "")
        plt.text(s, prices[s]-5, f'₹{prices[s]}', color='red', fontsize=9, ha='center')

    # Predicted next price
    if predicted:
        plt.scatter([days[-1] + 1], [predicted], color='orange', marker='o', s=150, label=f'Predicted ₹{predicted}')
        plt.text(days[-1]+1, predicted+3, f'₹{predicted}', color='orange', fontsize=10, ha='center')

    plt.title(f" Stock Analysis for: {symbol}", fontsize=16)
    plt.xlabel("Day", fontsize=12)
    plt.ylabel("Price", fontsize=12)
    plt.legend()
    plt.tight_layout()
    plt.savefig("static/plot.png")
    plt.close()

if __name__ == "__main__":
    plot_graph()
