import pandas as pd, yfinance as yf 

def fetch_data():
    # Get apple ticker data for one month
    apple = yf.download("AAPL", period = "1mo")

    # Drop the price column from yfinance data
    apple.columns = apple.columns.droplevel(1)


    # Save ticker data to csv
    apple.to_csv("data/raw/aapl_raw.csv", index_label="Date")


