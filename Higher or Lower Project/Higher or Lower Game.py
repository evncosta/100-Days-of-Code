from art import logo, vs
from game_data import data
import random

item_a = random.choice(data)
item_b = random.choice(data)
while item_b == item_a:
    item_b = random.choice(data)

score = 0
game_over = False

print(logo)
print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")


def compare_against():
    print(vs)
    print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")


compare_against()

while not game_over:
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if item_a['follower_count'] > item_b['follower_count']:
        correct_answer = "A"
        winner = item_a
    else:
        correct_answer = "B"
        winner = item_b

    if guess == correct_answer:
        score += 1
        item_a = winner
        item_b = random.choice(data)
        while item_b == item_a:
            item_b = random.choice(data)
        print(f"You're right! Current score: {score}")
        print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
        compare_against()
    elif guess in ["A", "B"]:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
    else:
        print("Invalid input. Type either 'A' to choose A or 'B' to choose B.")