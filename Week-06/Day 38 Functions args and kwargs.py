# Guided Practice
def total(*args): # a functio  to get total of numbers
# *args (args there can be substituted for anything else, not a fixed function, * does the work) allows to add as much positional arguments as needed, if initially unknown, in a tuple
    return sum(args) # sums of the argument values provided
print(total(1, 2, 3, 4)) # displays the sum of the argument values in the print statement

def describe(**kwargs): # a funtion to describe 
# **kwargs (kwargs there can be substituted for something else, ** does the work) allow to add as much keyword arguments as needed, collected in a dictionary of arguments
    for key, value in kwargs.items(): # to loop through items in the dictionary of argument
        print(f"{key}: {value}") # to display the key and value of the dictionary of argument
describe(name="Ada", city="Lagos") # the keyword argument collected as a dictionary of argument