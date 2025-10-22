# Password Manager

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

A secure password management application with automatic password generation and storage capabilities. This project was completed as part of **Day 29** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 29: Building a Password Manager GUI App with Tkinter** in the 100 Days of Code curriculum. It focuses on creating practical desktop applications with secure data handling.

## 🎯 Project Overview

The Password Manager features:
- Secure password generation with customizable complexity
- Local password storage in text file format
- Automatic clipboard copying for generated passwords
- Input validation and user confirmation dialogs
- Clean graphical user interface with logo
- Pre-filled email field for convenience

## 🚀 How It Works

1. **User Input**: Enter website, email/username, and password (or generate one)
2. **Password Generation**: Creates strong passwords with letters, numbers, and symbols
3. **Auto-Copy**: Generated passwords are automatically copied to clipboard
4. **Data Validation**: Ensures all required fields are completed
5. **Secure Storage**: Saves credentials to local text file with confirmation
6. **Form Reset**: Clears entries after successful save for next use

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Tkinter** - GUI framework for interface creation
- **Pyperclip** - Clipboard integration for password copying
- **Random Module** - Secure password generation
- **File I/O** - Local data storage management
- **Message Box** - User confirmation and warning dialogs

## 📋 Learning Objectives

This project helped reinforce understanding of:
- Advanced tkinter widget layout and grid management
- External library integration (pyperclip)
- File handling for persistent data storage
- User input validation and error handling
- Secure random password generation algorithms
- Professional GUI application structure

## 🔐 Security Features

- **Strong Password Generation**: 8-10 letters, 2-4 symbols, 2-4 numbers
- **Character Shuffling**: Randomizes password character order
- **Input Validation**: Prevents saving empty fields
- **User Confirmation**: Double-checks before saving sensitive data
- **Local Storage**: Passwords stored in user-controlled text file

## 🎨 User Interface

- **Logo Integration**: Professional branding with custom image
- **Intuitive Layout**: Clear form fields with proper labeling
- **Smart Defaults**: Pre-filled email field for convenience
- **Focus Management**: Automatic focus on website field at startup
- **Responsive Design**: Proper padding and widget spacing

## 🔧 Technical Implementation

### Password Generation Algorithm
```python
# Mix of letters, symbols, and numbers with random distribution
password_list = [choice(letters) for _ in range(randint(8, 10))]
password_list += [choice(symbols) for _ in range(randint(2, 4))]
password_list += [choice(numbers) for _ in range(randint(2, 4))]
shuffle(password_list)
```

### Data Storage Format
```
website | email | password
Website0 | evncosta@email.com | 07lB!$+8OMID+ax
Website1 | evncosta@email.com | P!OI)JL5(&SB7uoZ
```

## 💼 Practical Benefits

- **Password Security**: Generates strong, unique passwords for each service
- **Convenience**: Automatic clipboard copying saves time
- **Organization**: Centralized storage of all login credentials
- **Customization**: Easy to modify default email and storage location
- **Offline Access**: No internet connection required for operation

## 🎯 How to Use

1. Enter the website name in the first field
2. Enter your email/username (pre-filled for convenience)
3. Either type a password or click "Generate Password"
4. Generated passwords are automatically copied to clipboard
5. Click "Add" to save the entry after confirmation
6. Find saved passwords in the `data.txt` file

## ⚠️ Security Notes

- Store the `data.txt` file in a secure location
- Consider additional encryption for sensitive data
- Keep the application and data file backed up
- Be cautious when using on shared computers

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
