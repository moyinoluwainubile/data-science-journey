# Guided Practice - Nested Data Structures Usually a List of Dictionaries
students = [{"name": "Ada", "score": 80}, {"name": "Tunde", "score": 65}] # list of 2 dictionaries
print(students[0]["name"]) # prints name in first item (dictionary) i.e Ada
students[1]["score"] = 70 # changes score in second item (dictionary) from 65 to 70
for student in students: # for loop to loop through the list of dictionary
    print(f"{student['name']} scored {student['score']}") # argument to print name and score of each student (items/dictionary keys and values)
students.append({"name": "Chi", "score": 90}) # adds a new item (dictionary) to the list
print(len(students)) # pints out the number of items in the list (now 3, as a new item has been added)