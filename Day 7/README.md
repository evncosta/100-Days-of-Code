# Hangman Game

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A classic word-guessing game implemented in Python with ASCII art visuals and interactive gameplay. This project was completed as part of **Day 7** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎯 Project Overview

The Hangman game features:
- Random word selection from a custom word list
- Visual ASCII art that progresses with incorrect guesses
- Life-based gameplay system (6 lives)
- Input validation and duplicate guess prevention
- Real-time display of correctly guessed letters
- Win/lose condition checking

## 🚀 How It Works

1. The game selects a random word and displays it as blanks
2. Players guess one letter at a time
3. Correct guesses reveal the letter's positions in the word
4. Incorrect guesses reduce lives and advance the hangman ASCII art
5. The game continues until the word is guessed or lives run out

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Random Module** - For random word selection
- **Custom Modules** - External word list and ASCII art files
- **String Manipulation** - Building and updating the display
- **Set Operations** - Tracking guessed letters efficiently
- **Game State Management** - Life system and win/lose conditions

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Working with external modules and imports
- Implementing game loops and state management
- String manipulation and pattern matching
- Set operations for efficient data tracking
- ASCII art integration for visual feedback
- User input validation and error handling

## 🎓 Course Context

This project was part of **Day 7: Hangman** in the 100 Days of Code curriculum. It represents a significant step up in complexity, combining multiple programming concepts into a complete game application.

## 🎮 Game Features

- **Visual Feedback**: Progressive hangman ASCII art
- **Duplicate Prevention**: Prevents guessing the same letter multiple times
- **Life System**: 6 lives with visual counter
- **Real-time Updates**: Display updates after each guess
- **Win/Lose Conditions**: Clear end-game messages

## 📁 Project Structure

```
Day 7/
│
├── main.py             # Main game logic
├── hangman_words.py    # Word list module
├── hangman_art.py      # ASCII art module
└── README.md           # Project documentation
```

## 📝 Example Output

```
  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

Word to guess: _ _ _ _ _
****************************6/6 LIVES LEFT****************************
Guess a letter: a
Word to guess: _ a _ _ a
```

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
