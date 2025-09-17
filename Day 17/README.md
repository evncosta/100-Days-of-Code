# Quiz Game

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

An interactive quiz application that pulls questions from external data sources and tracks user performance. This project was completed as part of **Day 17** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎯 Project Overview

The Quiz Game features:
- External question data storage for easy updates
- Object-oriented design with separate Question and QuizBrain classes
- Randomized question order for varied gameplay
- Real-time score tracking
- Progress indication (current question/total questions)
- Clean, modular architecture

## 🚀 How It Works

1. Questions are loaded from external data files
2. Questions are shuffled for random order
3. Users answer True/False questions one by one
4. The system validates answers and updates scores
5. Progress and scores are displayed throughout the quiz
6. Final results are shown upon completion

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Object-Oriented Programming** - Custom Question and QuizBrain classes
- **External Data Files** - Separating data from logic
- **Random Module** - Question randomization
- **Modular Architecture** - Multiple files for organization
- **Class Methods** - Encapsulated quiz functionality

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Object-Oriented Programming principles
- Class creation and instantiation
- Working with external data sources
- Modular program architecture
- Randomization techniques
- User input validation
- Score tracking and progress reporting

## 🎓 Course Context

This project was part of **Day 17: The Quiz Project & the Benefits of OOP** in the 100 Days of Code curriculum. It demonstrates the practical benefits of object-oriented design for creating maintainable, scalable applications.

## 📁 Project Structure

```
Day 17/
│
├── main.py              # Main program entry point
├── question_model.py    # Question class definition
├── quiz_brain.py        # QuizBrain class with game logic
├── data.py              # Question data storage
└── README.md            # Project documentation
```

## 🏗️ Architecture

- **Question Class**: Represents individual questions with text and answer
- **QuizBrain Class**: Handles quiz logic, scoring, and question management  
- **Data Module**: Stores question data separately from logic
- **Main Program**: Coordinates the overall quiz flow

## 📝 Example Output

```
Q.1: The HTML5 standard was published in 2014. (True/False)? True
You got it right!
Your current score is: 1/1

Q.2: The programming language "Python" is based off a modified version of "JavaScript". (True/False)? False
You got it right!
Your current score is: 2/2

Q.3: The Windows 7 operating system has six main editions. (True/False)? True
That's wrong.
Your current score is: 2/3

You've completed the quiz.
Your final score was: 2/3
```

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
