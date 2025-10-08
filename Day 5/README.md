# Password Generator

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A secure password generator that creates customizable passwords with varying complexity levels. This project was completed as part of **Day 5** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 5: Python Loops** in the 100 Days of Code curriculum. It demonstrates practical application of loops for repetitive tasks and character generation.

## 🎯 Project Overview

The Password Generator offers:
- Customizable password composition (letters, symbols, numbers)
- Two security levels: Easy (ordered) and Hard (randomized)
- Secure random character selection
- User-friendly interface for specifying password requirements
- Professional-grade password generation techniques

## 🚀 How It Works

1. The program welcomes the user and explains its purpose
2. Users specify how many letters, symbols, and numbers they want in their password
3. The generator creates two versions:
   - **Easy Level**: Characters in predictable order (letters → symbols → numbers)
   - **Hard Level**: Characters randomly shuffled for maximum security
4. Both passwords are displayed for the user

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Random Module** - For secure random character selection and shuffling
- **List Operations** - Character set management and manipulation
- **String Manipulation** - Building and transforming password strings
- **Loops** - For generating multiple characters efficiently

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Working with lists and random selection
- String concatenation and manipulation
- Implementing different security levels
- User input handling and validation
- List shuffling and joining operations
- Creating practical, real-world applications

## 🔒 Security Features

- **Character Diversity**: Uses letters (uppercase and lowercase), numbers, and symbols
- **Random Selection**: Utilizes `random.choice()` for unpredictable character selection
- **Password Shuffling**: Implements `random.shuffle()` for enhanced security in hard mode
- **Customizable Length**: Users control the exact composition of their password

## 📝 Example Output

```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
8
How many symbols would you like?
2
How many numbers would you like?
2
Your password with security level EASY is: abcdefgh!$12
Your password with security level HARD is: h!2af$gb1ec
```

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
