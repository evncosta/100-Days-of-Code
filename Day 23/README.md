# Turtle Crossing Game

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A challenging road-crossing game where players navigate a turtle across increasingly busy traffic. This project was completed as part of **Day 23** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 23: Turtle Crossing Game** in the 100 Days of Code curriculum. It demonstrates side-scrolling game mechanics and dynamic difficulty.

## 🎯 Project Overview

The Turtle Crossing Game features:
- Player-controlled turtle movement
- Random car generation with varying speeds
- Progressive difficulty increase
- Score tracking system
- Collision detection mechanics
- Dynamic game environment

## 🚀 How It Works

1. The game creates a 600×600 road environment
2. Players control a turtle trying to cross from bottom to top
3. Cars randomly generate and move across the screen
4. Each successful crossing increases the score and game speed
5. Collisions with cars end the game
6. The challenge increases as cars move faster with each level

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Turtle Graphics** - Game visualization and rendering
- **Object-Oriented Programming** - Multiple classes for game components
- **Random Module** - Car generation and timing
- **Collision Detection** - Distance-based collision checking
- **Game State Management** - Progressive difficulty system

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Dynamic object generation and management
- Progressive difficulty systems
- Collision detection in game development
- Score tracking and level progression
- Game state transitions (win/lose conditions)
- Object coordination in real-time games

## 🎮 Controls

- **Up Arrow**: Move turtle forward (toward top of screen)

## 📁 Project Structure

```
Day 23 - Turtle Crossing Game/
│
├── main.py              # Main game loop and coordination
├── player.py            # Player turtle class
├── car_manager.py       # Car generation and management
├── scoreboard.py        # Score tracking and display
└── README.md            # Project documentation
```

## 🎯 Game Mechanics

### Player System
- Starts at bottom center of screen
- Moves upward with each key press
- Resets to starting position after successful crossing
- Collision detection with car objects

### Car System
- Random generation at right side of screen
- Movement from right to left at varying speeds
- Progressive speed increase with each level
- Multiple cars active simultaneously

### Scoring & Difficulty
- **Score Increase**: +1 point per successful crossing
- **Speed Increase**: Cars move faster after each level
- **Game Over**: Collision with any car ends the game
- **Win Condition**: Continuous progression with increasing challenge

## 🏁 Victory Conditions

- Successfully cross the road to reach y-coordinate > 310
- Each crossing increases score and difficulty
- No maximum score - game continues until collision

## 🚗 Car Behavior

- Random generation timing
- Varied movement speeds
- Continuous leftward movement
- Removal when off-screen
- Increasing speed with player progress

## 🎯 How to Play

1. Use Up Arrow to move turtle forward
2. Avoid colliding with moving cars
3. Reach the top to score points
4. Each successful crossing makes cars faster
5. Game ends when turtle hits a car

## 🔧 Technical Features

- **Dynamic Difficulty**: Speed increases with player success
- **Efficient Object Management**: Cars are removed when off-screen
- **Smooth Animation**: Controlled frame rate for consistent gameplay
- **Collision Precision**: 20-pixel distance threshold for collisions

## 📝 Example Output
![Turtle Crossing Game Demo](https://github.com/user-attachments/assets/dff041b3-a934-4607-b26b-732b3e01ddb1)

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
