# Practice 61 | Guess Number Game with Limited Chances

import random

# Generate a random number between 1 and 100
answer = random.randint(1, 100)
print("Guess the number between 1 and 100.")

# Initialize the number of chances
chances = 5

# Initialize a set to keep track of unique guesses
user_guesses_set = set()

while chances > 0:
    try:
        # Prompt the user to make a guess
        user_guess_input = input(f"\nEnter your guess (you have {chances} chances left): ")
        user_guess = int(user_guess_input)
        
        # Check if the guess is within the valid range
        if not 1 <= user_guess <= 100:
            print("Please guess a number within the range of 1 to 100.")
            continue
        
        # Check if the guess is correct
        if user_guess == answer:
            print("Well done! You found the right number 🤩")
            break
        elif user_guess < answer:
            print("Too low. Try a higher number ↑.")
        else:
            print("Too high. Try a lower number ↓.")
        
        # Check if the user has already guessed this number
        if user_guess in user_guesses_set:
            print("You've already guessed that number. Try again without losing a chance!")
        else:
            # Add the new guess to the set and decrement chances
            user_guesses_set.add(user_guess)
            chances -= 1  # Reduce chances only for new guesses
    except ValueError:
        # Handle non-integer input
        print("Invalid input. Please enter a valid integer between 1 and 100.")

# If the user runs out of chances without guessing correctly
if chances == 0:
    print(f"\nNice try! The correct number was {answer}.")
