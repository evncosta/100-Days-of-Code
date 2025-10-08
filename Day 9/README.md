# Silent Auction

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A discreet auction system that collects bids privately and determines the highest bidder. This project was completed as part of **Day 9** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 9: Dictionaries, Nesting and the Secret Auction** in the 100 Days of Code curriculum. It demonstrates practical application of dictionaries for data storage and retrieval.

## 🎯 Project Overview

The Silent Auction program features:
- Private bid collection with screen clearing between bidders
- Bidder name and amount tracking using dictionaries
- Input validation for bid amounts and continuation prompts
- Automatic determination of the highest bidder
- Professional ASCII art interface
- Secure bid collection process

## 🚀 How It Works

1. The program displays an ASCII art logo
2. Collects the first bidder's name and bid amount
3. Asks if there are additional bidders
4. Clears the screen for privacy when new bidders participate
5. Continues collecting bids until no more bidders remain
6. Determines and displays the winner with the highest bid

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Dictionary Data Structure** - Storing bidder information as key-value pairs
- **Function Definition** - Reusable code for collecting bidder information
- **Input Validation** - Ensuring proper yes/no responses
- **Screen Clearing** - Maintaining bid privacy using print statements
- **Max Function with Key** - Finding the highest bid efficiently

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Dictionary operations and manipulation
- Function creation and parameter handling
- While loops with conditional exit
- User input validation and error handling
- Data privacy techniques in console applications
- Finding maximum values in dictionaries using custom keys

## 🔒 Privacy Features

- **Screen Clearing**: `print("\n" * 100)` creates privacy between bidders
- **Individual Input**: Each bidder enters their bid without seeing others' bids
- **Final Reveal**: Only the winning bid and bidder are displayed at the end

## 📁 Project Structure

```
Day 9/
│
├── main.py              # Main auction logic
├── art.py               # ASCII art module
└── README.md            # Project documentation
```

## 📝 Example Output

```
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\

What is your name? Alice
What is your bid? $150
Are there any other bidders? Type 'yes' or 'no'. yes

[Screen clears and shows logo again]

What is your name? Bob
What is your bid? $200
Are there any other bidders? Type 'yes' or 'no'. no

The winning bid is $200.0 from Bob!
```

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
