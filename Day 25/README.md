# U.S. States Game

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

An interactive geography quiz that tests knowledge of U.S. states using turtle graphics and data processing. This project was completed as part of **Day 25** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 25: Working with CSV Data and the Pandas Library** in the 100 Days of Code curriculum. It combines data processing with interactive visualization.

## 🎯 Project Overview

The U.S. States Game features:
- Interactive map-based quiz interface
- Real-time score tracking and progress display
- State name placement on correct answers
- CSV data processing for state information
- Learning mode with export of unguessed states
- Visual feedback with turtle graphics

## 🚀 How It Works

1. Displays a blank U.S. map using turtle graphics
2. Prompts users to guess state names through text input
3. Validates answers against state database
4. Displays correct state names on their map locations
5. Tracks progress and provides real-time feedback
6. Generates learning file with missed states upon exit

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Turtle Graphics** - Interactive map visualization
- **Pandas** - Data processing and CSV operations
- **CSV Data Files** - State coordinates and names
- **Image Processing** - Map background integration
- **User Input Handling** - Interactive quiz interface

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Data processing with Pandas library
- CSV file operations and data manipulation
- Interactive graphics with turtle
- Game state management and progress tracking
- User input validation and processing
- File generation for learning purposes

## 🗺️ Game Features

- **Interactive Map**: Clickable interface with visual feedback
- **Progress Tracking**: Real-time score display (X/50 states)
- **State Placement**: Correct answers displayed on map
- **Learning Mode**: Export unguessed states to CSV for study
- **Case Insensitive**: Handles various input formats
- **Visual Learning**: Spatial recognition of state locations

## 📁 Project Structure

```
Day 25 - U.S. States Game/
│
├── main.py              # Main game logic and interface
├── 50_states.csv        # State data with coordinates
├── blank_states_img.gif # U.S. map background image
├── states_to_learn.csv  # Generated learning file (output)
└── README.md            # Project documentation
```

## 🎮 How to Play

1. Run the program to open the U.S. map
2. Enter state names when prompted
3. Correct answers will appear on the map
4. Continue until all 50 states are guessed
5. Type "Exit" to end game and generate learning file
6. Study the generated `states_to_learn.csv` file

## 📊 Data Structure

### 50_states.csv Format:
```csv
state,x,y
Alabama,139,-77
Alaska,-204,-170
Arizona,-203,-40
Arkansas,57,-53
...
Wyoming,-134,90
```

## 🔧 Technical Implementation

### Key Features
- **Map Integration**: GIF background with coordinate system
- **Data Validation**: Checks against state database
- **Progress Tracking**: Dynamic title updates
- **Learning Export**: Generates personalized study guide
- **Coordinate Placement**: Precise state name positioning

### Exit Functionality
```python
if answer_state == "Exit":
    missing_states = [state for state in all_states if state not in guessed_states]
    pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
```

## 🎯 Educational Value

- Geography knowledge reinforcement
- Spatial memory development
- State location recognition
- Self-paced learning approach
- Progress-based motivation

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
