from tkinter import *
from tkinter import messagebox

def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.60934, 2)
        kilometer_result.config(text=f"{km}")
    except ValueError:
        messagebox.showerror(title="Invalid input", message="Please enter a numeric value!")

def clear_fields():
    miles_input.delete(0, END)
    kilometer_result.config(text="0")

def copy_result():
    window.clipboard_clear()
    window.clipboard_append(kilometer_result.cget("text"))

window = Tk()
window.title("Miles ↔ Kilometers Converter")
window.minsize(width=400, height=150)
window.config(padx=90, pady=40)

# Input field
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_input.focus()

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 12))
is_equal_label.grid(column=0, row=1)

# Result label
kilometer_result = Label(text="0", font=("Arial", 12, "bold"))
kilometer_result.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

# Buttons
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

clear_button = Button(text="Clear", command=clear_fields)
clear_button.grid(column=2, row=2)

copy_button = Button(text="Copy Result", command=copy_result)
copy_button.grid(column=0, row=2)

# Bind Enter key
window.bind('<Return>', lambda event: miles_to_km())

window.mainloop()
