# Coffee Machine

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A comprehensive coffee machine simulator that handles drink orders, payment processing, and resource management. This project was completed as part of **Day 15** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎯 Project Overview

The Coffee Machine program features:
- Three drink options: Espresso, Latte, and Cappuccino
- Real-time resource tracking (water, milk, coffee)
- Coin-based payment system with change calculation
- Administrative reporting functionality
- Resource sufficiency checking
- Profit tracking system

## 🚀 How It Works

1. Users select from available drinks or special commands
2. The system checks if sufficient resources are available
3. Users insert coins (quarters, dimes, nickels, pennies)
4. Payment is verified and change is calculated if needed
5. Drinks are prepared by deducting required ingredients
6. Profits are tracked and resources are updated in real-time

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Dictionary Data Structures** - Menu and resource storage
- **Mathematical Operations** - Currency calculations
- **Function Definitions** - Modular resource checking and drink preparation
- **Input Validation** - Handling invalid user inputs
- **Resource Management** - Tracking and deducting ingredients

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Complex data structures with nested dictionaries
- Resource management and state tracking
- Monetary calculations and change handling
- Function modularization and separation of concerns
- User input validation and error handling
- Real-world application simulation

## 🎓 Course Context

This project was part of **Day 15: Local Development Environment Setup & the Coffee Machine** in the 100 Days of Code curriculum. It marks the transition to intermediate-level projects and local development.

## ☕ Drink Specifications

| Drink | Water | Milk | Coffee | Cost |
|-------|-------|------|--------|------|
| Espresso | 50ml | 0ml | 18g | $1.50 |
| Latte | 200ml | 150ml | 24g | $2.50 |
| Cappuccino | 250ml | 100ml | 24g | $3.00 |

## 💰 Coin Values

- Quarter = $0.25
- Dime = $0.10  
- Nickel = $0.05
- Penny = $0.01

## 🎮 Special Commands

- **report**: Shows current resource levels and money
- **off**: Turns off the coffee machine

## 📝 Example Output

```
What would you like? (espresso/latte/cappuccino): latte
Please insert your coins.
How many quarters? 4
How many dimes? 2  
How many nickels? 1
How many pennies? 3
Here is $0.08 in change!
Here is your latte! Enjoy! ☕

What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
