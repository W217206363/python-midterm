# Get price and state from the user
price = float(input("Enter the price of the sale item (e.g., 3.99): "))
# .strip().upper() ensures the input matches the logic even if the user types "tx " or "tx"
state = input("Enter the state to which the item will be shipped (ex: TX, LA, CA): ").strip().upper()

# Determine the shipping tax
if state == "TX" or state == "LA":
    shipping_tax = 1.25
elif state == "CA":
    shipping_tax = 3.25
else:
    shipping_tax = 0.50

# Display the shipping tax
print(f"Shipping tax: {shipping_tax}")