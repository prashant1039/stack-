import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def generate_pie_chart():
    try:
        # Get total number of days
        with open("stock_data.txt", "r") as f:
            total_days = len(f.readlines())
        
        # Read trades (buy/sell pairs)
        buys = []
        sells = []
        with open("trades.txt", "r") as f:
            for line in f:
                b, s = map(int, line.strip().split())
                buys.append(b)
                sells.append(s)

        used_days = len(set(buys + sells))
        rest_days = total_days - used_days

        labels = ['Buy Days', 'Sell Days', 'Hold Days']
        values = [len(buys), len(sells), rest_days]
        colors = ['#28a745', '#dc3545', '#6c757d']

        plt.figure(figsize=(6, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
        plt.title("Trade Distribution")
        plt.tight_layout()
        plt.savefig("static/pie.png")
        plt.close()
        print(" Pie chart saved to static/pie.png")
    except Exception as e:
        print(" Error generating pie chart:", e)
