import sqlite3

def analyze_data():
    # Connect to database
    conn = sqlite3.connect('stock_data.db')
    cursor = conn.cursor()

    # Retreive and display highest closing price
    query = """SELECT MAX(Close) FROM stocks"""

    print("Highest Close: ")
    print(conn.execute(query).fetchall())

    # Retreive and display avg trading volume
    query = """SELECT AVG(Volume) FROM stocks"""

    print("Average Trading Volume: ")
    print(conn.execute(query).fetchall())





