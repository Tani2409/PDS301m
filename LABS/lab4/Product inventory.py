
# 1. Create the initial inventory
inventory = {
    "Laptop": 12,
    "Mouse": 55,
    "Keyboard": 30
}
print("Initial Inventory:", inventory)

# 2. Add a new product
inventory["Webcam"] = 20
print("After adding Webcam:", inventory)

# 3. Update stock (shipment of 15 laptops arrived)
inventory["Laptop"] += 15
print("After updating Laptop stock:", inventory)

# 4. Process a sale (customer bought 5 mice)
inventory["Mouse"] -= 5
print("After selling Mouse:", inventory)

# 5. Print the final stock report
print("\n--- Final Inventory Report ---")
for product, stock in inventory.items():
    print(f"Product: {product}, Stock Remaining: {stock}")
