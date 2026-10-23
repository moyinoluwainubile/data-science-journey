# Guided practice 1
count = 0
def increment():
    global count # used the global keyword to call the global scope variable count, so as to be able to change it's value inside the function
    count = count + 1
    print(count) # displays count + 1, 1
increment()

# Guided practive 2
total = 100
def spend(amount):
    global total # global keyword used to allow for changes to be made to global scope variable total
    total -= amount
# spend() funtion called twice with different arguments, 30 and 20
spend(30)
spend(20)
print(total) # displays total - amount, both instances, 70 and 30