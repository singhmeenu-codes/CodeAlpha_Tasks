"""
Stock Portfolio Tracker
------------------------
A simple tracker that calculates total investment based on
manually defined (hardcoded) stock prices.

Key Concepts Used: dictionary, input/output, basic arithmetic, file handling.
"""

import csv
from datetime import datetime

# Hardcoded dictionary of stock prices (price per share, in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330,
}


def show_available_stocks(prices):
    """Print the stocks the user is allowed to enter."""
    print("Available stocks and prices per share:")
    for symbol, price in prices.items():
        print(f"  {symbol}: ${price}")
    print()


def get_portfolio_input(prices):
    """
    Repeatedly ask the user for a stock symbol and quantity.
    Returns a list of (symbol, quantity, price, value) tuples.
    """
    portfolio = []

    print("Enter stock symbols and quantities. Type 'done' as the symbol to finish.\n")

    while True:
        symbol = input("Stock symbol: ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in prices:
            print(f"'{symbol}' is not in the price list. Please choose from the available stocks.\n")
            continue

        quantity_input = input(f"Quantity of {symbol}: ").strip()

        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            print("Please enter a positive whole number for quantity.\n")
            continue

        quantity = int(quantity_input)
        price = prices[symbol]
        value = quantity * price

        portfolio.append((symbol, quantity, price, value))
        print(f"Added: {quantity} share(s) of {symbol} = ${value}\n")

    return portfolio


def display_summary(portfolio):
    """Print a summary table and the total investment value."""
    if not portfolio:
        print("No stocks were added to the portfolio.")
        return 0

    print("\n--- Portfolio Summary ---")
    print(f"{'Symbol':<10}{'Quantity':<12}{'Price':<10}{'Value':<10}")
    total = 0
    for symbol, quantity, price, value in portfolio:
        print(f"{symbol:<10}{quantity:<12}${price:<9}${value:<9}")
        total += value

    print("-" * 42)
    print(f"Total Investment Value: ${total}")
    return total


def save_to_file(portfolio, total):
    """Ask the user whether to save results, then write to a .csv or .txt file."""
    choice = input("\nSave results to a file? (y/n): ").lower().strip()

    if choice != "y":
        print("Results not saved.")
        return

    file_format = input("Save as .csv or .txt? ").lower().strip()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if file_format == "csv":
        filename = f"portfolio_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])
            for symbol, quantity, price, value in portfolio:
                writer.writerow([symbol, quantity, price, value])
            writer.writerow(["", "", "Total", total])
        print(f"Saved to {filename}")

    elif file_format == "txt":
        filename = f"portfolio_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write(f"{'Symbol':<10}{'Quantity':<12}{'Price':<10}{'Value':<10}\n")
            for symbol, quantity, price, value in portfolio:
                f.write(f"{symbol:<10}{quantity:<12}${price:<9}${value:<9}\n")
            f.write("-" * 42 + "\n")
            f.write(f"Total Investment Value: ${total}\n")
        print(f"Saved to {filename}")

    else:
        print("Unrecognized format. Results not saved.")


def main():
    print("=== Stock Portfolio Tracker ===\n")
    show_available_stocks(STOCK_PRICES)
    portfolio = get_portfolio_input(STOCK_PRICES)
    total = display_summary(portfolio)

    if portfolio:
        save_to_file(portfolio, total)


if __name__ == "__main__":
    main()