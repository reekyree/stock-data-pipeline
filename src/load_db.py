import sqlite3
import pandas as pd

# Load validated csv
data = pd.read_csv("data/processed/aapl_clean.csv")

# Create/connect to database
conn = sqlite3.connect("stock_data.db")

# Create table 
data.to_sql("stocks", conn, if_exists="replace", index=False)


query = """
SELECT
    Date,
    ABS(Close - Open) AS movement
FROM stocks
ORDER BY movement DESC
LIMIT 5
"""

print(conn.execute(query).fetchall())
