# Stock Data Pipeline

## Overview

A small proof-of-concept financial data project built in Python. The program pulls data from the Yahoo Finance API, stores and validates it, and outputs average trading volume and highest close numbers. It also displays a graph of the closing prices.

The main goal was to demonstrate and practice the following concepts:
- data ingestion
- validation checks
- relational database manipulation
- Basic SQL querying

---

## Technologies

- Python
- pandas
- yfinance
- SQLite
- matplotlib
- Git/GitHub

---

## Project Structure

stock-data-pipeline/
|
|--data/
|  |--raw/
|  |--processed/
|
|-src/
|  |--fetch.py
|  |--validate.py
|  |--load_db.py
|  |--analyze.py
|  |--visualize.py
|
|--main.py
|--requirements.txt
|--stock_data.db
|--.gitignore
|--README.md

---

## How to Run

- Install Dependencies:
```bash
pip install -r requirements.txt
```

---

Run the full program with:
```bash
python main.py
```

