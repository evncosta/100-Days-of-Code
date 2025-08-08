# Task 1
# Printing
print("Hello World!")

# Task 2
# String manipulation
# Use \n to add another line of "Hello world!"
print("Hello world!\nHello world!\nHello world!")
# Add a space between the strings
print("Hello" + " " + "world!")

# Task 3
# Inputs
# Update the code to add an exclamation mark
print("Hello " + input("What is your name?") + "!")

# Task 4
# Variables
name = "Jack"
print(name)
name = "Angela"
print(name)
# Check the length of the user input
print(len(input("What is your name?")))
# Split everything into variables
username = input("What is your name?")
length = len(username)
print(length)

# Task 5
# Variable naming
name = "Angela"
length = len(name)
print(length)

# Task 6
# Band Name Generator Project
# 1. Create a greeting for your program / 2. Ask the user for the city that they grew up in and store it in a variable / 3. Ask the user for the name of a pet and store it in a variable / 4. Combine the name of their city and pet and show them their band name / 5. Make sure the input cursor shows on a new line
print("Welcome to the Band Name Generator!")
city = input("What is the name of the city you grew up in?\n")

pet = input("Suggest a name for a pet!\n")
print("Your band name could be " + city + " " + pet)