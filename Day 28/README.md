# Miles to Kilometers Converter

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A graphical user interface application that converts miles to kilometers using tkinter. This project was completed as part of **Day 27** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 27: Tkinter, Args, Kwargs and Creating GUI Programs** in the 100 Days of Code curriculum. It introduces GUI development with Python's built-in tkinter library.

## 🎯 Project Overview

The Miles to Kilometers Converter features:
- Clean and intuitive graphical user interface
- Real-time conversion with button click
- Precise mathematical calculation (1 mile = 1.60934 km)
- Formatted output with two decimal places
- Responsive layout with proper widget spacing

## 🚀 How It Works

1. Launches a GUI window with input field and labels
2. User enters miles value in the input field
3. Clicking "Calculate" button triggers the conversion
4. Conversion formula: `kilometers = miles × 1.60934`
5. Result displays in kilometers with two decimal places
6. Window remains open for multiple conversions

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Tkinter** - GUI framework for interface creation
- **Grid Layout** - Widget positioning system
- **Event Handling** - Button click responses
- **String Formatting** - Precision control for results

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Tkinter widget creation and configuration
- Grid-based layout management
- Event-driven programming with command binding
- GUI application structure and mainloop
- Input validation and data conversion
- User interface design principles

## 🖥️ GUI Components

- **Entry Widget**: Input field for miles value
- **Label Widgets**: Static text and dynamic result display
- **Button Widget**: Calculate trigger with command binding
- **Main Window**: Container with title and padding

## 🔧 Technical Implementation

### Key Features
```python
# Conversion function with precision formatting
kilometers = miles * 1.60934
kilometer_result_label.config(text=f"{kilometers:.2f}")

# Grid layout for precise widget positioning
miles_input.grid(column=1, row=0)
calculate_button.grid(column=1, row=2)
```

### Layout Structure
```
[Input Field] "Miles"
"is equal to" [Result] "Km"
      [Calculate Button]
```

## 💼 Practical Applications

- Distance conversion for travel planning
- Educational tool for unit conversion
- Fitness tracking for runners and cyclists
- International measurement standardization
- Quick reference utility application

## 🎯 How to Use

1. Run the program to open the converter window
2. Enter the number of miles in the input field
3. Click the "Calculate" button
4. View the equivalent kilometers in the result field
5. Perform additional conversions by entering new values

## 📊 Conversion Accuracy

- Uses precise conversion factor: 1 mile = 1.60934 kilometers
- Results formatted to two decimal places
- Handles both integer and decimal inputs
- Automatic float conversion for calculation

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
