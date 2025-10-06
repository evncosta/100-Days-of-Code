# Pong Game

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A classic two-player Pong game implementation featuring paddle controls, ball physics, and real-time scoring. This project was completed as part of **Day 22** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎯 Project Overview

The Pong Game features:
- Two-player paddle controls with keyboard input
- Realistic ball physics with bounce mechanics
- Dynamic scoring system for both players
- Collision detection with walls and paddles
- Adjustable game speed and ball velocity
- Professional scoreboard display

## 🚀 How It Works

1. The game initializes an 800×600 black playing field
2. Two paddles are positioned on left and right sides
3. Players control paddles using keyboard keys
4. The ball moves automatically with realistic physics
5. Collisions with paddles cause directional changes
6. Scoring occurs when a player misses the ball
7. The game runs continuously until manually stopped

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Turtle Graphics** - Game visualization and rendering
- **Object-Oriented Programming** - Multiple classes for game components
- **Physics Simulation** - Ball movement and bounce mechanics
- **Collision Detection** - Distance-based and coordinate-based detection
- **Event Handling** - Keyboard controls for both players

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Multi-object game coordination
- Physics simulation in game development
- Real-time collision detection
- Two-player game mechanics
- Score tracking and display systems
- Game state management and object interaction

## 🎓 Course Context

This project was part of **Day 22: Pong Game** in the 100 Days of Code curriculum. It demonstrates classic arcade game development principles.

## 🎮 Controls

### Player 1 (Left Paddle)
- **W Key**: Move paddle up
- **S Key**: Move paddle down

### Player 2 (Right Paddle)  
- **Up Arrow**: Move paddle up
- **Down Arrow**: Move paddle down

## 📁 Project Structure

```
Day 22 - Pong Game/
│
├── main.py          # Main game loop and coordination
├── paddle.py        # Paddle class with movement logic
├── ball.py          # Ball class with physics and movement
├── scoreboard.py    # Score tracking and display
└── README.md        # Project documentation
```

## 🎯 Game Mechanics

### Ball Physics
- Continuous movement in x and y directions
- Wall bounce when hitting top/bottom boundaries
- Paddle bounce with directional change
- Speed adjustment on paddle collisions
- Position reset after scoring

### Collision System
- **Wall Collision**: Ball bounces when y-coordinate exceeds ±280
- **Paddle Collision**: Ball bounces when within 50 pixels of paddle and appropriate x-position
- **Scoring**: Ball reset when x-coordinate exceeds ±380

### Scoring System
- Left player scores when ball passes right paddle
- Right player scores when ball passes left paddle  
- Real-time score display updates
- Ball resets to center after each point

## 🕹️ How to Play

1. Player 1 uses W/S keys to control left paddle
2. Player 2 uses Up/Down arrows to control right paddle
3. Hit the ball with your paddle to prevent opponent from scoring
4. Score points by making the ball pass your opponent's paddle
5. The game continues indefinitely with score tracking

## 📝 Example Output
![Pong Game Demo](https://github.com/user-attachments/assets/cb790db8-3173-47f0-b275-ac111bbfc4a6)

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
