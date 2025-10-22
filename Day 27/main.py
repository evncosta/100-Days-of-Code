# Miles to Kilometers Converter - GUI application using tkinter
from tkinter import *

def miles_to_km():
    # Convert miles to kilometers and update result label
    miles = float(miles_input.get())
    kilometers = miles * 1.60934
    kilometer_result_label.config(text=f"{kilometers:.2f}")

# Set up main window
window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)  # Add padding around widgets

# Create input field for miles
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Create labels for conversion display
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Create calculate button that triggers conversion
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Start the GUI event loop
window.mainloop()
