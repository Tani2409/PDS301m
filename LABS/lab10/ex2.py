import pandas as pd
import numpy as np

# Create customers data
customers = pd.DataFrame({
    'customer_id': range(1, 11),
    'customer_name': [f'Customer_{i}' for i in range(1, 11)]
})

# Create products data
products = pd.DataFrame({
    'product_id': range(101, 106),
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories']
})

# Create orders data
orders = pd.DataFrame({
    'order_id': range(1001, 1021),
    'customer_id': np.random.randint(1, 11, 20),
    'order_date': pd.to_datetime(pd.date_range(start='2025-01-15', periods=20, freq='D'))
})

# Create order items data
order_items = []
for order_id in orders['order_id']:
    num_items = np.random.randint(1, 4)
    for _ in range(num_items):
        product_id = np.random.randint(101, 106)
        quantity = np.random.randint(1, 5)
        price_per_item = products.loc[products['product_id'] == product_id, 'product_id'].iloc[0] * 2.5 + np.random.uniform(0, 50)
        order_items.append([order_id, product_id, quantity, round(price_per_item, 2)])

order_items_df = pd.DataFrame(order_items, columns=['order_id', 'product_id', 'quantity', 'price_per_item'])

# Save to CSV
customers.to_csv('customers.csv', index=False)
products.to_csv('products.csv', index=False)
orders.to_csv('orders.csv', index=False)
order_items_df.to_csv('order_items.csv', index=False)

print("Sample data files created successfully.")
