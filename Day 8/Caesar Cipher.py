# Caesar Cipher - Encrypts or decrypts messages using character shifting
from art import logo

print(logo)

# Define the alphabet for cipher operations
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Get user input for operation type with validation
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction in ["encode", "decode"]:
        break
    else:
        print("Invalid output. Write 'encode' or 'decode'.")

# Get message and shift amount from user
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Caesar cipher function that handles both encryption and decryption
def caesar(original_text, shift_amount):
    result_text = ""

    for letter in original_text:
        if letter in alphabet:
            # Calculate position in alphabet (0-25)
            position_alphabet = ord(letter) - ord(alphabet[0])
            
            # Apply shift based on operation type
            if direction == "encode":
                new_position = (position_alphabet + shift_amount) % 26
            elif direction == "decode":
                new_position = (position_alphabet - shift_amount) % 26
                
            # Convert back to character and add to result
            new_letter = chr(new_position + ord(alphabet[0]))
            result_text += new_letter
        else:
            # Preserve non-alphabet characters
            result_text += letter
            
    print(f"The {direction}d message is: {result_text}")

# Execute the cipher function
caesar(original_text=text, shift_amount=shift)
