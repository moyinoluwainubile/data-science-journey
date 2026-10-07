# Guided practice
count = 0
while count < 5:
    print(count)
    count += 1      # adding this ensures the loop does not run forever, looping through 0, stops it at 5
print("Done")

secret = 9
guesses_taken = 0
max_attempts = 5

while guesses_taken < max_attempts:
    guess = int(input("Guess the secret number between 1 and 15: "))
    guesses_taken += 1
    if guess == secret:
        print("Correct!")
        print(f"You guessed the secret number in {guesses_taken} attempts.")
        break
    elif guess > secret:
        if guesses_taken < max_attempts:
            print("Too high! Try again.")
        else:
            print("Too high!")
    else:
        if guesses_taken < max_attempts:
            print("Too low! Try again.")
        else:
            print("Too low!")
else:
    print(f"You've run out of attempts. The secret number was {secret}.")