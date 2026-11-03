# Reflection 1:
# I would use .get() if I'm unsure whether a key is in the dictionary
# because it helps avoid errors. I would use brackets when I'm certain
# the key exists. Overall, I think .get() is better when some data
# might not be available.

# Reflection 2:
# Exercise 8 is similar to using a PivotTable in Excel because both
# help organize data into groups. Python can be helpful when working
# with a lot of data since it can sort and calculate information
# automatically instead of doing everything by hand.


# Exercise 1: One Customer

customer = {
    "name": "Ela",
    "email": "elakekec@icloud.com",
    "tier": "gold",
    "ytd_spend": 500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2: Update and Add

customer["phone"] = "123-456-7890"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# Exercise 3: Safe Lookup

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("Email not found")


# Exercise 4: Iterate

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only prints the keys.
for key in customer:
    print(key)


# Exercise 5: Lookup Table

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
price = 200
final_price = price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")


# Exercise 6: List of Dicts

customers = [
    {"name": "Ela", "tier": "gold"},
    {"name": "Gabe", "tier": "silver"},
    {"name": "Reyniel", "tier": "platinum"}
]

for person in customers:
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount

    print(f"{person['name']}: {tier}, Discount: ${discount_amount:.2f}")


# Exercise 7: Nested Catalog

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} remaining")


# Exercise 8: Sales by Region

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")
