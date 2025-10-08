# Caesar Cipher

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A classic encryption and decryption tool that implements the Caesar cipher algorithm, one of the oldest and simplest encryption techniques. This project was completed as part of **Day 8** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 8: Function Parameters & Caesar Cipher** in the 100 Days of Code curriculum. It demonstrates practical application of function parameters and advanced string manipulation.

## 🎯 Project Overview

The Caesar Cipher program features:
- Bidirectional functionality (encode/decode)
- Customizable shift amount for encryption strength
- Input validation for operation type
- Preservation of non-alphabet characters
- ASCII art logo for visual appeal
- Clean, user-friendly interface

## 🚀 How It Works

1. The program displays an ASCII art logo
2. Users choose between encoding or decoding
3. Users input their message and a shift number
4. The program processes each character:
   - Alphabet characters are shifted by the specified amount
   - Non-alphabet characters (spaces, punctuation) remain unchanged
5. The encrypted or decrypted message is displayed

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Character Encoding** - Using ASCII values with `ord()` and `chr()`
- **Modulo Arithmetic** - Handling wrap-around from z to a
- **Input Validation** - Ensuring correct operation selection
- **String Manipulation** - Processing text character by character
- **Custom Art Module** - External ASCII art import

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Character encoding and ASCII values
- Mathematical operations for encryption algorithms
- Modulo arithmetic for circular data structures
- Function parameters and return values
- Input validation and error handling
- String iteration and manipulation techniques

## 🔐 Encryption Algorithm

The Caesar cipher works by:
- Converting each letter to its position in the alphabet (0-25)
- Applying a shift: 
  - **Encode**: `(position + shift) % 26`
  - **Decode**: `(position - shift) % 26`
- Converting back to a character
- Non-alphabet characters remain unchanged

## 📁 Project Structure

```
Day 8/
│
├── main.py             # Main cipher logic
├── art.py              # ASCII art module
└── README.md           # Project documentation
```

## 📝 Example Output

```
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world!
Type the shift number:
3
The encoded message is: khoor zruog!
```

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
