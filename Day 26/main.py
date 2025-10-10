# NATO Alphabet Project - Converts words to NATO code words
import pandas as pd

# Load NATO phonetic alphabet data from CSV
df = pd.read_csv("nato_phonetic_alphabet.csv")

# Create dictionary mapping letters to code words
nato_dict = df.set_index('letter')['code'].to_dict()

# Get user input and convert to uppercase
word = input("Write the word you'll like to know the phonetic code words for: ").upper()

# Convert each letter to its corresponding NATO code word
word_to_code = [nato_dict[letter] for letter in word if letter in nato_dict]

print(f"The phonetic code words for {word} are: {word_to_code}")
