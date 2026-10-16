scores = {"Ada": 80, "Tunde": 65} # dictionary 
for name in scores: # loops through keys
    print(name) # prints the keys line by line
for score in scores.values(): # loops through the values
    print(score) # prints the values line by line
for name, score in scores.items(): # loops through the keys and values
    print(f"{name} scored {score}") # prints the keys and values line by line