# Mail Merge Project - Creates personalized letters from template and name list
with open("Input/Names/invited_names.txt", "r") as guests:
    guest_list = guests.readlines()

with open("Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_template = letter_file.read()

# Generate personalized letter for each guest
for name in guest_list:
    clean_name = name.strip()  # Remove newline characters
    letter = letter_template.replace("[name]", clean_name)  # Insert name into template

    # Save personalized letter to output directory
    with open(f"Output/ReadyToSend/letter_for_{clean_name}.txt", "w") as output_file:
        output_file.write(letter)
