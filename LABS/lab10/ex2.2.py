import pandas as pd
import matplotlib.pyplot as plt

# Load data
orders = pd.read_csv('orders.csv')
order_items = pd.read_csv('order_items.csv')
products = pd.read_csv('products.csv')
customers = pd.read_csv('customers.csv')

# --- Data Preparation ---
# Convert order_date to datetime objects
orders['order_date'] = pd.to_datetime(orders['order_date'])

# Calculate the total price for each order item
order_items['total_price'] = order_items['quantity'] * order_items['price_per_item']

# Merge DataFrames to create a single master view
# Merge orders with order_items
df = pd.merge(orders, order_items, on='order_id')
# Add product information
df = pd.merge(df, products, on='product_id')
# Add customer information
df = pd.merge(df, customers, on='customer_id')

print("Data loaded and merged successfully. Here is a sample:")
print(df.head())

#Question 1: What are the total monthly sales? Understanding sales trends over time is crucial for planning and marketing.
# Set order_date as the index
df.set_index('order_date', inplace=True)

# Resample data by month and sum the total_price
monthly_sales = df['total_price'].resample('M').sum()

# Plot the results
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o')
plt.title('Total Monthly Sales for Jan 2025')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.grid(True)
plt.show()

print("Monthly Sales:\n", monthly_sales)
#Question 2: What are the top 5 best-selling products by quantity? - This helps identify popular products for inventory management and marketing focus.
# Group by product name and sum the quantities
top_products = df.groupby('product_name')['quantity'].sum().nlargest(5)

# Plot the results
plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind='barh', color='skyblue')
plt.title('Top 5 Best-Selling Products by Quantity')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Product Name')
plt.show()

print("Top 5 Products:\n", top_products)
#Question 3: Who are the top 5 highest-spending customers? Identifying top customers is key for loyalty programs and targeted marketing.
# Group by customer and sum their total spending
top_customers = df.groupby('customer_name')['total_price'].sum().nlargest(5)

print("Top 5 Highest-Spending Customers:\n", top_customers)

#Question 4: Which product category generates the most revenue? This insight can guide business strategy and resource allocation.
# Group by category and sum the total price
category_revenue = df.groupby('category')['total_price'].sum().sort_values(ascending=False)

print("\nRevenue by Product Category:\n", category_revenue)
