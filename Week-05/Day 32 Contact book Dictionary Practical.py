phonebook = {
    "dad": {"name": "Alabi", "phone_number": "07054637897", "city": "Ibadan"},
    "mum": {"name": "Cynthia", "phone_number": "09076543456", "city": "Ikeja"},
    "brother": {"name": "Victor", "phone_number": "08023455432", "city": "Akure"},
    "me": {"name": "Ayomide", "phone_number": "08098766789", "city": "Ibadan"}
}
# loop through the whole contact book and print each person with their details
for key, obj in phonebook.items():
    print(key)
    for value in obj:
        print(value + ':', obj[value])
# add a new contact, update one detail for an existing contact, and print the result
phonebook.update({"sister": {"name": "Salem", "phone_number": "07067122176", "city": "Ikeja"}}) # adds new contact
for key, value in phonebook["sister"].items(): # loops through inner dictionary sister and print displays its keys and values
    print(f"{key}: {value}")
phonebook["dad"]["city"] = "Ikeja" # updates city in dad to Ikeja       # addresses task 4, chaining keys to look up one person's city
print(phonebook["dad"]["city"]) # prints updated city in dad
# loop through the whole updated contact book and print each person with their details
for key, obj in phonebook.items():
    print(key)
    for value in obj:
        print(value + ':', obj[value])

# stretch task: make the contact book interactive with a while loop and input(): add a contact, look one up, or show everyone. Use .get(), so a missing name doesn't crash it.
while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add a contact")
    print("2. Look up a contact")
    print("3. Show everyone")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        contact_name = input("Enter the contact's name: ")
        phone = input("Enter their phone number: ")
        city = input("Enter their city: ")

        phonebook[contact_name] = {
            "name": contact_name,
            "phone_number": phone,
            "city": city
        }

        print(f"{contact_name} has been added successfully!")
    elif choice == "2":
        name = input("Enter the contact name to look up: ")

        contact_name = phonebook.get(name)

        if contact_name is not None:
            print(f"Name: {contact_name['name']}")
            print(f"Phone: {contact_name.get('phone_number')}")
            print(f"City: {contact_name.get('city')}")
        else:
            print(f"{name} was not found in the contact book.")
    elif choice == "3":
        for key, contact in phonebook.items():
            print(f"\nContact name: {key}")
            for values in contact:
                print(values + ":", contact[values])
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-4.")