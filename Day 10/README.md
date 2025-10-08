# Calculator

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A fully functional calculator application that performs basic arithmetic operations with a continuous calculation feature. This project was completed as part of **Day 10** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 10: Functions with Outputs** in the 100 Days of Code curriculum. It demonstrates practical application of functions that return values and more complex program flow control.

## 🎯 Project Overview

The Calculator program features:
- Four basic arithmetic operations: addition, subtraction, multiplication, and division
- Continuous calculation mode using previous results
- Error handling for division by zero
- Input validation for operation selection
- Professional ASCII art interface
- Recursive function design for restart capability

## 🚀 How It Works

1. The program displays an ASCII art logo
2. Users input the first number
3. Users select an operation from available options
4. Users input the second number
5. The calculation is performed and displayed
6. Users can continue calculating with the result or start fresh
7. Division by zero errors are handled gracefully

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Function Dictionary** - Mapping operators to corresponding functions
- **Error Handling** - Division by zero prevention
- **Input Validation** - Ensuring valid operation selection
- **Recursive Functions** - Calculator restart capability
- **Modular Design** - Separate functions for each operation

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Function definitions and return values
- Dictionary mapping for operation selection
- While loops for continuous operation
- Error handling and input validation
- Recursive function calls
- Modular program design
- User interface design for console applications

## 🔢 Operations Supported

- **Addition (+)**: `n1 + n2`
- **Subtraction (-)**: `n1 - n2`
- **Multiplication (*)**: `n1 * n2`
- **Division (/)**: `n1 / n2` (with zero division protection)

## 📁 Project Structure

```
Day 10/
│
├── main.py          # Main calculator logic
├── art.py           # ASCII art module
└── README.md        # Project documentation
```

## 📝 Example Output

```
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' |
|_____________________|

What's the first number? 10
+ 
- 
* 
/ 

Pick an operation: *
What's the next number? 5
10.0 * 5.0 = 50.0
Type 'y' to continue calculating with 50.0, or type 'n' to start a new calculation: y
+ 
- 
* 
/ 

Pick an operation: /
What's the next number? 2
50.0 / 2.0 = 25.0
Type 'y' to continue calculating with 25.0, or type 'n' to start a new calculation: n
```

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
