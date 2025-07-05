def run_strategy(fee=2):
    try:
        with open("stock_data.txt", "r") as f:
            prices = [int(line.strip().split()[1]) for line in f.readlines()]
    except FileNotFoundError:
        print(" stock_data.txt not found.")
        return 0

    trades = []
    if not prices:
        return 0

    hold = -prices[0]
    sold = 0
    rest = 0
    buy_day = 0
    total_profit = 0

    for i in range(1, len(prices)):
        prev_hold = hold
        if rest - prices[i] > hold:
            hold = rest - prices[i]
            buy_day = i

        rest = max(rest, sold)

        if prev_hold + prices[i] - fee > sold:
            sold = prev_hold + prices[i] - fee
            trades.append((buy_day, i))
            buy_day = -1

    total_profit = max(sold, rest)

    with open("trades.txt", "w") as f:
        for b, s in trades:
            f.write(f"{b} {s}\n")

    return total_profit

if __name__ == "__main__":
    profit = run_strategy()
    print(f" Total Profit: ₹{profit}")
