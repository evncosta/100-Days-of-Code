# Number Guessing Game

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A challenging number guessing game with multiple difficulty levels that tests your intuition and deduction skills. This project was completed as part of **Day 12** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 12: Scope & Number Guessing Game** in the 100 Days of Code curriculum. It demonstrates practical application of scope concepts and game design principles.

## 🎯 Project Overview

The Number Guessing Game features:
- Two difficulty levels: Easy (10 attempts) and Hard (5 attempts)
- Random number generation between 1-100
- Progressive feedback system (too high/too low)
- Attempt counter and remaining chances display
- Professional ASCII art interface
- Win/lose condition handling

## 🚀 How It Works

1. The game displays an ASCII art logo and welcome message
2. Players choose between easy or hard difficulty
3. The game generates a random number between 1-100
4. Players make guesses and receive feedback (too high/too low)
5. The game tracks remaining attempts
6. Players win by guessing correctly or lose by running out of attempts

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Random Module** - For generating random numbers
- **Function Definitions** - Separate functions for each difficulty level
- **While Loops** - Game loop with attempt tracking
- **Conditional Statements** - Feedback and win/lose conditions
- **Input Validation** - Difficulty selection validation

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Random number generation and range selection
- Function parameterization and modular design
- Loop control with conditional exits
- User feedback systems
- Difficulty level implementation
- Game state management and attempt tracking
- Clean program flow and organization

## 🎮 Difficulty Levels

- **Easy Mode**: 10 attempts to guess the number
- **Hard Mode**: 5 attempts to guess the number  
- **Progressive Feedback**: "Too high" or "Too low" hints after each guess
- **Attempt Tracking**: Clear display of remaining chances

## 📁 Project Structure

```
Day 12/
│
├── main.py               # Main game logic
├── art.py                # ASCII art module
└── README.md             # Project documentation
```

## 📝 Example Output

```
    ___                       _   _                                  _               
  / _ \_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100
Choose a difficulty. Type 'easy' or 'hard': hard
You chose the hard difficulty! You have 5 chances in total.
Make a guess: 50
Too high.
You now have 4 chances remaining.
Make a guess: 25
Too low.
You now have 3 chances remaining.
Make a guess: 37
Too high.
You now have 2 chances remaining.
Make a guess: 31
The number was 31! You win!
```

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
