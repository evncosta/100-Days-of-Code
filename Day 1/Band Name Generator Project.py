# Band Name Generator
# This program generates a band name by combining the user's city and pet name

# Display a welcome message to the user
print("Welcome to the Band Name Generator!")

# Prompt user for the city they grew up in
# The newline character (\n) moves the cursor to the next line for cleaner input
city = input("What is the name of the city you grew up in?\n")

# Prompt user for a suggested pet name
pet = input("Suggest a name for a pet!\n")

# Combine the city and pet name with a space to create the band name
# Using string concatenation to format the final output
print("Your band name could be " + city + " " + pet)
