# TODO
# Add conditionals before writing data into a new CSV.
# Add additional validation checks

import pandas as pd 

# Retrieve csv
data = pd.read_csv("data/raw/aapl_raw.csv")

# Check for null values
null_amounts = print(data.isnull().sum())

# Dispaly the number of null values 
print(null_amounts)

# Run a check for the returned data type
if null_amounts is None:
    null_amounts = 0

# Display warning for user
if null_amounts > 0:
    print("Warning: Missing Values in Data")

# Check for an empty data set
if data.empty:
    print("Data set is empty.")

# Check for duplicate dates
print("Duplicates Found: ")
print(data.index.duplicated().sum())

# Convert Date index into a column
data.reset_index(inplace=True)

# Check columns TEST
print(data.columns)

# Write validated data to csv in separate data folder
data.to_csv("data/processed/aapl_clean.csv")
