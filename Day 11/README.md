# Blackjack Game

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A simplified version of the classic casino card game Blackjack, also known as 21. This capstone project was completed as part of **Day 11** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎯 Project Overview

The Blackjack game features:
- Complete card dealing and scoring system
- Intelligent Ace handling (11 or 1 points)
- Player turn with hit/stand options
- Computer dealer AI that follows standard rules (hit until 17+)
- Win/lose/draw condition checking
- Professional ASCII art interface
- Multiple game sessions support

## 🚀 How It Works

1. The game displays the Blackjack logo and welcomes players
2. Both player and computer receive two initial cards
3. Player can choose to hit (draw another card) or stand (end their turn)
4. Computer automatically draws cards according to casino rules
5. Scores are calculated with special handling for Aces
6. The winner is determined based on final scores and bust conditions

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Random Module** - For card dealing and shuffling
- **List Operations** - Card management and scoring
- **Conditional Logic** - Game rules and win conditions
- **While Loops** - Player and computer turn management
- **Function Definitions** - Modular game design

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Complex game state management
- Conditional logic and flow control
- List manipulation and scoring calculations
- User input validation
- Modular programming with functions
- AI behavior implementation for computer opponent
- Edge case handling (Aces, bust conditions, blackjacks)

## 🎓 Course Context

This project was part of **Day 11: The Blackjack Capstone Project** in the 100 Days of Code curriculum. It represents a comprehensive application of all concepts learned in the beginner section.

## 🎮 Game Rules

- **Card Values**: Number cards = face value, Face cards = 10, Ace = 11 or 1
- **Blackjack**: 21 with first two cards (automatic win)
- **Player Turn**: Choose to hit (draw) or stand (stop)
- **Dealer Rules**: Must hit until score reaches 17 or higher
- **Bust**: Score over 21 (automatic loss)
- **Winning**: Higher score without busting (or dealer busts)

## 📁 Project Structure

```
Day 11/
│
├── main.py         # Main game logic
├── art.py          # ASCII art module
└── README.md       # Project documentation
```

## 📝 Example Output

```
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
Do you want to play Blackjack (y/n)? y
Your cards: [8, 10], current score: 18
Computer's first card: 7
Do you want to draw another card (y/n)? n
Computer drew a 10. Computer's cards: [7, 10], current score: 17
Your final hand: [8, 10], final score: 18
Computer's final hand: [7, 10], final score: 17
You got a higher score! You win!
```

## 🔄 Related Projects

This capstone project concludes the beginner section of the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
