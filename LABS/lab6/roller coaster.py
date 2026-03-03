# Get user input
height_str = input("Enter your height in cm: ")
height = float(height_str)

age_str = input("Enter your age: ")
age = int(age_str)

# Check if both conditions are met
if height >= 120 and age >= 10:
    print("Access granted. Enjoy the ride!")
else:
    print("Access denied. You do not meet the requirements.")
