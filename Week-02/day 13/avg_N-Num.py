numbers= [15, 20, 55, 38, 42, 60]

sum1 = sum(numbers)
average = sum1 / len(numbers)
if len(numbers) == 0:
    print("The list is empty. Cannot compute average.")
else:
    print("The average of the numbers is:", average)