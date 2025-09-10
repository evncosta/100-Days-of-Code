# Hangman Game - Word guessing game with ASCII art
import random
from hangman_words import word_list
from hangman_art import stages, logo

# Initialize game variables
lives = 6
chosen_word = random.choice(word_list)
print(logo)

# Create initial placeholder for the word to guess
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Track game state and player progress
game_over = False
correct_letters = []
guessed_letters = set()

# Main game loop
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # Check for duplicate guesses
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        continue
    guessed_letters.add(guess)

    # Build display string with correctly guessed letters
    display = ""
    if guess in chosen_word and guess not in correct_letters:
        correct_letters.append(guess)

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # Handle incorrect guesses and life deduction
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        # Check for game loss
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # Check for game win
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Display current hangman stage
    print(stages[lives])
