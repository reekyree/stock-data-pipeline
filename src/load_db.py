import sqlite3
import pandas as pd

def load_database():
    # Load validated csv
    data = pd.read_csv("data/processed/aapl_clean.csv")

    # Connect to database
    conn = sqlite3.connect("stock_data.db")

    # Create table 
    data.to_sql("stocks", conn, if_exists="replace", index=False)

    print("Stock data saved to database.")



