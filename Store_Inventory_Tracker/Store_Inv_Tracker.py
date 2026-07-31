""" Model a small store's inventory using a dictionary, then generate a stock report from it. Each product maps to a quantity,
 and your program loops over the dictionary to print every item, total the stock on hand, and flag anything running low.
  Dictionaries are how real programs store labeled data, and looping over them is the bread and butter of working with that data.

You'll use everything through Section 5: variables, math, conditionals, loops, and dictionaries (creating, accessing, and looping over them). 

Use only Section 1–5 skills: variables, math, conditionals, loops, and dictionaries
Store inventory as a dictionary mapping product name -> quantity
Loop over the dictionary to produce the report
Use a conditional to flag low-stock items
No functions required

Build an inventory dictionary, e.g. inventory = {"apples": 12, "bread": 3, "milk": 0}
Loop over the dictionary and print each product with its quantity
Compute the total units in stock across all products
Flag products at or below a low-stock threshold (e.g. 5)
Print a clean report
--- INVENTORY REPORT ---
apples: 12
bread:  3  (LOW)
milk:   0  (OUT OF STOCK)
Total units in stock: 15
Low-stock items: 2

Add a price to each item using a second dictionary and compute total inventory value
Count how many distinct products you carry
"""
inventory = {
    "apples": 12,
    "bread": 3,
    "milk": 0,
    "eggs": 6,
    "cheese": 2,
    "oranges": 8,
    "bananas": 4,
}
prices = {
    "apples": 0.5,
    "bread": 2.0,
    "milk": 1.5,
    "eggs": 0.2,
    "cheese": 3.0,
    "oranges": 0.6,
    "bananas": 0.3,
}

low_stock_threshold = 5
total_stock = 0

print("Store Inventory Report:")
print("-" * 30)

for product, quantity in inventory.items():
    total_stock += quantity
    if quantity <= low_stock_threshold:
        print(f"{product}: {quantity} (LOW STOCK!)")
    else:
        print(f"{product}: {quantity}")

print("-" * 30)
print(f"Total units in stock: {total_stock}")
print(f"Total inventory value: ${sum(inventory[product] * prices[product] for product in inventory):.2f}")
print(f"Distinct products: {len(inventory)}")
