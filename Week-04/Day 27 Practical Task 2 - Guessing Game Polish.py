import random

def play_round(round_number, players_list, best_scores, min_number, max_number):
    print("\n=======================")
    print(f"      ROUND {round_number}      ")
    print("=======================")

    secret = random.randint(min_number, max_number)
    guesses_taken = 0

    # Each player gets exactly 3 valid guesses per round.
    turns_per_player = 3
    max_attempts = len(players_list) * turns_per_player

    player_index = 0

    while guesses_taken < max_attempts:
        current_player = players_list[player_index]

        print(f"\n--- {current_player}'s Turn ---")

        try:
            guess = int(
                input(
                    f"{current_player}, guess the secret number "
                    f"between {min_number} and {max_number}: "
                )
            )
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue

        # Reject guesses outside the selected difficulty range.
        if guess < min_number or guess > max_number:
            print(
                f"Out of range! Please enter a number "
                f"between {min_number} and {max_number}."
            )
            continue

        # Only valid, in-range guesses use an attempt.
        guesses_taken += 1

        if guess == secret:
            print(f"Correct! {current_player} wins this round! 🎉")
            print(
                f"You guessed the secret number "
                f"in {guesses_taken} attempts."
            )

            # Keep the player's fewest guesses needed to win.
            if (
                best_scores[current_player] is None
                or guesses_taken < best_scores[current_player]
            ):
                best_scores[current_player] = guesses_taken

            return current_player

        elif abs(guess - secret) <= 2:
            print("Warm! 🔥 You're within 2 of the secret number!")

        elif guess > secret:
            if guesses_taken < max_attempts:
                print("Too high! Passing to the next player...")
            else:
                print(f"Too high! {current_player} is out of attempts.")

        else:
            if guesses_taken < max_attempts:
                print("Too low! Passing to the next player...")
            else:
                print(f"Too low! {current_player} is out of attempts.")

        # Move to the next player, then return to the first player.
        player_index = (player_index + 1) % len(players_list)

    print(
        f"\nRound Over! Everyone ran out of attempts. "
        f"The secret number was {secret}."
    )
    return None


# --- Main Game Setup ---

print("🏆 WELCOME TO THE NUMBER GUESSING GAME 🏆\n")

# Ask how many players will participate.
while True:
    try:
        num_players = int(input("How many players want to play? "))

        if num_players < 1:
            print("Please enter at least 1 player.")
            continue

        break

    except ValueError:
        print("Invalid input! Please enter a whole number.")


# Select the difficulty level.
difficulty_levels = {
    "easy": 10,
    "medium": 30,
    "hard": 100
}

print("\nChoose your difficulty:")
print("1. Easy   (numbers 1–10)")
print("2. Medium (numbers 1–30)")
print("3. Hard   (numbers 1–100)")

difficulty_options = {
    "1": "easy",
    "2": "medium",
    "3": "hard"
}

while True:
    difficulty_choice = input(
        "\nEnter your choice (1, 2, or 3): "
    ).strip().lower()

    if difficulty_choice in difficulty_options:
        difficulty = difficulty_options[difficulty_choice]
        break

    elif difficulty_choice in difficulty_levels:
        difficulty = difficulty_choice
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, Easy, Medium, or Hard.")


min_number = 1
max_number = difficulty_levels[difficulty]

print(f"\nDifficulty selected: {difficulty.title()}")
print(f"Secret numbers will range from {min_number} to {max_number}.")


# Create the player lists and scoreboards.
players = []
scores = {}
best_scores = {}

for i in range(num_players):
    name = input(f"Enter name for Player {i + 1}: ").strip()

    if not name:
        name = f"Player {i + 1}"

    players.append(name)
    scores[name] = 0
    best_scores[name] = None


current_round = 1


# --- Main Game Loop ---

while True:
    winner = play_round(
        current_round,
        players,
        best_scores,
        min_number,
        max_number
    )

    # Update the number of round victories.
    if winner in scores:
        scores[winner] += 1

    print("\n🏆 CURRENT LEADERBOARD:")
    for player, score in scores.items():
        print(f" {player}: {score} victories")

    print("\n⭐ BEST ROUND SCORES (fewest guesses to win):")
    for player, best_score in best_scores.items():
        if best_score is None:
            print(f" {player}: No wins yet")
        else:
            print(f" {player}: {best_score} guesses")

    play_again = input(
        "\nDo you want to play another round? (yes/no): "
    ).strip().lower()

    if play_again not in ("yes", "y"):
        print("\nThanks for playing! FINAL SCORE:")

        for player, score in scores.items():
            print(f" {player}: {score} victories")

        print("\n⭐ FINAL BEST ROUND SCORES:")
        for player, best_score in best_scores.items():
            if best_score is None:
                print(f" {player}: No wins yet")
            else:
                print(f" {player}: {best_score} guesses")

        print("Goodbye!")
        break

    current_round += 1
