balance = int(input("Enter the initial balance: "))
tickets = 0
while balance >= 15:
    balance -= 15
    tickets += 1
print(f"You bought {tickets} tickets and your remaining balance is {balance}.")