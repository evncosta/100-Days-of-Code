# OOP Coffee Machine

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

An object-oriented coffee machine implementation that demonstrates proper software architecture with separated concerns and modular design. This project was completed as part of **Day 16** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎯 Project Overview

The OOP Coffee Machine features:
- Clean separation of concerns with dedicated classes
- Menu management with drink objects
- Resource tracking and validation
- Payment processing with change calculation
- Professional object-oriented architecture
- Maintainable and extensible code structure

## 🚀 How It Works

1. **Menu Class**: Handles drink definitions and retrieval
2. **CoffeeMaker Class**: Manages resources and drink preparation
3. **MoneyMachine Class**: Processes payments and handles transactions
4. **Main Program**: Coordinates all components for user interaction

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Object-Oriented Programming** - Classes and encapsulation
- **Modular Architecture** - Separated concerns across files
- **Method Chaining** - Clean, readable code flow
- **Error Handling** - Graceful failure handling
- **Type Hints** - Better code documentation

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Object-Oriented Programming principles
- Class design and responsibility separation
- Modular architecture and file organization
- Method encapsulation and interface design
- Code maintainability and extensibility
- Professional software development practices

## 🎓 Course Context

This project was part of **Day 16: Object Oriented Programming (OOP)** in the 100 Days of Code curriculum. It demonstrates the evolution from procedural to object-oriented programming.

## 📁 Project Structure

```
Day 16 - OOP Coffee Machine/
│
├── main.py              # Main program interface
├── menu.py              # Menu class and drink management
├── coffee_maker.py      # Resource handling and drink preparation
├── money_machine.py     # Payment processing functionality
└── README.md            # Project documentation
```

## 🏗️ Architecture Design

### Menu Class
- Stores drink definitions and prices
- Provides drink lookup functionality
- Manages available menu items

### CoffeeMaker Class
- Tracks resource levels (water, milk, coffee)
- Checks resource sufficiency for drinks
- Prepares drinks and deducts resources
- Generates resource reports

### MoneyMachine Class
- Processes coin payments
- Calculates change
- Tracks revenue
- Generates financial reports

## 📝 Example Output

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters? 10
How many dimes? 2
How many nickels? 1  
How many pennies? 3
Here is $0.08 in change.
Here is your latte ☕. Enjoy!

What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

What would you like? (espresso/latte/cappuccino): off
```

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
