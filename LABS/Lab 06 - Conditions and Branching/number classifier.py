# Get user input for a number
num_str = input("Enter a number: ")
number = float(num_str)

# Classify the number
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
