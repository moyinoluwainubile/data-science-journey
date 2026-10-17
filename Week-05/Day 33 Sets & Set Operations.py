# Guided Practice
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a | b) # returns a combination of a and b, excluding the duplicate items
print(a & b) # returns a combination of a and b containing items common to both
print(a - b) # returns a set containing only items present in a and not in b
print(b - a) # returns a set containing only items present in b and not in a
names = ["Ada", "Tunde", "Ada"]
print(set(names)) # converts the list "names" to a set, removes the duplicate
# Practical Task
names1 = ["Ada", "John", "Moyin", "Ada", "Sarah", "John"]
names2 = ["Sarah", "David", "Moyin", "David", "Peter", "Sarah"]
# names1 and names2 are list of names
unique1 = set(names1)
unique2 = set(names2)
# unique1 and unique2 converts the lists name1 and name2 to sets, usin set() constructor.
print("Unique names in list 1:", unique1) # prints unique names in unique1, i.e removes duplicates
print("Duplicates removed from list 1:", len(names1) - len(unique1)) # prints duplicates removed from names1 compared to unique1
print("Unique names in list 2:", unique2) # prints unique names in unique2, i.e removes duplicates
print("Duplicates removed from list 2:", len(names2) - len(unique2)) # prints duplicates removed from names2 compared to unique2

common_names = unique1 & unique2 # combines names common to both sets in new set "common_names"
print("Names in both lists:", unique1 & unique2) # prints out common_names

firstlist_only_names = unique1 - unique2 
print("Names only in list 1:", unique1 - unique2) # returns only names present in unique1 and not in unique2

all_names = unique1 | unique2
print("All unique names:", unique1 | unique2) # returns names unique across both sets, unique1 and unique2, excluding duplicate items

# STRETCH TASK
names3 = input("Enter the first list of names, separated by commas: ")
names4 = input("Enter the second list of names, separated by commas: ")

list1 = [name.strip() for name in names3.split(",") if name.strip()]
list2 = [name.strip() for name in names4.split(",") if name.strip()]

set1 = set(list1)
set2 = set(list2)

print("Common names:", set1 & set2)