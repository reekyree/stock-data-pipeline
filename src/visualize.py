import pandas as pd 
import sqlite3
import matplotlib.pyplot as plt

def visualize_data():
    # Connect to db 
    conn = sqlite3.connect('stock_data.db')

    # Use pandas to query table
    data = pd.read_sql_query("SELECT * FROM stocks", conn)

    # Get the closing price column
    data["Close"].plot()

    # Set chart labels 
    plt.title("AAPL Closing Price")
    plt.xlabel("Index")
    plt.ylabel("Price")

    # Display chart

    plt.show()
