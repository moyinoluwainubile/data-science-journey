# Guided Practice 1
def countdown(n): # a function to countdown from 'n'
    # base case
    if n == 0:
        print("Go!")
        return
    # Recursive case
    print(n)
    countdown(n - 1)
countdown(4) # n = 4 in the function here, so the countdown is done from 4 to 0, when it gets to 0, it displays "Go!"
# Guided practice 2
def factorial(n): # A fution to get the factorial of 'n'
    # Base case and recursive case 
    return 1 if n == 1 else n * factorial(n - 1) # here, n multiplied by factorial of n-1 is returned for each run, which is totaled to get the factorial of n
print(factorial(5)) # n = 5 in the function here, and it displays the factorial of 5, 120
# Practical Task 1
def sum_to(n):
    return 0 if n == 0 else n + sum_to(n-1) #The recursive calls count down until n reaches 0.
print(sum_to(5))
# practical Task 2
def fib(n):
    if n <= 1: # corrected with base case
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(8))
# stretch task
def count_vowels(word):
    if word == "":
        return 0
    if word[0].lower() in "aeiou":
        return 1 + count_vowels(word[1:])
    else:
        return count_vowels(word[1:])
print(count_vowels("hello"))
