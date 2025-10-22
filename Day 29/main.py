# Password Manager - GUI application for storing and generating passwords
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

def generate_password():
    # Character sets for password generation
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate password with random character distribution
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)  # Randomize character order
    password = "".join(password_list)
    
    pyperclip.copy(password)  # Copy password to clipboard
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def save():
    # Save password entry to file after validation
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    # Validate required fields are filled
    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Empty fields", message="Please don't leave any empty fields")
    elif messagebox.askokcancel(title=website, message=f"You've entered: \nEmail: {email}\nPassword: {password}"
                                                       f"\nIs it OK to save?"):
        # Save to file and clear entries
        with open("data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# Set up main application window
window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

# Create logo canvas
canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

# Create and position labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", width=21)
password_label.grid(column=0, row=3)

# Create and position buttons
generate_button = Button(text="Generate Password", width=21, command=generate_password)
generate_button.grid(column=2, row=3, columnspan=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# Create and position entry fields
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()  # Set initial focus to website field
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "phillip@email.com")  # Pre-fill with default email
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

# Start the application
window.mainloop()
