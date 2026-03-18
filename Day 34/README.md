# Quizzler App

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate%2B-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A modern trivia quiz application that fetches questions from the Open Trivia Database API and presents them in an elegant GUI interface. This project was completed as part of **Day 34** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 34: API Practice - Creating a GUI Quiz App** in the 100 Days of Code curriculum. It combines API integration with GUI development to create a fully functional trivia game.

## 🎯 Project Overview

The Quizzler App features:
- **API Integration**: Fetches real trivia questions from Open Trivia Database
- **True/False Format**: Simple binary answer choices for streamlined gameplay
- **GUI Interface**: Professional purple-themed graphical interface
- **Score Tracking**: Real-time score display during gameplay
- **Visual Feedback**: Green/red color coding for correct/incorrect answers
- **HTML Entity Handling**: Automatically decodes HTML entities in questions
- **Question Counter**: Progress tracking through the quiz

## 🚀 How It Works

1. **Data Fetching**: API call to Open Trivia Database for 10 true/false questions
2. **Question Processing**: Converts API response into Question objects
3. **GUI Display**: Presents questions with True/False buttons
4. **User Interaction**: Players click True/False to answer
5. **Instant Feedback**: Canvas changes color (green/red) based on answer correctness
6. **Score Update**: Score increments for correct answers
7. **Auto-Advance**: Automatically moves to next question after 1-second delay
8. **Quiz Completion**: Shows end message when all questions answered

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Tkinter** - GUI framework for visual interface
- **Requests Library** - API calls to Open Trivia Database
- **HTML Module** - HTML entity unescaping for clean text display
- **Object-Oriented Programming** - Modular class-based architecture
- **Event Handling** - Button clicks and GUI interactions

## 📋 Learning Objectives

This project helped reinforce understanding of:
- API integration with parameters and response handling
- Object-oriented design for scalable applications
- GUI development with Tkinter and custom theming
- Event-driven programming patterns
- Data flow between API, logic, and interface layers
- User feedback mechanisms in GUI applications
- Modular code organization across multiple files

## 📁 Project Structure

```
Day 34 - Quizzler App/
│
├── main.py                 # Application entry point
├── data.py                 # API data fetching logic
├── question_model.py       # Question class definition
├── quiz_brain.py          # Quiz logic and scoring
├── ui.py                   # GUI interface
├── images/
│   ├── true.png           # True button image
│   └── false.png          # False button image
└── README.md              # Project documentation
```

## 🏗️ Architecture

### Data Layer (`data.py`)
- Fetches questions from Open Trivia Database API
- Configures parameters (10 questions, true/false format)
- Processes JSON response for main application

### Question Model (`question_model.py`)
- Simple data structure for question objects
- Stores question text and correct answer

### Quiz Logic (`quiz_brain.py`)
- Manages question progression and scoring
- Handles HTML entity decoding for clean display
- Validates user answers against correct answers

### GUI Interface (`ui.py`)
- Creates professional purple-themed interface
- Manages button interactions and visual feedback
- Displays scores and question text
- Handles quiz completion gracefully

## 🎨 Visual Design

- **Theme Color**: Purple (#5C3762) background
- **Question Canvas**: White with purple text
- **Feedback System**: Green (correct) / Red (incorrect) flashes
- **Button Design**: Custom true/false image buttons
- **Typography**: Arial font with italic styling for questions
- **Layout**: Clean grid-based organization

## 🔧 Technical Implementation

### API Configuration
```python
parameters = {
    "amount": 10,
    "type": "boolean",  # True/False questions only
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
```

### HTML Entity Cleaning
```python
import html
q_text = html.unescape(self.current_question.text)
```

### Visual Feedback System
```python
def give_feedback(self, is_right):
    if is_right:
        self.canvas.config(bg="green")
    else:
        self.canvas.config(bg="red")
    self.window.after(1000, self.get_next_question)
```

## 🎮 How to Play

1. **Launch App**: Run `main.py` to start the quiz
2. **Read Question**: Question appears on white canvas
3. **Choose Answer**: Click ✅ for True or ❌ for False
4. **Get Feedback**: Canvas flashes green (correct) or red (incorrect)
5. **Continue**: Next question appears automatically after 1 second
6. **Track Progress**: Score updates in top-right corner
7. **Finish**: End message shows after all 10 questions

## 📊 Game Features

- **10 Questions**: Fixed number per game session
- **Real-time Scoring**: Updates with each correct answer
- **Progress Tracking**: Question counter in display
- **Auto-Advance**: Seamless question transitions
- **Accessibility**: Large buttons and clear text
- **Visual Appeal**: Professional design with custom graphics

## 🔄 API Integration Notes

- **Source**: Open Trivia Database (opentdb.com)
- **Question Type**: True/False boolean questions
- **Quantity**: 10 questions per request
- **Format**: JSON response with HTML-encoded text
- **Reliability**: Free API with rate limiting considerations

## 🔄 Related Projects

This project builds upon concepts from earlier days (API integration, GUI development, OOP) and is part of the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
