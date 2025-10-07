# Exercise 3: Grocery Tracker with Item Removal & Refunds
# Based on Exercise 2, write code allowing users to remove mistakenly added items and get
# refunds, updating the budget in real-time.
# New Concepts Added:
# ✔ List Removal Methods (remove(), pop())
# ✔ Refund Calculations
# ✔ Error Handling for invalid removals


# danh sách items, prices, category, discounts
items_list = ['Apple', 'Milk', 'Chips','Carrot']
prices_dict = {'Apple': 2.0, 'Milk' : 3 , 'Chips' : 1,'Carrot' : 2.5}
category_list = ['Fruits', 'Vegatables', 'Dairy', 'Snacks']
dicount_dict = {'Fruits' : 0.1 , 'Vegatables' : 0.05, 'Dairy': 0.07, 'Snacks': 0.1}

# input budget , flag và total
budget_input = float(input("Enter your budget: $"))
purchases = []
s_budget = budget_input
within_budget = True
total = 0

# Add item function
def add_item():
    print(f"Available items: {items_list}")
    item = input("Enter your item (or quit to finish): ").capitalize().strip()
    if item == "Quit":
        return False
    if item not in items_list:
        print("Item is not in list.")
        return True
    category = category_list[items_list.index(item)]
    print("Category of the item above is: ", category)
    
    # lấy giá và discount
    price = prices_dict[item]
    discount = dicount_dict[category]
    final_price = price * (1 - discount)
    global total
    total += final_price
    
    # kiểm tra ngân sách 
    global budget_input
    if budget_input - final_price < 0:
        print("Not enough budget to this item.")
        return False
    
    # Lưu record
    purchases.append((item,category,price,discount,final_price))
    
    # cập nhật ngân sách 
    budget_input -= final_price
    print(f"Applied {discount:.0%} discount.")
    print(f"Added {item}. Remaining budget: ${budget_input:.2f}")
    print("\n")
    return True

# Remove item function
def remove_item():
    if not purchases:
        print("No items to remove.")
        return
    print("Current purchases:")
    for idx, (item, category, price, discount, final_price) in enumerate(purchases):
        print(f"{idx + 1}. {item} - ${final_price:.2f}")
    try:
        choice = int(input("Enter the number of the item to remove (or 0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(purchases):
            item, category, price, discount, final_price = purchases.pop(choice - 1)
            global total, budget_input
            total -= final_price
            budget_input += final_price
            print(f"Removed {item}. Refunded ${final_price:.2f}. New budget: ${budget_input:.2f}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")
        
# View cart function
def view_cart():
    if not purchases:
        print("Your cart is empty.")
        return
    print("\n=================================RECEIPT===================")
    print("{:<10} {:<12} {:<10} {:<10} {:<10}".format("Item","Category","Price","Discount","Final Price"))
    for item, category, price, discount, final_price in purchases:
        print("{:<10} {:<12} ${:<9.2f} {:<10.0%} ${:<10.2f}".format(item, category, price, discount, final_price))
    print("\n============================================================")
    print("TOTAL: ${:.2f}".format(total))
    print("BUDGET: ${:.2f}".format(s_budget))
    if total > s_budget:
        print("STATUS: OVER BUDGET")
    else:
        print("STATUS: UNDER BUDGET")

# vòng lặp
while True:
    print("=== MENU ===")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Finish shopping")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for shopping!")
        
    
