# Task 1: *args-based Stats Function
def stats(*numbers):
    if len(numbers)==0:
        return None
    min_num = numbers[0]
    max_num = numbers[0]
    # for loop to get minimum and maximum number in a list of values
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    # average of values calculation
    average = sum(numbers)/len(numbers)
    return min_num, max_num, average # returns the stats being calculated, min, max, and avg
# displays the stats calculated, i.e min, max, and avg
print(f"The minimum number, maximum number, and average of numbers in these set of numbers is {stats(20, 14, 5, 89, 34, 11, 1, 0, 26)}")
# interactive input
input_numbers = input("Enter numbers seperated by commas: ")
numbers = [float(number.strip()) for number in input_numbers.split(",")]
print(f"The minimum number, maximum number, and average of numbers in these set of numbers is {stats(*numbers)}")
# Task 2: **kwargs-based Profile Builder
def profile_builder(**kwargs):
    name = kwargs.get("name", "Unknown")
    profession = kwargs.get("profession", "Not specified")
    location = kwargs.get("location", "Not specified")
    hobby = kwargs.get("hobby", "Not specified")
    return f"My name is {name}. I am a {profession} based in {location}, and I enjoy {hobby}."
details = profile_builder(name = "Moyinoluwa Inubile", profession = "Doctor", location = "Ibadan, Oyo State", hobby = "Reading")
print(details)
# interactive input
input_name = input("Enter your name: ")
input_profession = input("Enter your profession: ")
input_location = input("Enter your location: ")
input_hobby = input("Enter your hobby: ")
profile = profile_builder(
    name = input_name.strip().title(),
    profession = input_profession.strip(),
    location = input_location.strip(),
    hobby = input_hobby.strip()
    )
print(profile)
# Task 3: A recursive helper for a Factorial function
def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    else:
        return n*factorial(n-1)
print(factorial(4))
# Interactive Input
factor = input("Enter the number to get factorial for: ")
num_factorial = [int(number.strip()) for number in factor.split(",")]
print(f"The factorial of {num_factorial[0]} is: {factorial(num_factorial[0])}")
# Task 4: A Generator Function: squares up to "n"
def squares(n):
    count = 1
    while count <= n:
        yield count**2
        count += 1
for square in squares(5):
    print(square)
num_square = input("Enter number to find squares up to: ")
square = [int(number.strip()) for number in num_square.split(",")]
print(f"The square of numbers up to {square[0]} is: {list(squares(square[0]))}")
