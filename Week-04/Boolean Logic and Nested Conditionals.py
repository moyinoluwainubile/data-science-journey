age = int(input("Enter your age: "))
# Nested Version
if age >= 18: # checks if user is 18 or older
    has_id = input("Do you have an ID? (yes/no): ").lower() == "yes" 
    if has_id: #checks if user has an ID
        print("You are eligible to vote.")
    else:
        print("You need an ID to vote.")
else: #checks if user is younger than 18
    print("You are not eligible to vote.")

# Equivalent Compound Version
if age >= 18 and input("Do you have an ID? (yes/no): ").lower() == "yes": #checks if user is 18 or older and has an ID
    print("You are eligible to vote.")
else: #checks if user is younger than 18 or does not have an ID
    print("You are not eligible to vote.")


# Guided Practice
password = "abc123"
has_length = len(password) >= 8 # Checks length of Password
has_number = any(char.isdigit() for char in password) # checks if number is in password
print(has_length) #prints True or False depending on the length of the password
print(has_number) #prints True or False depending on if there is a number in the password
print(has_length and has_number) #prints True if both conditions are met, otherwise prints False

#Practical Task and Stretch Challenge
password = input("Enter a password: ")
has_length = len(password) >= 8 # Checks length of Password
has_number = any(char.isdigit() for char in password) # checks if number is in password
has_uppercase = any(char.isupper() for char in password) # checks if there is an uppercase letter in the password
has_special_char = any(not char.isalnum() for char in password) # checks if there is a special character in the password
print(has_length) #prints True or False depending on the length of the password
print(has_number) #prints True or False depending on if there is a number in the password
print(has_uppercase) #prints True or False depending on if there is an uppercase letter in the password
print(has_special_char) #prints True or False depending on if there is a special character in the password
print(has_length and has_number and has_uppercase and has_special_char) #prints True if all conditions are met, otherwise prints False

if has_length: # checks if password has at least 8 characters
    if has_number: # checks if password contains at least one number
        if has_uppercase: # checks if password contains at least one uppercase letter
            if has_special_char: # checks if password contains at least one special character
                print("Your password is strong.")
            else:
                print("Your password must contain at least one special character.")
        else:
            print("Your password must contain at least one uppercase letter.")
    else:
        print("Your password must contain at least one number.")
else:
    print("Your password must be at least 8 characters long.")
#checks if all conditions are met