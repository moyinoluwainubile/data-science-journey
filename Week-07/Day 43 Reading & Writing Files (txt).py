# Guided Practice: Reading and Writing Files
with open("test.txt", "w") as f: #this creates test.txt, and opens it in write mode
    f.write("Line one\n") # this line and the one below write in test.txt
    f.write("Line two\n")

with open("test.txt", "r") as f: # this opens test.txt in read mode
    for line in f: # this loops through the lines in test.txt
        print(line.strip()) # this prints the lines in test.txt, and removes the newline character at the end of each line

# Practical Task: Reading and Writing Files
# Task 1: Take the output from your Day 42 toolkit (the stats function, the profile builder, at least) and save it to a .txt file using with open(..., "w"). Then open the file again in read mode and print its contents back out, confirming it matches.
with open("output.txt", "w") as f:
    f.write("The minimum number, maximum number, and average of numbers in these set of numbers is (0, 89, 22.22222222222222)\n")
    f.write("The minimum number, maximum number, and average of numbers in these set of numbers is (0.0, 78.0, 32.333333333333336)\n")
    f.write("My name is Moyinoluwa Inubile. I am a Doctor based in Ibadan, Oyo State, and I enjoy Reading.\n")
    f.write("My name is Salem Ashiegbu. I am a Teacher based in Ado-Ekiti, and I enjoy reading.\n")
with open("output.txt", "r") as f:
    for line in f:
        print(line.strip())
# Task 2 (Stretch): Use "a" mode to append a second run’s results to the same file without overwriting the first, then read the whole file back and confirm both runs are in there.
with open("output.txt", "a") as f: # appending a second run's results to the same file without overwriting the first
    f.write("The minimum number, maximum number, and average of numbers in these set of numbers is (0, 89, 22.22222222222222)\n")
    f.write("The minimum number, maximum number, and average of numbers in these set of numbers is (0.0, 15.0, 8.2)\n")
    f.write("My name is Moyinoluwa Inubile. I am a Doctor based in Ibadan, Oyo State, and I enjoy Reading.\n")
    f.write("My name is Shobowale Salem. I am a actor based in Lagos, and I enjoy sleeping.\n")
with open("output.txt", "r") as f: # reading the whole file to confirm both runs are there, using for loop to iterate through the lines in the file and print them out, using strip() to remove the newline character at the end of each line
    for line in f:
        print(line.strip())
