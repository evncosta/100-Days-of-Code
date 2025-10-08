# Snake Game - Part 2

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

The complete implementation of the classic Snake game featuring food collection, scoring, collision detection, and game over conditions. This project was completed as part of **Day 21** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 21: Build the Snake Game Part 2: Inheritance & List Slicing** in the 100 Days of Code curriculum. It completes the Snake game with advanced features.

## 🎯 Project Overview

Snake Game Part 2 builds upon the foundation from Part 1 and adds:
- Food generation and collection mechanics
- Score tracking and display system
- Wall collision detection
- Self-collision detection (tail biting)
- Game over conditions and messaging
- Snake growth when eating food

## 🚀 How It Works

1. The game initializes with a snake, food, and scoreboard
2. Players control the snake using arrow keys to collect food
3. Each food item collected increases the score and extends the snake
4. The game checks for collisions with walls and the snake's own body
5. Game over conditions trigger appropriate messages
6. The game runs at a controlled frame rate for smooth gameplay

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Turtle Graphics** - Game visualization and rendering
- **Object-Oriented Programming** - Multiple classes for game components
- **Collision Detection** - Distance-based collision checking
- **Random Module** - Food placement randomization
- **Event Handling** - Keyboard controls for snake movement

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Complete game loop implementation
- Collision detection algorithms
- Score tracking and display systems
- Object interaction and coordination
- Game state management
- Modular game architecture with multiple classes

## 🎮 Game Features

- **Food Collection**: Snake grows when eating food
- **Score System**: Points increase with each food collected
- **Wall Collisions**: Game ends if snake hits screen boundaries
- **Self Collisions**: Game ends if snake bites its own tail
- **Smooth Movement**: Controlled frame rate for consistent gameplay

## 📁 Project Structure

```
Day 21 - Snake Game Complete/
│
├── main.py          # Main game loop and coordination
├── snake.py         # Snake class with movement and growth
├── food.py          # Food class with random placement
├── scoreboard.py    # Score tracking and display
└── README.md        # Project documentation
```

## 🎯 Game Mechanics

### Food System
- Random placement within game boundaries
- Distance-based collision detection (<15 pixels)
- Automatic respawn after collection
- Score increment on successful collection

### Collision Detection
- **Wall Collision**: Check if head position exceeds ±280 coordinates
- **Self Collision**: Check distance between head and any body segment
- **Food Collision**: Check distance between head and food

### Scoring System
- Initial score: 0
- +1 point per food collected
- Real-time score display updates
- Game over message with final score

## 🕹️ How to Play

1. Use arrow keys to control snake direction
2. Collect food to increase score and grow longer
3. Avoid hitting walls or your own tail
4. Try to achieve the highest score possible

## 📝 Example Output

### Body collision
![Snake Game Part 2 Body Collision Demo](https://github.com/user-attachments/assets/d61e710a-17df-4cd1-92d7-4b4ef77926b8)

### Wall collision
![Snake Game Part 2 Wall Collision](https://github.com/user-attachments/assets/1fed6400-d403-4842-9ac8-d2d646495999)

## 🔄 Related Projects

This project completes the Snake game series and is part of the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
