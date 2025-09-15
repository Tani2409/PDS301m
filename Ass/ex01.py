budget = input('what is your total budget: $')
list =[]
total = 0
while True:
    item_price = input('enter item price: $')
    
    total = total + float(item_price)
    if total > float(budget):
        diff = total - float(budget)
        print(f'you are ${diff} over budget')
        break
print(f'total spent: ${total}') 
print('you exceeded your budget')
    
    