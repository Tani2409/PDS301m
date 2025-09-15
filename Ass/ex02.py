budget = input('what is your total budget: $')
avaiable_items = ['apple', 'milk', 'chips', 'carrot']
cart =  []
total_budget = 0
discount = 0
while True:
    item = input('enter item to add to cart: ')
    if item in avaiable_items:
        cart.append(item)
        
        total_budget = total_budget + float(item_price)
        if total_budget > float(budget):
            diff = total_budget - float(budget)
            print(f'you are ${diff} over budget')
            break
    else:
        print(f'sorry, we dont have {item} in stock')