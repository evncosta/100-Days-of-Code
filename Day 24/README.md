# Mail Merge Project

![Python](https://img.shields.io/badge/Python-3-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

An automated mail merge system that generates personalized letters from a template and name list. This project was completed as part of **Day 24** of the "100 Days of Code: The Complete Python Pro Bootcamp" course.

## 🎓 Course Context

This project was part of **Day 24: Files, Directories and Paths** in the 100 Days of Code curriculum. It focuses on practical file handling and automation.

## 🎯 Project Overview

The Mail Merge Project features:
- Template-based letter generation
- Batch processing of multiple recipients
- File input/output operations
- String manipulation and replacement
- Organized file structure management
- Automated personalized document creation

## 🚀 How It Works

1. Reads a list of names from an input file
2. Loads a letter template with placeholder text
3. Replaces the `[name]` placeholder with each person's name
4. Generates individual personalized letters for each recipient
5. Saves each letter as a separate file in the output directory

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **File I/O Operations** - Reading and writing text files
- **String Manipulation** - Template replacement and cleaning
- **Batch Processing** - Handling multiple data entries
- **Directory Management** - Organized file structure

## 📋 Learning Objectives

This project helped reinforce understanding of:
- File input/output operations in Python
- String manipulation and replacement methods
- Batch processing techniques
- Working with file paths and directories
- Data cleaning (removing newline characters)
- Automated document generation

## 📁 Project Structure

```
Day 24 - Mail Merge/
│
├── main.py                      # Main mail merge script
├── Input/
│   ├── Names/
│   │   └── invited_names.txt    # List of recipient names
│   └── Letters/
│       └── starting_letter.txt  # Letter template with [name] placeholder
├── Output/
│   └── ReadyToSend/             # Generated personalized letters
└── README.md                    # Project documentation
```

## 📝 File Formats

### Input Names File (`invited_names.txt`)
```
Aang
Zuko
Appa
Katara
Sokka
Momo
Uncle Iroh
Toph
```

### Letter Template (`starting_letter.txt`)
```
Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Angela
```

### Generated Output
- `letter_for_Aang.txt`
- `letter_for_Zuko.txt`
- `letter_for_Appa.txt`
- `letter_for_Katara.txt`
- `letter_for_Sokka.txt`
- `letter_for_Momo.txt`
- `letter_for_Uncle Iroh.txt`
- `letter_for_Toph.txt`

## 🔧 Technical Implementation

### Key Operations
- **File Reading**: Reading names and template from text files
- **String Cleaning**: Removing newline characters with `strip()`
- **Template Replacement**: Using `replace()` to insert names
- **File Writing**: Creating individual output files for each recipient

### Code Features
```python
# Batch processing with file operations
for name in guest_list:
    clean_name = name.strip()
    personalized_letter = letter_template.replace("[name]", clean_name)
```

## 💼 Practical Applications

- Event invitations
- Marketing campaigns
- Personalized notifications
- Mass communication
- Automated document generation

## 🎯 How to Use

1. Prepare your name list in `Input/Names/invited_names.txt`
2. Create your letter template in `Input/Letters/starting_letter.txt` with `[name]` placeholder
3. Run the script to generate personalized letters
4. Find all generated letters in `Output/ReadyToSend/` directory

## 🔄 Related Projects

This project is part of a series of exercises in the 100 Days of Code course. Check out my progress on other days in the main repository.

---

*Part of the #100DaysOfCode challenge - [View Full Progress](https://github.com/evncosta/100-Days-of-Code)*
