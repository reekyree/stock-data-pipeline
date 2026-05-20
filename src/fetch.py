import pandas as pd, yfinance as yf 

# Get apple ticker data for one month
apple = yf.download("AAPL", period = "1mo")


# Save ticker data to csv
apple.to_csv("data/raw/aapl_raw.csv", index_label="Date")

print(apple)

