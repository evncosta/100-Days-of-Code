# Snake Game - Part 1

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

The first part of the classic Snake game implementation, featuring snake movement, keyboard controls, and basic game mechanics. This project was completed as part of **Day 20** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 20: Build the Snake Game Part 1: Animation & Coordinates** in the 100 Days of Code curriculum. It focuses on the foundational mechanics of game development.

## 🎯 Project Overview

Snake Game Part 1 features:
- Snake object with segment-based movement
- Keyboard controls for directional movement
- Smooth animation with manual screen updates
- Game loop with controlled frame rate
- Collision detection with screen boundaries
- Object-oriented snake implementation

## 🚀 How It Works

1. The game initializes a 600×600 black screen
2. A snake object is created with initial segments
3. Players control the snake using arrow keys
4. The game loop updates the snake's position every 0.1 seconds
5. Manual screen updates create smooth animation
6. The snake moves continuously in the chosen direction

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Turtle Graphics** - For game visualization
- **Object-Oriented Programming** - Snake class implementation
- **Event Listeners** - Keyboard input handling
- **Time Module** - Frame rate control
- **Manual Screen Updates** - Smooth animation technique

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Game loop implementation and frame rate control
- Object-oriented game development
- Keyboard event handling in Turtle graphics
- Manual screen updates for smooth animation
- Coordinate-based movement systems
- Multi-segment object management

## 🎮 Controls

- **Up Arrow**: Move snake upward
- **Down Arrow**: Move snake downward  
- **Left Arrow**: Move snake left
- **Right Arrow**: Move snake right

## 📁 Project Structure

```
Day 20 - Snake Game Part 1/
│
├── main.py          # Main game loop and screen setup
├── snake.py         # Snake class implementation
└── README.md        # Project documentation
```

## 🔧 Technical Implementation

### Screen Setup
- 600×600 pixel game window
- Black background color
- Manual screen updates (`screen.tracer(0)`)
- Controlled frame rate (`time.sleep(0.1)`)

### Snake Movement
- Segmented body that follows the head
- Continuous movement in chosen direction
- Smooth animation through manual updates
- Direction change through keyboard input

## 📝 Example Output

![Snake Game Part 1 Demo](https://github.com/user-attachments/assets/a7003f77-9900-45e4-bd7c-a991e3c469ef)

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
