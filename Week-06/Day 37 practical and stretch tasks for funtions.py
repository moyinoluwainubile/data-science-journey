# Temperature converter
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    return celsius
# Example usages
print(f"200°F is equal to {fahrenheit_to_celsius(200):.2f}°C")
print(f"100°F is equal to {fahrenheit_to_celsius(100):.2f}°C")
print(f"120°F is equal to {fahrenheit_to_celsius(120):.2f}°C")
# while loop to request for input
while True:
    try:
        input_fahrenheit = float(input("Enter the Fahrenheit: "))
        c_temp = fahrenheit_to_celsius(input_fahrenheit)
        print(f"{input_fahrenheit} °F is equal to {c_temp:.2f}°C")
        break
    except ValueError:
        print("Invalid input, please enter a numeric Fahrenheit value.")
        
# Grading logic
def grading_scale(score):
    """Return a letter grade for each score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# Example usages
print(f"Moyinoluwa's grade is {grading_scale(90)}")
print(f"Ayomide's grade is {grading_scale(50)}")
print(f"Ruth's grade is {grading_scale(40)}")
# while loop to request for input
while True:
    try:
        input_score = int(input("Enter your score (0-100): "))
        if 0 <= input_score <= 100:
            break
        else:
            print("Invalid score. Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
print("Your grade is:", grading_scale(input_score))

# fizz buzz
def fizz_buzz(number):
    """display FizzBuzz, Fizz, Buzz, or the number"""
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
for i in range(1, 101):
    print(fizz_buzz(i))