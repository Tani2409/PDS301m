score = input("Enter your score 0-100: ")
score = int(score)
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score < 90:
        print("B")
elif score >= 70 and score < 80:
        print("C")
elif score >= 60 and score < 70:
        print("D")
elif score >= 0 and score < 60:
        print("F")
else:
        print("Invalid score. Please enter a number between 0 and 100.")
    