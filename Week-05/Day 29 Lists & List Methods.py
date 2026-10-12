# Guided practice
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # displays item indexed 0, apple
print(fruits[-1])  # displays item indexed -1, cherry
print(fruits[1:3]) # displays items indexed range from 1 to 3, but not including 3 i.e banana, cherry
fruits.append("mango") # adds mango to the fruits list, at the end of the list
fruits.remove("banana") # removes banana from the list (first instance if two instances)
print(fruits)   # displays the new list which excludes banana, and includes mango
print(len(fruits))  # displays the number of items in the list, 3
# Practical Task
tasks = ["cook", "eat", "practice"]
tasks.append("bath")
tasks.remove("eat")
tasks.sort  # sorts the list in ascending order
print(tasks) # prints the sorted list
tasks.sort(reverse = True)
print(tasks) # tasks.sort(reverse = True) sorts out in descending order, and this prints it out
for i, task in enumerate(tasks, 1): # helps to print out in a numbered list, one item per line
    print(f"{i} {task}")
done = [] # creates an empty list 'done'
done.append(tasks.pop(0)) # removes the task index 0 which is practice, due to descending order sorting, and adds it to list 'done'
for i, done in enumerate(done, 1):
    print(f"{i} {done}")