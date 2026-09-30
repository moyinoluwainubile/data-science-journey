name = "    Moyinoluwa    "
print(name.strip()) # prints the string with leading and trailing whitespace removed
print(name.strip().upper()) # prints the string with leading and trailing whitespace removed and in uppercase
print(name[1:10]) # prints the characters from index 1 to 9 of the string
print(name[0:4]) # prints the first four characters of the string
print(len(name)) # prints the length of the string

messy = "    mOyInOlUwA BlEsSiNg InUbIlE    "
print(messy.strip()) # prints the string with leading and trailing whitespace removed
print(messy.strip().replace("mOyInOlUwA", "Pelumi")) # prints the string with leading and trailing whitespace removed and "mOyInOlUwA" replaced by "Pelumi"
print(messy.strip().upper()) # prints the string with leading and trailing whitespace removed and in uppercase
print(messy.strip().lower()) # prints the string with leading and trailing whitespace removed and in lowercase
print(messy.strip().title()) # prints the string with leading and trailing whitespace removed and with the first character of each word in uppercase
print(messy.strip().capitalize()) # prints the string with leading and trailing whitespace removed and with the first character in uppercase


sentence = "I am learning Python programming and I am excited about it!"
print(sentence.split()) # prints the string split into a list of words
print("-".join(sentence.split())) # prints the string with "-" inserted between each word