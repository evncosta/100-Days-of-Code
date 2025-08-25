from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction in ["encode", "decode"]:
        break
    else:
        print("Invalid output. Write 'encode' or 'decode'.")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount):
    result_text = ""

    for letter in original_text:
        if letter in alphabet:
            position_alphabet = ord(letter) - ord(alphabet[0])
            if direction == "encode":
                new_position = (position_alphabet + shift_amount) % 26
            elif direction == "decode":
                new_position = (position_alphabet - shift_amount) % 26
            new_letter = str(new_position + ord(alphabet[0]))
            result_text += new_letter
        else:
            result_text += letter
    print(f"The {direction}d message is: {result_text}")

caesar(original_text = text, shift_amount = shift)