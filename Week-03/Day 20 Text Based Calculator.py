def calculator():
    print("Welcome to my Text-Based Calculator!")
    print("You can only perform simple addition, subtraction, multiplication, and division operations.")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator. Please try again.")
                continue
            
            print(f"The result of {num1} {operator} {num2} is: {result}")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        again = input("Would you like to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the calculator function
calculator()