# NATO Alphabet Project

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A phonetic alphabet converter that translates words into their corresponding NATO code words. This project was completed as part of **Day 26** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 26: List Comprehension and the NATO Alphabet** in the 100 Days of Code curriculum. It focuses on data manipulation with list comprehensions and dictionary operations.

## 🎯 Project Overview

The NATO Alphabet Project features:
- CSV data processing for phonetic alphabet
- Dictionary creation from external data
- List comprehension for efficient data transformation
- User input processing and validation
- Clean conversion of words to phonetic code words

## 🚀 How It Works

1. Loads NATO phonetic alphabet data from a CSV file
2. Creates a dictionary mapping letters to their code words
3. Accepts user input and converts it to uppercase
4. Processes each letter through list comprehension
5. Outputs the corresponding NATO code words for the input word

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Pandas** - Data processing and CSV operations
- **List Comprehensions** - Efficient data transformation
- **Dictionary Operations** - Key-value mapping and lookup
- **String Manipulation** - Text processing and conversion

## 📋 Learning Objectives

This project helped reinforce understanding of:
- List comprehensions for concise data processing
- Dictionary creation and manipulation with Pandas
- CSV file reading and data extraction
- String operations and character iteration
- Data validation and error handling
- Efficient code writing with Pythonic patterns

## 📁 Project Structure

```
Day 26 - NATO Alphabet/
│
├── main.py                      # Main conversion script
├── nato_phonetic_alphabet.csv   # NATO alphabet data file
└── README.md                    # Project documentation
```

## 📊 Data Structure

### nato_phonetic_alphabet.csv Format:
```csv
letter,code
A,Alfa
B,Bravo
C,Charlie
...
Z,Zulu
```

## 🔧 Technical Implementation

### Key Operations
- **Data Loading**: Using pandas to read CSV file
- **Dictionary Creation**: Converting DataFrame to dictionary
- **List Comprehension**: Efficient letter-to-code conversion
- **Input Processing**: Handling user input and validation

### Code Features
```python
# Dictionary creation from CSV data
nato_dict = df.set_index('letter')['code'].to_dict()

# List comprehension for conversion
word_to_code = [nato_dict[letter] for letter in word if letter in nato_dict]
```

## 💼 Practical Applications

- Military and aviation communication
- Radio transmission clarity
- Spelling assistance over phone
- Language learning tools
- Accessibility applications

## 🎯 How to Use

1. Run the program
2. Enter any word when prompted
3. View the phonetic code words for each letter
4. The program handles both uppercase and lowercase input

## 📝 Example Output

```
Write the word you'll like to know the phonetic code words for: hello
The phonetic code words for HELLO are: ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

## 🔧 Error Handling

- Automatically filters non-alphabetic characters
- Handles case insensitivity through uppercase conversion
- Only processes letters present in the NATO alphabet
- Gracefully handles empty or invalid input

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
