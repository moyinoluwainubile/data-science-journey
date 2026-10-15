person = {"name": "Ada", "age": 30} # a dictionary containing 2 items
print(person["name"]) # this prints the name value "Ada"
person["city"] = "Lagos" # this adds a new item "city: lagos" to the list
person["age"] = 31 # this changes the value of the key age to 31
print(person) # this prints out the list of the dictionary (variable "person")
print(person.get("phone")) # this will return none as there is no key "phone"
print("age" in person) # this prints True, as the key "age" exists, with a value 31
person.pop("city") # this removes the item with the key "city"
print(person.keys()) # this prints out a list of all the keys in the dictionary, which will now exclude city