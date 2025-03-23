from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get().strip()
    email_username = email_username_entry.get().strip()
    password = password_entry.get().strip()
    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }

    if not website or not password:
        messagebox.showwarning("Missing Information", "Please fill in both the Website and Password fields.")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    for stored_website in data.keys():
        if stored_website.lower() == website.lower():
            confirm = messagebox.askyesno("Modify Entry", f"'{website}' already exists. Do you want to modify the password?")
            print(confirm)
            if not confirm:
                return

    data.update(new_data)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get().strip().lower()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            found = False
            for stored_website in data.keys():
                if stored_website.lower()==website.lower():
                    email = data[stored_website]['email']
                    password = data[stored_website]['password']
                    messagebox.showinfo(title=stored_website, message=f"Email: {email}\nPassword: {password}")
                    found = True
                    break
            if not found:
                messagebox.showerror(title="Not Found", message="No details for the website exist.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")

# ---------------------------- DELETE PASSWORD ------------------------------- #
def delete_password():
    website = website_entry.get().strip()
    if not website:
        messagebox.showinfo(title="Info", message="Please enter a website to delete.")
        return

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            found = False
            for stored_website in data.keys():
                if stored_website.lower() == website.lower():
                    found = True
                    del data[stored_website]
                    break

        with open("data.json", mode="w") as file:
            json.dump(data, file, indent=4)

        if found:
            messagebox.showinfo(title="Deleted", message=f"Details for {website} has been deleted.")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details found for {website}.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")

# ---------------------------- COPY PASSWORD ------------------------------- #
def copy_password():
    website = website_entry.get().strip().lower()
    if not website:
        messagebox.showinfo(title="Info", message="Please enter a website to copy.")
        return

    found = False  # Initialize found before the loop
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            for stored_website in data.keys():
                if stored_website.lower()==website.lower():
                    found = True
                    password = data[stored_website]['password']
                    pyperclip.copy(password)
                    break

        if found:
            messagebox.showinfo(title="Copied", message=f"Password for {website} has been copied.")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details found for {website}.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

Label(text="Website:").grid(column=0, row=1)
Label(text="Email/Username:").grid(column=0, row=2)
Label(text="Password:").grid(column=0, row=3, pady=5)

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, pady=5)
website_entry.focus()

email_username_entry = Entry(width=51)
email_username_entry.grid(column=1, row=2, columnspan=2, pady=5)
email_username_entry.insert(0, "user@example.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, pady=5)

Button(text="Generate", width=15, command=generate_password).grid(column=2, row=3, pady=5)
Button(text="Search", width=15, command=search_password).grid(column=2, row=1, pady=5)
Button(text="Add", width=44, command=add_password).grid(column=1, row=4, columnspan=2, pady=5)
Button(text="Delete", width=15, command=delete_password).grid(column=1, row=5, pady=5)
Button(text="Copy Password", width=15, command=copy_password).grid(column=2, row=5, pady=5)

window.mainloop()
