items = int(input("how many items: "))
total_price = 0
for i in range(items):
    total_price += int(input("price of item: "))
print(f"Total price is:{total_price} ")
