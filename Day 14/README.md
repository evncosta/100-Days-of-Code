# Higher or Lower Game

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

An engaging social media guessing game where players compare which celebrity has more Instagram followers. This project was completed as part of **Day 14** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 14: Higher Lower Game Project** in the 100 Days of Code curriculum. It demonstrates practical application of data manipulation and game design principles.

## 🎯 Project Overview

The Higher or Lower game features:
- Real celebrity data with names, descriptions, and follower counts
- Progressive gameplay with increasing difficulty
- Score tracking system
- Visual comparison interface with ASCII art
- Random selection of celebrities for comparison
- Input validation and error handling

## 🚀 How It Works

1. The game displays two celebrities with their descriptions and countries
2. Players guess which celebrity has more Instagram followers (A or B)
3. Correct guesses increase the score and the winning celebrity stays for the next round
4. A new random celebrity is selected for comparison
5. The game continues until the player guesses incorrectly
6. The final score is displayed at the end

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Random Module** - For random celebrity selection
- **External Data Files** - Celebrity information storage
- **ASCII Art** - Visual elements for game interface
- **Dictionary Manipulation** - Working with celebrity data
- **Game State Management** - Score tracking and flow control

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Working with external data files and imports
- Dictionary data structure manipulation
- Random selection and comparison operations
- Game loop implementation and state management
- User input validation and error handling
- Score tracking and progressive difficulty
- Modular code organization with multiple files

## 📊 Data Structure

The game uses a list of dictionaries with the following structure:
```python
{
    'name': 'Celebrity Name',
    'follower_count': 1000000,
    'description': 'Profession/Description', 
    'country': 'Country of Origin'
}
```

## 📁 Project Structure

```
Day 14/
│
├── main.py            # Main game logic
├── game_data.py       # Celebrity data module
├── art.py             # ASCII art module
└── README.md          # Project documentation
```

## 📝 Example Output

```
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Cristiano Ronaldo, a Footballer, from Portugal

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Ariana Grande, a Musician, from United States

Who has more followers? Type 'A' or 'B': A
You're right! Current score: 1
Compare A: Cristiano Ronaldo, a Footballer, from Portugal

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Dwayne Johnson, a Actor, from United States
```

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
