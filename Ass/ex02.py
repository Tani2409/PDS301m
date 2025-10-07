budget = input('what is your total budget: $')
avaiable_items = {'Apple' : 10, 'Milk': 20, 'Chips': 30, 'Carrot': 40}
cart =  []
total_budget = 0
discounts = {'Fruit': 10, 'Vegatable': 15, 'Dairy': 20, 'Snacks': 25}
category = ['Fruit', 'Vegatable', 'Dairy', 'Snacks']

print (f'Available items:  {avaiable_items}')
item = input('enter item to add to cart: ').capitalize()
if item in avaiable_items:
    cart.append(item)
    discount_code = input(f'enter category {category}:').capitalize()
    if discount_code in discounts:
        discount = discounts.get(discount_code, 0)
        print (f'Applied {discount}% discount!')
        print (f'Added {item}. Remaining budget: ${int(budget) - avaiable_items[item] + (avaiable_items[item] * discount / 100)}')

# Exercise 2: Advanced Grocery Shopping Tracker
# Based on an exercise 1, write a program to enhance the budget tracker to include item names,
# categorize purchases, apply discounts, and generate a detailed receipt.
# Key Python Concepts Covered: Lists: Track multiple purchases dynamically; Tuples: Immutable
# (item, price, category) records; Dictionaries: Look up prices/discounts efficiently; String
# Formatting: Align receipt columns (:<10 for left-align); Logical Operators(discount); Boolean
# Flag: within_bnudget controls loop exit

# danh sách items, prices, category, discounts
items_list = ['Apple', 'Milk', 'Chips','Carrot']
prices_dict = {'Apple': 2.0, 'Milk' : 3 , 'Chips' : 1,'Carrot' : 2.5}
category_list = ['Fruits', 'Vegatables', 'Dairy', 'Snacks']
dicount_dict = {'Fruits' : 0.1 , 'Vegatables' : 0.05, 'Dairy': 0.01, 'Snacks': 0.1}

# input budget , flag và total
budget_input = float(input("Enter your budget: $"))
purchases = []
s_budget = budget_input
within_budget = True
total = 0
# vòng lặp 
while within_budget:
    print(f"Available items: {items_list}")
    item = input("Enter your item (or quit to finish): ").capitalize().strip()
    if item == "Quit":
        within_budget = False
        break
    if item not in items_list:
        print("Item is not in list.")
        continue
    category = category_list[items_list.index(item)]
    print("Category of the item above is: ", category)
    
    # lấy giá và discount
    price = prices_dict[item]
    discount = dicount_dict[category]
    final_price = price * (1 - discount)
    total += final_price
    
    # kiểm tra ngân sách 
    if budget_input - final_price < 0:
        print("Not enough budget to this item.")
        within_budget = False
    
    # Lưu record
    purchases.append((item,category,price,discount,final_price))
    
    # cập nhật ngân sách 
    budget_input -= final_price
    print(f"Applied {discount:.0%} discount.")
    print(f"Added {item}. Remaining budget: ${budget_input:.2f}")
    print("\n")
    
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