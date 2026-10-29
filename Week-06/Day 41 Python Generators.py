# Guided Practice
def counter(): # # creating a funtion for a counter
    # the yeilds to yeild the numbers 1 to 3
    yield 1
    yield 2
    yield 3
# for loop to loop through counter, and display/print yeild number i.e 1, 2, and 3 as output on individual lines
for n in counter():
    print(n)
# g is a variable created to point towards the function pointer, so whenever g is called, the function is called
g = counter()
# the print statements call the function via g, moving to the next yeild iteration with next.
print(next(g))
print(next(g))
print(next(g))
# displays 1, 2, and 3 on individual lines
# print(next(g)) # this generates an stopiteration error if not commented out

# practical Task 1
def squares(n):
    count = 1
    while count <= n:
        yield count**2
        count += 1
square = squares(5)
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
# practical Task 2
def squares(n):
    count = 1
    while count <= n:
        yield count**2
        count += 1
for square in squares(5):
    print(square)
# Practical Task 3
def num_square(n):
    square = []
    for num in range(1, n + 1):
        square.append(num**2)
    return square
print(num_square(5))
# Generator: yield produces one square at a time and pauses, resuming when the next value is requested. It doesn't build and return the entire list at once.
# Ordinary function: .append() stores every square in a list return gives back the completed list after the loop finishes.

# Stretch Task
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
for count, number in enumerate(fib(), start=1):
    print(number)
    if count == 10:
        break