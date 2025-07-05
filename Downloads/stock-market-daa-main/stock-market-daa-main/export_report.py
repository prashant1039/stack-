from fpdf import FPDF
from datetime import datetime
import os

def export_to_pdf(symbol, profit, predicted, trades):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Stock Strategy Analysis Report", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
    pdf.ln(10)

    # Summary details
    pdf.cell(200, 10, txt=f"Stock Symbol: {symbol}", ln=True)
    pdf.cell(200, 10, txt=f"Total Profit: Rs. {profit}", ln=True)
    pdf.cell(200, 10, txt=f"Predicted Next Price: Rs. {predicted}", ln=True)
    pdf.cell(200, 10, txt=f"Number of Trades: {trades}", ln=True)
    pdf.ln(10)

    # Trade list
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Trade Summary (Buy -> Sell):", ln=True)
    pdf.set_font("Arial", size=12)

    try:
        with open("trades.txt", "r") as f:
            trade_lines = f.readlines()
            if trade_lines:
                for line in trade_lines:
                    b, s = line.strip().split()
                    pdf.cell(200, 10, txt=f"Buy Day: {b} -> Sell Day: {s}", ln=True)
            else:
                pdf.cell(200, 10, txt="No trades recorded.", ln=True)
    except:
        pdf.cell(200, 10, txt="Trade file missing.", ln=True)

    pdf.ln(10)

    # Add graph image
    if os.path.exists("static/plot.png"):
        pdf.image("static/plot.png", x=10, y=pdf.get_y(), w=190)
    else:
        pdf.cell(200, 10, txt="Graph image not found.", ln=True)

    # Save PDF
    pdf.output("static/report.pdf")
    print(" Report saved to static/report.pdf")
