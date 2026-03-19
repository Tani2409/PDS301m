
while True:
    try:
        age_str = input("Please enter your age: ")
        age = int(age_str)
        print(f"You are {age} years old.")
        break  # Exit the loop if input was valid
    except ValueError:
        print("Invalid input. Please enter a whole number.")
