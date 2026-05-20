# TODO
# Add conditionals before writing data into a new CSV.
# Add additional validation checks

import pandas as pd 

def validate_data():

    # Retrieve csv
    data = pd.read_csv("data/raw/aapl_raw.csv")

    # Check for null values
    null_rows = data[data.isnull().any(axis=1)]

    # Display number of rows to be removed
    print(f"Rows removed: {len(null_rows)}")

    # Remove rows
    data = data.dropna()

    # Check for an empty data set
    if data.empty:
        print("Data set is empty.")

    # Check for duplicates  
    print("Duplicates Found: ")
    print(data.index.duplicated().sum())

    # Write validated data to csv in separate data folder
    data.to_csv("data/processed/aapl_clean.csv", index=False)
