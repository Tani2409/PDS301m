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

