# guided practice
def square(n): # a funtion to find the square of a given number
    return n * n # the given number in the argument called is returned after the calculation is done to the print statement to display

print(square(4)) # displays returned value of 4*4, 16
result = square(5) # result stores the returned value of 5*5, 25
print(result + 1) # displays result (25) + 1, 26

def shout(text): # a funtion to to "shout a value"
    print(text.upper()) # here, print is used intead of return, so the result of the argument is not stored, it is printed directly, as a string and capitalized using the .upper() method.

output = shout("hi") # the funtion is called with the argument "hi", which gets printed based on the print statement above
print(output) # output here stores nothing, and returns falsy i.e None, as the result of the function's argument is not stored there