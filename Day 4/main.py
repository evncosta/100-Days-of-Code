# Rock Paper Scissors Game - Player vs Computer
import random

# ASCII art for rock, paper, scissors
choices = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

# Get player choice and generate computer choice
player_turn = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
comp_turn = random.randint(0, 2)

# Display choices using ASCII art
print("You chose:")
print(choices[player_turn])

print("The computer chose:")
print(choices[comp_turn])

# Determine winner using modulo arithmetic
if player_turn == comp_turn:
    print("It's a tie.")
elif (player_turn - comp_turn) % 3 == 1:
    print("You win!")
else:
    print("You lose.")
