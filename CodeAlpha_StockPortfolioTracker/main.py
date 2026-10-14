from datetime import datetime
import csv

# Example prices are hardcoded for this assignment, not live market prices.
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 165.00,
    "AMZN": 190.00,
}

def main():
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(STOCK_PRICES))
    portfolio = []

    while True:
        symbol = input("Stock symbol (or DONE to finish): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Unknown symbol. Choose one from the available list.")
            continue

        try:
            quantity = int(input(f"Quantity of {symbol}: ").strip())
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Quantity must be a positive whole number.")
            continue

        price = STOCK_PRICES[symbol]
        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "value": price * quantity,
        })

    if not portfolio:
        print("No stocks entered.")
        return

    total = sum(item["value"] for item in portfolio)
    print("\n--- Portfolio Summary ---")
    for item in portfolio:
        print(f'{item["symbol"]}: {item["quantity"]} × ${item["price"]:.2f} = ${item["value"]:.2f}')
    print(f"Total investment value: ${total:.2f}")

    save = input("Save summary to portfolio.csv? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["symbol", "quantity", "price", "value"])
            writer.writeheader()
            writer.writerows(portfolio)
            writer.writerow({
                "symbol": "TOTAL",
                "quantity": "",
                "price": "",
                "value": total,
            })
        print("Saved portfolio.csv")

if __name__ == "__main__":
    main()
