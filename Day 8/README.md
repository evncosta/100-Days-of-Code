# Caesar Cipher

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A classic encryption and decryption tool that implements the Caesar cipher algorithm, one of the oldest and simplest encryption techniques. This project was completed as part of **Day 8** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

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

## 🎓 Course Context

This project was part of **Day 8: Function Parameters & Caesar Cipher** in the 100 Days of Code curriculum. It demonstrates practical application of function parameters and advanced string manipulation.

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
  ___   ___  ___  ___   ___  ______ _____ ______   ___   _   _ _____ _   _ _____ 
 / _ \ / _ \ |  \/  |  / _ \ | ___ \_   _|| ___ \ / _ \ | \ | |  ___| \ | |  __ \
/ /_\ / /_\ \| .  . | / /_\ \| |_/ / | |  | |_/ // /_\ \|  \| | |__ |  \| | |  \/
|  _  |  _  || |\/| | |  _  ||    /  | |  | ___ \|  _  || . ` |  __|| . ` | | __ 
| | | | | | || |  | | | | | || |\ \ _| |_ | |_/ /| | | || |\  | |___| |\  | |_\ \
\_| |_/\_| |_/\_|  |_/ \_| |_/\_| \_|\___/ \____/ \_| |_/\_| \_\____/\_| \_/\____/
                                                                                  
                                                                                  

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
