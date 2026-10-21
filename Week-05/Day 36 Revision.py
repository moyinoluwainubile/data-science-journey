# fixing broken snippets
# snippet one
scores = [70, 85, 90]
total = 0
for score in scores: # added colon infront of this to correct it
    total = total + score

average = total / len(scores) # having score initially was referencing a single score, which would have raised an error, corrected to len(scores)
print("Average:", average)

#snippet two
student = {"name": "Ada", "scores": (70, 80)}
student["scores"] = (75, 80)

tags = set() # makes an empty dictionary with {}, and dictionaries dont have a .add() method, would have raised error, corrected to tags = (), a set, so as to accomodate the line below
tags.add("python")

student.update({"grade": ("B", "A")}) # added this so that grade below will print, as grade was not existing before now.
print(student["grade"])
print(tags)
