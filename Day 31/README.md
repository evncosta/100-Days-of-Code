# Flash Card App

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A language learning application that uses spaced repetition and flash cards to help memorize vocabulary. This project was completed as part of **Day 31** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 31: Flash Card App Capstone Project** in the 100 Days of Code curriculum. It combines GUI development, file handling, and educational technology principles.

## 🎯 Project Overview

The Flash Card App features:
- **Spaced Repetition**: Automatically removes known words from rotation
- **Bilingual Flashcards**: French to English vocabulary training
- **Auto-Flip Cards**: Automatic reveal of translations after 3 seconds
- **Progress Tracking**: Saves learning progress to CSV file
- **Visual Design**: Professional card-based interface with custom graphics
- **Adaptive Learning**: Focuses on words that need more practice

## 🚀 How It Works

1. **Card Display**: Shows French word on card front with auto-flip timer
2. **Translation Reveal**: Flips after 3 seconds to show English translation
3. **User Response**: 
   - ✅ Right Button: Word is known (removed from learning deck)
   - ❌ Wrong Button: Word needs more practice (stays in rotation)
4. **Progress Saving**: Updates learning file with remaining words
5. **Continuous Learning**: Cycles through vocabulary with spaced repetition

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Tkinter** - GUI framework for card interface
- **Pandas** - Data processing and CSV file management
- **Random Module** - Randomized card presentation
- **File I/O** - Progress tracking and data persistence
- **Timer Functions** - Automatic card flipping with `after()`

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Spaced repetition learning algorithms
- Advanced tkinter canvas operations
- Dynamic image and text updates
- File-based progress tracking systems
- User interaction patterns for educational apps
- Error handling for file operations
- State management in learning applications

## 🎨 Visual Design

- **Color Scheme**: Professional blue background (#B1DDC6)
- **Card Design**: Front (white) for questions, Back (green) for answers
- **Typography**: Clear hierarchy with different font sizes and styles
- **Icons**: Intuitive right/wrong button graphics
- **Layout**: Clean, focused interface minimizing distractions

## 📁 Project Structure

```
Day 31 - Flash Card App/
│
├── main.py                 # Main application logic
├── data/
│   ├── french_words.csv    # Original vocabulary database
│   └── words_to_learn.csv  # Progress tracking file (generated)
├── images/
│   ├── card_front.png      # Flash card front design
│   ├── card_back.png       # Flash card back design  
│   ├── right.png           ✅ Known word button
│   └── wrong.png           ❌ Unknown word button
└── README.md               # Project documentation
```

## 🔧 Technical Implementation

### Spaced Repetition System
```python
def is_known():
    data_dict.remove(current_card)  # Remove mastered word
    learn_data = pandas.DataFrame(data_dict)
    learn_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()  # Continue with remaining words
```

### Auto-Flip Timer
```python
flip_timer = window.after(3000, flip_card)  # Flip after 3 seconds
window.after_cancel(flip_timer)  # Reset timer for new card
```

### Data Persistence
```python
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    # Fallback to original word list
    data = pandas.read_csv("./data/french_words.csv")
```

## 💡 Educational Benefits

- **Spaced Repetition**: Scientifically proven learning technique
- **Active Recall**: Forces memory retrieval rather than passive review
- **Visual Memory**: Combines text with visual cues for better retention
- **Self-Paced Learning**: Users control their learning speed
- **Progress Tracking**: Visual feedback on learning accomplishments

## 🎯 How to Use

1. **Start Learning**: App shows French word on card front
2. **Think of Translation**: Try to recall the English meaning
3. **Auto-Reveal**: Card flips after 3 seconds showing the answer
4. **Self-Assess**:
   - Click ✅ if you knew the word (removes from deck)
   - Click ❌ if you need more practice (keeps in rotation)
5. **Continue**: App automatically shows next word in sequence
6. **Track Progress**: Watch as the deck shrinks with mastered words

## 🔄 Learning Workflow

```
French Word Display → User Recall Attempt → 
Auto Translation Reveal → Self Assessment → 
Progress Update → Next Word
```

## 🌍 Language Support

Currently configured for French-English learning, but easily adaptable for:
- Any language pair
- Different subject matter (history, science, etc.)
- Custom vocabulary sets
- Professional terminology

## 🔄 Related Projects

This capstone project demonstrates comprehensive application development skills and is part of the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
