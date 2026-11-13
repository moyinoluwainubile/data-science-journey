# Guided Practice
import csv #imports CSV module to work with CSV files
with open("scores.csv", "w", newline="") as f: #create and open scores.csv in write mode, using newline="" to prevent extra blank lines in the file
    writer = csv.writer(f) # using csv.writer() method to write to the file, creating a writer object
    writer.writerow(["name", "score"]) # using .writerow() method to write a row to the file, passing in a list of values to write as a single row
    writer.writerow(["Ada", 80])
    writer.writerow(["Tunde", 65])
# scores.csv is automatically closed outside the with block
with open("scores.csv", "r") as f: # reopening scores.csv in read mode, using with open() to automatically close the file when done
    reader = csv.reader(f) # using csv.reader() method to read the file, creating a reader object
    for row in reader: # using a for loop to iterate through the rows in the file, printing each row to the console
        print(row) # prints each row to the console, which is a list of values in the row

# Practical Task: Take your Day 34 list of 5 student dictionaries (name, score, grade) and save it to a CSV file, one row per student. 
# Then read the file back and print each row, and calculate the class average from the CSV data you just read (cast the score column to int first).
fields = ['Name', 'Score', 'Grade'] # Define header and data rows
# List of lists, containing students data
students = [
    ["Olamide", 78, "B"],
    ["David", 81, "B+"],
    ["Oluwaseun", 65, "C"],
    ["Moyinoluwa", 97, "A"],
    ["Salem", 90, "A-"],
]
with open("students.csv", "w", newline="") as f: # create and open students.csv in write mode, using newline="" to prevent extra blank lines in the file
    writer = csv.writer(f) # using csv.writer() method to write to the file, creating a writer object
    writer.writerow(fields) # using .writerow() method to write the header row to the file, passing in a list of values to write as a single row
    writer.writerows(students) # using .writerows() method to write multiple rows to the file, passing in a list of lists to write as multiple rows
# students.csv is automatically closed outside the with block
with open("students.csv", "r") as f: # reopening students.csv in read mode, using with open() to automatically close the file when done
    reader = csv.reader(f) # using csv.reader() method to read the file, creating a reader object
    total_score = 0
    num_students = 0
    next(reader)  # Skip the header row
    for row in reader:
        print(row)
        total_score += int(row[1])
        num_students += 1
# Calculate and print the class average
if num_students > 0:
    class_average = total_score / num_students
    print(f"The class average is {class_average}")

# Stretch Task: Look up csv.DictReader and csv.DictWriter, which let you read/write rows as dictionaries instead of plain lists, use the column headers as keys. 
# Try rewriting your practical task with one of them.
with open("students.csv", "r") as f: # reopening students.csv in read mode, using with open() to automatically close the file when done
    reader = csv.DictReader(f) # using csv.DictReader() method to read the file, creating a reader object
    total_score = 0
    num_students = 0
    for row in reader:
        print(row)
        total_score += int(row['Score'])
        num_students += 1
# Calculate and print the class average
if num_students > 0:
    class_average = total_score / num_students
    print(f"The class average is {class_average}")
