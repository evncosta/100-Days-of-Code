# Improved Password Manager

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

An enhanced password management application with JSON storage, search functionality, and improved data handling. This project was completed as part of **Day 30** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 30: Errors, Exceptions and JSON Data: Improving the Password Manager** in the 100 Days of Code curriculum. It builds upon the previous password manager with advanced error handling and data storage.

## 🎯 Project Overview

The Improved Password Manager features:
- **JSON Data Storage**: Structured, readable password storage format
- **Search Functionality**: Quick lookup of saved credentials by website
- **Enhanced Error Handling**: Graceful file operations and user feedback
- **Improved UI**: Additional search button and optimized layout
- **Data Validation**: Comprehensive input checking with user notifications
- **Robust File Operations**: Handles missing files and corrupted data

## 🚀 How It Works

1. **Data Entry**: Input website, email, and password (or generate one)
2. **Password Generation**: Creates secure passwords with character variety
3. **JSON Storage**: Saves data in structured JSON format with proper error handling
4. **Search Feature**: Retrieves saved credentials by website name
5. **Auto-Copy**: Generated passwords copied to clipboard automatically
6. **Input Validation**: Ensures all required fields are completed before saving

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **Tkinter** - GUI framework for interface creation
- **JSON Module** - Structured data storage and retrieval
- **Pyperclip** - Clipboard integration for password copying
- **Random Module** - Secure password generation algorithms
- **Exception Handling** - Robust error management for file operations

## 📋 Learning Objectives

This project helped reinforce understanding of:
- JSON data serialization and deserialization
- Advanced exception handling with try/except blocks
- File operations with proper error management
- Search functionality implementation in GUI applications
- Data validation and user feedback systems
- Professional application architecture with multiple features

## 🔐 Enhanced Security Features

- **JSON Encryption Ready**: Structured format allows for easy encryption addition
- **Search Security**: Only displays credentials after user confirmation
- **Input Validation**: Prevents saving incomplete or malformed data
- **File Integrity**: Handles corrupted or missing data files gracefully
- **Structured Storage**: Organized data format for better security management

## 💾 Data Storage Format

```json
{
    "Website0": {
        "email": "evncosta@email.com",
        "password": "rg+3Qa4sisEs5+"
    },
    "Website1": {
        "email": "evncosta@email.com",
        "password": "k7cv7Al+8Bu0*KC"
    },
    "Website2": {
        "email": "evncosta@email.com",
        "password": "S(65LUcIZPbp&j5"
    }
}
```

## 🔧 Technical Improvements

### Enhanced Error Handling
```python
try:
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    # Create new file if it doesn't exist
    with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)
else:
    # Update existing data
    data.update(new_data)
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)
```

### Search Functionality
```python
def find_password():
    website = website_entry.get()
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
```

## 🎨 User Interface Enhancements

- **Search Button**: Quick access to saved credentials
- **Improved Layout**: Better widget spacing and organization
- **User Feedback**: Clear error messages and confirmation dialogs
- **Streamlined Workflow**: Focus management and default values
- **Professional Appearance**: Consistent styling and branding

## 💼 Practical Benefits

- **Quick Retrieval**: Instant access to saved passwords with search feature
- **Data Integrity**: JSON format prevents corruption and allows easy backup
- **User Experience**: Clear feedback for all operations
- **Scalability**: Easy to add features like categories or password strength indicators
- **Maintainability**: Clean code structure for future enhancements

## 🎯 How to Use

1. **Save Credentials**: Enter website, email, and password → Click "Add"
2. **Generate Password**: Click "Generate Password" for secure auto-generation
3. **Search Passwords**: Enter website name → Click "Search" to retrieve credentials
4. **Auto-Copy**: Generated passwords are automatically copied to clipboard
5. **Data Management**: All data stored in `data.json` with proper formatting

## 🔄 Related Projects

This enhanced version builds upon the Day 29 Password Manager and is part of the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
