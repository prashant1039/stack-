import numpy as np
from sklearn.linear_model import LinearRegression

def predict_next_price():
    try:
        with open("stock_data.txt", "r") as f:
            lines = f.readlines()
            X = np.array([int(line.split()[0]) for line in lines]).reshape(-1, 1)
            y = np.array([int(line.split()[1]) for line in lines])
    except FileNotFoundError:
        print(" stock_data.txt not found.")
        return None

    if len(X) < 5:
        print(" Not enough data for prediction.")
        return None

    model = LinearRegression()
    model.fit(X, y)
    next_day = np.array([[X[-1][0] + 1]])
    predicted_price = int(model.predict(next_day)[0])

    # Save prediction to a file
    with open("predicted.txt", "w") as f:
        f.write(str(predicted_price))

    return predicted_price

if __name__ == "__main__":
    price = predict_next_price()
    if price:
        print(f" Predicted price for next day: ₹{price}")
