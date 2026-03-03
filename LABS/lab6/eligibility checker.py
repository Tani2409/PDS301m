# Get user input for age
age_str = input("Please enter your age: ")
age = int(age_str)

# Check if the user is 18 or older
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
