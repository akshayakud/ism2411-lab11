
# ISM2411 Module 11 Lab
# Customer Dictionary & Lookup

# REFLECTION 1:
# I would use .get() when a key might be missing because it allows me to provide a default value instead of causing an error. I would use bracket
# notation when I know the key exists and need to access its exact value. My rule of thumb is to use .get() for optional information and brackets
# for information that should always be present.

# REFLECTION 2:
# Exercise 8 reminds me of using SUMIF in Excel because both methods calculate totals based on categories such as regions. Python is more
# useful for large datasets because it can process many records automatically using loops without manually creating formulas.

# EXERCISE 1:

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250
}

print("EXERCISE 1")

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# EXERCISE 2: 

print("\nEXERCISE 2")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# EXERCISE 3:

print("\nEXERCISE 3")

email = customer.get("email", "no email on file")
print(email)

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# EXERCISE 4:

print("\nEXERCISE 4")

# Use items() to access both keys and values
for key, value in customer.items():
    print(f"{key}: {value}")

# Without items(), the loop only accesses the keys
for key in customer:
    print(key)

# Difference: .items() gives both the key and value,
# while looping through the dictionary directly gives only keys.

# EXERCISE 5:

print("\nEXERCISE 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

discount_rate = tier_discounts.get(customer["tier"], 0)

purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print("Tier:", customer["tier"])
print("Discount rate:", discount_rate * 100, "%")
print("Final price: $", round(final_price, 2))

# EXERCISE 6:

print("\nEXERCISE 6")

customer1 = {
    "name": "Alice",
    "tier": "platinum"
}

customer2 = {
    "name": "Bob",
    "tier": "gold"
}

customer3 = {
    "name": "Charlie",
    "tier": "silver"
}

customers = [customer1, customer2, customer3]

for customer_record in customers:
    tier = customer_record["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f'{customer_record["name"]}: '
        f'{tier}, Discount: ${discount_amount:.2f}'
    )

# EXERCISE 7: 

print("\nEXERCISE 7")

catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}")


# EXERCISE 8:

print("\nEXERCISE 8")

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
    print(f"{region}: ${sales_by_region[region]}")