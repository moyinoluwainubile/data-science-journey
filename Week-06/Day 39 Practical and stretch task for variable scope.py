# Practice task 1 and 2
total = 15
def reduce(number):
    global total
    total -= number

reduce(5)
print(total)
reduce(7)
print(total)

# Practical task 3
numbers = (1, 2, 3)
def something():
    print(numbers)

something()

# stretch task
cart_total = 0
# function to add price
def shopping_cart(price):
    global cart_total
    cart_total += price
    print(f"Item added: ₦{price}")
    print(f"Current cart total: ₦{cart_total}")
# function to reset cart
def reset_cart():
    global cart_total
    cart_total = 0
    print("Cart has been reset.")
# Add items
shopping_cart(500)
shopping_cart(250)
shopping_cart(1000)
# check total
print(f"Final cart total: ₦{cart_total}")
# reset the cart
reset_cart()
print(f"Cart total after reset: ₦{cart_total}")

# Stretch task using while loop
cart_total = 0

def shopping_cart():
    global cart_total
    while True:
        price = input("Enter item price (or 'done' to finish): ")
        if price.lower() == "done":
            break
        try:
            price = float(price)
            if price < 0:
                print("Price cannot be negative.")
                continue
            cart_total += price
            print(f"Current cart total: ₦{cart_total:.2f}")
        except ValueError:
            print("Invalid input. Enter a number or 'done'.")
    print(f"Final cart total: ₦{cart_total:.2f}")
def reset_cart():
    global cart_total
    cart_total = 0
    print("Cart total has been reset.")
# Run the shopping cart
shopping_cart()
# Reset the cart when needed
reset_cart()
