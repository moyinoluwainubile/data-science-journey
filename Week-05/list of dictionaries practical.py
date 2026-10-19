# Practice and stretch task
students = [
    {"name": "Olamide", "score": 78},
    {"name": "David", "score": 81},
    {"name": "Oluwaseun", "score": 65},
    {"name": "Moyinoluwa", "score": 97},
    {"name": "Salem", "score": 90},
    {"name": "John", "score": 55}
]
    
# students grading system
for student in students:
    score = student["score"]

    if score >= 90:
        student["grade"] = "A"
    elif score >= 80:
        student["grade"] = "B"
    elif score >= 70:
        student["grade"] = "C"
    elif score >= 60:
        student["grade"] = "D"
    else:
        student["grade"] = "F"

for student in students:
    print(f"Our student {student['name']}, scored {student['score']}, with grade level {student['grade']} in the examination")

# average of score
total_score = 0

for student in students:
    total_score = total_score + student["score"]
average = total_score / len(students)
print(f"Class Average is: {average:.2f}")

#highest scoring student
highest_student = students[0]

for student in students:
    if student["score"] > highest_student["score"]:
        highest_student = student
print(f"The highest scoring student is {highest_student['name']}, with a score of {highest_student['score']}.")

# grade counting 
grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for student in students:
    grade = student["grade"]
    grade_count[grade] += 1

for grade, count in grade_count.items():
    print(f"Grade {grade}: {count} student(s)")
