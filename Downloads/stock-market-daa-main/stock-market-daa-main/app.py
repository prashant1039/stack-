from flask import Flask, render_template, request
import os
import strategy_logic
import predict_price
import stock_visualization
import fetch_stock_data
import export_report
import generate_pie

app = Flask(__name__)

def get_trade_count():
    try:
        with open("trades.txt", "r") as f:
            return len(f.readlines())
    except:
        return 0

def get_price_data():
    try:
        with open("stock_data.txt", "r") as f:
            return [(int(line.split()[0]), int(line.split()[1])) for line in f.readlines()]
    except:
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    profit = None
    predicted = None
    trades = 0
    symbol = ""
    price_data = []

    if request.method == 'POST':
        symbol = request.form['symbol'].strip().upper()
        days = int(request.form.get('days', 30))  # Get custom number of days

        with open("symbol.txt", "w") as f:
            f.write(symbol)

        fetch_stock_data.fetch_stock(symbol, days)  #  Pass selected days
        profit = strategy_logic.run_strategy()
        predicted = predict_price.predict_next_price()
        stock_visualization.plot_graph()
        generate_pie.generate_pie_chart()
        trades = get_trade_count()
        price_data = get_price_data()
        export_report.export_to_pdf(symbol, profit, predicted, trades)

    return render_template('index.html',
                           profit=profit,
                           predicted=predicted,
                           trades=trades,
                           symbol=symbol,
                           price_data=price_data)

if __name__ == '__main__':
    app.run(debug=True)
