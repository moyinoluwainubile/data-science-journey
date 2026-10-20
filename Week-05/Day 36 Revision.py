# fixing broken snippets
# snippet one
scores = [70, 85, 90]
total = 0
for score in scores:
    total = total + score

average = total / len(scores)
print("Average:", average)

#snippet two
student = {"name": "Ada", "scores": (70, 80)}
student["scores"] = (75, 80)

tags = set()
tags.add("python")

print(student["scores"])
print(tags)