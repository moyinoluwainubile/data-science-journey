phonebook = {"Moyin": 7098765432, "Salem": 8043216754, "Ruth": 9143565648}
if "Salem" in phonebook:
    print("Yes, Salem's number is in the phonebook.")
else:
    print("Name not found in phonebook!")

phonebook["Eben"] = 9065437890
print(phonebook)

phonebook.update({"Moyin": 9065786787})
print(f"Moyin's number: {phonebook["Moyin"]}")

phonebook.pop("Eben")
print(phonebook)
print(len(phonebook))
print(phonebook.items())
print(phonebook.keys())
print(phonebook.values())
# interactive phonebook lookup code
name = input("Input a name to search: ")
if name == "Moyin":
    print(f"Moyin's number: {phonebook["Moyin"]}")
elif name == "Salem":
    print(f"Salem's number: {phonebook["Salem"]}")
elif name == "Ruth":
    print(f"Ruth's number: {phonebook["Ruth"]}")
else:
    print(f"The details of {name} could not be found in the phonebook!")
# alternative interactive phonebook lookup code
name = input("Input a name to search: ")
number = phonebook.get(name)

if number is not None:
    print(f"{name}'s number: {number}")
else:
    print(f"The details of {name} could not be found in the phonebook!")