import pandas as pd
import random
from datetime import datetime, timedelta

# ==================================
# CUSTOMERS
# ==================================

customers = []

cities = [
    "Mumbai",
    "Delhi",
    "Pune",
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Kolkata"
]

for i in range(1, 1001):
    customers.append({
        "customer_id": i,
        "customer_name": f"Customer_{i}",
        "email": f"customer{i}@gmail.com",
        "city": random.choice(cities),
        "signup_date": (
            datetime(2024, 1, 1)
            + timedelta(days=random.randint(0, 500))
        ).date()
    })

customers_df = pd.DataFrame(customers)

# ==================================
# PRODUCTS
# ==================================

products = []

categories = [
    "Electronics",
    "Accessories",
    "Home",
    "Fashion"
]

for i in range(1, 201):
    products.append({
        "product_id": i,
        "product_name": f"Product_{i}",
        "category": random.choice(categories),
        "price": random.randint(100, 50000)
    })

products_df = pd.DataFrame(products)

# ==================================
# ORDERS
# ==================================

orders = []

for i in range(1, 5001):
    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, 1000),
        "order_date": (
            datetime(2025, 1, 1)
            + timedelta(days=random.randint(0, 365))
        ).date()
    })

orders_df = pd.DataFrame(orders)

# ==================================
# ORDER ITEMS
# ==================================

order_items = []

for i in range(1, 12001):

    product_id = random.randint(1, 200)

    product_price = products_df.loc[
        products_df["product_id"] == product_id,
        "price"
    ].iloc[0]

    order_items.append({
        "order_item_id": i,
        "order_id": random.randint(1, 5000),
        "product_id": product_id,
        "quantity": random.randint(1, 5),
        "unit_price": product_price
    })

order_items_df = pd.DataFrame(order_items)

# ==================================
# SAVE CSV FILES
# ==================================

customers_df.to_csv(
    "data/processed/customers_large.csv",
    index=False
)

products_df.to_csv(
    "data/processed/products_large.csv",
    index=False
)

orders_df.to_csv(
    "data/processed/orders_large.csv",
    index=False
)

order_items_df.to_csv(
    "data/processed/order_items_large.csv",
    index=False
)

# ==================================
# SUMMARY
# ==================================

print("Customers:", len(customers_df))
print("Products:", len(products_df))
print("Orders:", len(orders_df))
print("Order Items:", len(order_items_df))
print("CSV files saved successfully")