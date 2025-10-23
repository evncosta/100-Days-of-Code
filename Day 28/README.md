# Pomodoro GUI Application

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A productivity timer application that implements the Pomodoro Technique with automatic work and break intervals. This project was completed as part of **Day 28** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 28: Tkinter, Dynamic Typing and the Pomodoro GUI Application** in the 100 Days of Code curriculum. It combines GUI development with timer logic and state management.

## 🎯 Project Overview

The Pomodoro Application features:
- Automated work/break session sequencing
- Visual timer with tomato-themed interface
- Progress tracking with checkmark system
- Color-coded session indicators
- Start/Reset controls for session management
- Automatic session progression

## 🚀 How It Works

1. **Work Session**: 25 minutes of focused work time
2. **Short Break**: 5 minutes after each work session
3. **Long Break**: 20 minutes after 4 work sessions
4. **Visual Feedback**: Color changes and checkmarks track progress
5. **Automatic Cycling**: Sessions transition automatically upon completion

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Tkinter** - GUI framework for interface creation
- **Canvas Widget** - Custom graphics and image display
- **Time Management** - Countdown logic with `after()` method
- **State Management** - Session tracking and progression
- **Color Scheme** - Custom palette for visual hierarchy

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Advanced tkinter widget usage (Canvas, Labels, Buttons)
- Timer implementation with `window.after()`
- State management in GUI applications
- Dynamic UI updates during runtime
- Image integration in tkinter applications
- Event-driven programming patterns

## ⏱️ Pomodoro Technique

The application follows the proven productivity method:
- **25 minutes** of focused work
- **5 minute** short break
- Repeat 4 times, then take a **20 minute** long break
- Visual checkmarks track completed work sessions

## 🎨 Visual Design

- **Color Scheme**: 
  - Green: Work sessions
  - Pink: Short breaks  
  - Red: Long breaks
  - Yellow: Background
- **Typography**: Courier font for retro terminal aesthetic
- **Iconography**: Classic tomato image representing the technique

## 🔧 Technical Implementation

### Key Features
```python
# Automatic session progression
if reps % 8 == 0:  # Long break every 4 work sessions
    count_down(long_break_sec)
elif reps % 2 == 0:  # Short break after each work session
    count_down(short_break_sec)
else:  # Work session
    count_down(work_sec)
```

### Timer Logic
- Uses `window.after()` for non-blocking countdown
- Mathematical floor division for minute calculation
- Zero-padding for seconds display
- Automatic callback chaining for continuous operation

## 💼 Productivity Benefits

- **Time Management**: Structured work/break intervals
- **Focus Enhancement**: Minimizes distractions during work sessions
- **Prevention of Burnout**: Regular breaks maintain mental freshness
- **Progress Tracking**: Visual feedback motivates continued effort
- **Work-Life Balance**: Encourages regular rest periods

## 🎯 How to Use

1. Click "Start" to begin the first 25-minute work session
2. Work focused until the timer completes
3. Take the automatic 5-minute break
4. Continue through the cycle (work → break → work → break...)
5. After 4 work sessions, enjoy a 20-minute long break
6. Use "Reset" to stop and clear the current session

## 📊 Session Pattern

```
Work (25m) → Break (5m) → Work (25m) → Break (5m) → 
Work (25m) → Break (5m) → Work (25m) → Break (20m) → Repeat
```

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
