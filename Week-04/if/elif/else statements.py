# Guided Practice
score = 75
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# Practical Task and Stretch Challenge
while True:
    try:
        input_score = int(input("Enter your score (0-100): "))
        if 0 <= input_score <= 100:
            break
        else:
            print("Invalid score. Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
if input_score >= 90:
    print("A")
elif input_score >= 80:
    print("B")
elif input_score >= 70:
    print("C")
elif input_score >= 60:
    print("D")
else:
    print("F")