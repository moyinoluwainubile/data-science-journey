def find_smallest_largest(numbers): # defines the function to find smallest and largest numbers
    smallest = min(numbers) # explains what smallest means in the function defined
    largest = max(numbers)  # explains what largest means in the function defined

    return smallest, largest    # returns smallest and largest values as a tuple

values = [8, 3, 12, 5, 1]   # variable 'values' containing a list of numbers

smallest, largest = find_smallest_largest(values)   # tuple unpacking, python assigns smallest value to smallest, and largest value to largest

print("Smallest:", smallest)    # displays Smallest: 1
print("Largest:", largest)      # displays Largest: 12