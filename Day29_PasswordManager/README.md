# Day 29: Password Manager (Enhanced Version)

Welcome to the **Password Manager**! This secure and user-friendly application helps you store, generate, search, and manage passwords efficiently. It features an intuitive graphical interface built with Tkinter.

## How It Works

1. **Generate Password**: Automatically generates a strong password and copies it to the clipboard.
2. **Add Password**: Saves website credentials (website, email, password) to a data file.
3. **Search Password**: Retrieves stored credentials for a given website.
4. **Delete Password**: Removes stored credentials for a specific website.
5. **Copy Password**: Copies a stored password directly to the clipboard for easy use.

## Example Run

- **User enters** a website and email, then clicks **Generate**:
  - A random password appears in the entry field and is copied to the clipboard.
- **User clicks Add**:
  - Credentials are saved in a `data.txt` file.
- **User clicks Search**:
  - If the website exists, a popup displays the stored credentials.
- **User clicks Delete**:
  - The corresponding website's credentials are removed from the file.
- **User clicks Copy Password**:
  - The saved password for the website is copied to the clipboard.

## Features

- **Secure Password Generation**: Creates strong, random passwords with a mix of letters, numbers, and symbols.
- **Persistent Storage**: Stores credentials in a text file for later retrieval.
- **Search Functionality**: Quickly look up stored credentials.
- **Data Deletion**: Remove saved credentials when no longer needed.
- **Clipboard Integration**: Automatically copies generated and stored passwords.
- **User-Friendly Interface**: Clean and organized Tkinter GUI.

## How to Use

1. Clone the repository and navigate to the `Day29_PasswordManager` folder:
   ```bash
   git clone https://github.com/your_username/python-projects.git
   cd Day29_PasswordManager
   ```
2. Ensure you have `logo.png` in the project directory for the GUI.
3. Run the application:
   ```bash
   python password_manager.py
   ```
4. Use the interactive buttons to generate, save, search, delete, or copy passwords.

## Technologies Used

- Python 3
- Tkinter for GUI development
- Random module for password generation
- Pyperclip for clipboard functionality
- Messagebox for user notifications

## What I Learned

- Enhancing GUI applications with Tkinter widgets.
- Implementing password storage and retrieval using file handling.
- Adding clipboard integration for seamless password copying.
- Improving user interaction with alerts and confirmation dialogs.
- Managing application state for CRUD (Create, Read, Update, Delete) functionality.

Secure your passwords with ease using this intuitive **Password Manager**! 🔒✨
