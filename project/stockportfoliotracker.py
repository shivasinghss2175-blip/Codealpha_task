

# Predefined stock prices (sample prices, not live market data)
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total = 0

print("--- STOCK PORTFOLIO TRACKER ---")
print("Available stocks:", stocks)

while True:
    name = input("\nEnter stock name (or done): ").upper()

    if name == "DONE":
        break

    if name in stocks:
        quantity = int(input("Enter quantity: "))

        investment = stocks[name] * quantity
        total += investment

        print("Investment:", investment)

    else:
        print("Stock not available!")

print("\nTotal Investment:", total)

# Save the final investment in a text file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment: " + str(total))

print("Report saved successfully!")