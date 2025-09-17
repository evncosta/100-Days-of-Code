# Number Guessing Game - Guess a random number with difficulty levels
from art import logo
import random

# Generate random number between 1 and 100
number = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def easy_mode():
    chances = 10
    print(f"You chose the easy difficulty! You have {chances} chances in total.")

    while chances > 0:
        guess = int(input("Make a guess: "))
        
        # Provide feedback and adjust remaining chances
        if guess > number:
            print("Too high.")
            chances -= 1
            print(f"You now have {chances} chances remaining.")
        elif guess < number:
            print("Too low.")
            chances -= 1
            print(f"You now have {chances} chances remaining.")
        elif guess == number:
            print(f"The number was {number}! You win!")
            return

    # Handle game loss when chances run out
    if chances <= 0:
        print(f"You don't have any chances left. The number was {number}. You lost...")
        return

def hard_mode():
    chances = 5
    print(f"You chose the hard difficulty! You have {chances} chances in total.")

    while chances > 0:
        guess = int(input("Make a guess: "))
        
        # Provide feedback and adjust remaining chances
        if guess > number:
            print("Too high.")
            chances -= 1
            print(f"You now have {chances} chances remaining.")
        elif guess < number:
            print("Too low.")
            chances -= 1
            print(f"You now have {chances} chances remaining.")
        elif guess == number:
            print(f"The number was {number}! You win!")
            return

    # Handle game loss when chances run out
    if chances <= 0:
        print(f"The number was {number}. You lost...")
        return

# Start game with selected difficulty level
if difficulty == "easy":
    easy_mode()
elif difficulty == "hard":
    hard_mode()
else:
    print("Invalid input. Type 'easy' for easy mode or 'hard' for hard mode.")
