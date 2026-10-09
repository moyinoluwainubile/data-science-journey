# Guided Practice 1
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)         # this nested for loop iterates through the values of i from 1 to 3 and j from 1 to 2, printing each combination of i and j.
# Guided Practice 2
for i in range(3):
    for j in range(3):
        if j == 1:
            break           # this nested for loop iterates through the values of i and j, but when j equals 1, the inner loop breaks, stopping further iterations of j for that value of i. The outer loop continues to the next value of i.
        print(i, j)
# Practical Task 1      PRINT STAR * TRIANGLE USING NESTED FOR LOOPS
for i in range(1,6):
    for j in range(i):
        print("*", end=' ')   # this nested for loop iterates through the values of i from 1 to 5, and for each value of i, it iterates through the values of j from 0 to i-1, printing each value of j on the same line separated by a space. The end=' ' argument in the print function prevents a newline after each print statement, allowing the values to be printed on the same line.
    print()                   # this print statement is used to create a new line after each iteration of the outer loop, so that the next set of asterisks is printed on a new line.
# Practical Task 2      PRINT A NUMBER VERSION OF THE TRIANGLE
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
# Stretch Task 1            PRINT THE TRIANGLE UPSIDE DOWN
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
# Stretch Task 2            PRINT THE TRIANGLE AS A CENTERED PYRAMID
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# Stretch Task 3            PRINT THE NUMBERS 1 TO 20, SKIP MULTIPLES OF 3 USING CONTINUE, STOP COMPLETELY ONCE IT PASSES 15 USING BREAK
for i in range(1, 21):
    for j in range(1, i + 1):
        if i > 15:
            break
        if i % 3 == 0:
            continue
        print(j, end="")
    print()