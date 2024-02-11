import json
import time
import sys

def load_json(file):
    """
    Load JSON data from a file.

    Args:
        file (str): The name of the file to load.

    Returns:
        The loaded JSON data.

    Raises:
        SystemExit: If the file cannot be loaded.
    """
    try:
        with open(file, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        sys.exit(1)

def compute_total_sales(price_catalogue, sales_record):
    """
    Compute the total sales from a sales record and a price catalogue.

    Args:
        price_catalogue (list): The price catalogue.
        sales_record (list): The sales record.

    Returns:
        The total sales.
    """
    total_sales = 0
    for sale in sales_record:
        for item in price_catalogue:
            if item['title'] == sale['Product']:
                total_sales += item['price'] * sale['Quantity']
    return total_sales

def write_results(total_sales, elapsed_time):
    """
    Write the results to the console and a text file.

    Args:
        total_sales (float): The total sales.
        elapsed_time (float): The elapsed time.
    """
    result = f"Total sales: {total_sales}\nElapsed time: {elapsed_time} seconds"
    print(result)
    with open('SalesResults.txt', 'w') as f:
        f.write(result)

def main():
    """
    Main function to execute the program.
    """
    # Check the number of command line arguments
    if len(sys.argv) != 3:
        print("Usage: python compute_sales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    # Start the timer
    start_time = time.time()

    # Load the JSON data
    price_catalogue = load_json(sys.argv[1])
    sales_record = load_json(sys.argv[2])

    # Compute the total sales
    total_sales = compute_total_sales(price_catalogue, sales_record)

    # Stop the timer
    elapsed_time = time.time() - start_time

    # Write the results
    write_results(total_sales, elapsed_time)

if __name__ == "__main__":
    main()