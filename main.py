from src.fetch import fetch_data
from src.validate import validate_data
from src.load_db import load_database
from src.analyze import analyze_data
from src.visualize import visualize_data

def main():
   
    # Pull stock data
    fetch_data()

    # Validate raw data
    validate_data()

    # Input stock data into db 
    load_database()

    # Analyze data for specific queries
    analyze_data()

    # Visualize one the highest close
    visualize_data()



if __name__ == '__main__':
    main()


