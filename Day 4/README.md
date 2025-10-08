# Rock Paper Scissors Game

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A classic Rock Paper Scissors game implemented in Python with ASCII art visuals. This project was completed as part of **Day 4** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 4: Randomisation and Python Lists** in the 100 Days of Code curriculum. It combines random number generation with list manipulation to create an engaging game experience.

## 🎯 Project Overview

The Rock Paper Scissors game features:
- Interactive gameplay against the computer
- Visual ASCII art representations of choices
- Random computer selection using Python's random module
- Mathematical logic to determine the winner
- Clean and engaging user interface

## 🚀 How It Works

1. The game prompts the player to choose Rock (0), Paper (1), or Scissors (2)
2. The computer randomly selects one of the three options
3. Both choices are displayed using ASCII art for visual appeal
4. The winner is determined using mathematical logic
5. Results are displayed (win, lose, or tie)

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Random Module** - For computer's random choice selection
- **ASCII Art** - Visual representation of game elements
- **Mathematical Logic** - Modulo arithmetic for win/lose determination
- **List Data Structure** - Storing and accessing ASCII art

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Importing and using Python modules (random)
- Working with lists and list indexing
- Implementing game logic with conditional statements
- Creating interactive console applications
- Using mathematical operations for game mechanics
- Handling user input and validation

## 🎮 Game Rules

- Rock (0) beats Scissors (2)
- Scissors (2) beats Paper (1) 
- Paper (1) beats Rock (0)
- Same choices result in a tie

The win condition is determined using modulo arithmetic: `(player_turn - comp_turn) % 3 == 1`

## 📝 Example Output

```
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. 1

You chose:

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

The computer chose:

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

You win!
```

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
