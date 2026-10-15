#   Guided Practice
point = (3, 4)
print(point[0]) #prints out item indexed o, first item which is 3

x, y = point #   unpacks tuple 'point' into varaible x = 3, and y = 4
print(x, y)  #   prints out the unpacked tuple as indicated with teh variables x, y

a, b = 1, 2  #Python assigns values to variable a, b, as 1, 2 respectively. Known as multiple assignment or iterable unpacking
a, b = b, a  # a, b is switched up to become b, a, with variable b coming before variable a
print(a, b)  # prints out variable a, b in the new order of b, a   

# practical task
about_me = (11, "February", 2001)
print(about_me)
(day, month, year) = about_me
print(f"My date of birth is the {day}th day of {month}, {year}")
day, year = year, day
print(year)
print(day)
