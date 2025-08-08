# Task 1
# Data Types
# Subscripting
print("Hello"[0])
# Strings
print("123" + "456")
# Integer = Whole number
print(123 + 456)
# Large Integers
print(123_456_789)
# Floating Point Number
print(3.14)
# Boolean
print(True)
print(False)

# Task 2
#TypeError, Checking and Conversion
# Fix the len() function: len(12345)
len("Hello")
# Write out 4 type checks to print all 4 data types
print(type("Hello"))
print(type(12345))
print(type(3.14))
print(type(True))
# Make this line of code run without errors: print("Number of letters in your name: " + len(input("Enter your name")))
print("Number of letters in your name: " + str(len(input("Enter your name\n"))))

# Task 3
# Mathematical Operators
print(123 + 456)
print (7 - 2)
print(3 * 2)
print(6 / 3)
print(6 // 3)
print(2 ** 2)
# Change the code so it outputs 3: print(3 * 3 + 3 / 3 - 3)
print(3 * 3 * 3 / 3 / 3)

# Task 4
# Number Manipulation
bmi = 84 / 1.65 ** 2
print(bmi)
# Flooring a number
print(int(bmi))
# Rounding a number
print(round(bmi))
print(round(bmi, 2))
print(round(3.738492))
print(round(3.14159))
# Assignment Operators
score = 0
score += 1 # User scores a point
score -= 1 # User looses a point
score *= 2 # User multiplies his score by 2
score /= 2 # User divides his score by 2
# f-strings
score = 0
height = 1.8
is_winning = True
print(f"Your score is {score}, your height is {height} and your winning is {is_winning}.")