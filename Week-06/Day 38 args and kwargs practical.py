# Practical Task 1, write a funtion using *args to get average
def average(*avg):
    average = sum(avg)/len(avg)
    return average
print(average(20, 30, 40, 50))
input_numbers = input("Enter numbers seperated by commas: ")
numbers = [float(number.strip()) for number in input_numbers.split(",")]
print("Average:", average(*numbers))

# Practical task 2
def summary(**kwargs):
    print(f"My name is {kwargs['name']}, I work at {kwargs['work']}, and I like eating hot {kwargs['food']} in the afternoon.")

summary(name="Moyinoluwa", work="HugoTech", food="rice")