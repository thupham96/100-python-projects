# Day 30: Password Manager with JSON

Welcome to the enhanced **Password Manager with JSON**! This secure and intuitive application allows you to generate, store, search, delete, and manage passwords efficiently using a JSON file for reliable and structured storage. Built using Tkinter, it provides a smooth graphical user interface for seamless interaction.

## How It Works

1. **Generate Password**: Instantly create strong, random passwords copied to your clipboard.
2. **Add Password**: Securely save website credentials (website, email, password) in a JSON file.
3. **Search Password**: Quickly retrieve stored credentials.
4. **Delete Password**: Remove credentials for outdated or unused websites.
5. **Copy Password**: Easily copy a stored password to the clipboard for convenience.

## Example Run

- **Generate Password**:
  - User inputs website and email, clicks **Generate**.
  - A robust password is auto-generated, displayed, and copied to the clipboard.
- **Add Credentials**:
  - User clicks **Add**.
  - Details are securely stored in `data.json`.
- **Search Credentials**:
  - User enters website and clicks **Search**.
  - Stored credentials appear in a popup if found.
- **Delete Credentials**:
  - User specifies website and clicks **Delete**.
  - Confirmation popup appears, and credentials are deleted.
- **Copy Stored Password**:
  - User enters website and clicks **Copy Password**.
  - Password for the specified website is copied directly to clipboard.

## Features

- **Advanced Password Generation**: Creates secure passwords mixing letters, numbers, and symbols.
- **Structured Storage with JSON**: Credentials stored neatly and securely in JSON format.
- **Intuitive Searching**: Effortlessly locate stored passwords.
- **Efficient Deletion**: Simple removal of outdated credentials.
- **Clipboard Integration**: Quick copying of generated or stored passwords.
- **Enhanced User Experience**: Modern and user-friendly GUI design with Tkinter.

## How to Use

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/your_username/python-projects.git
   cd Day30_PasswordManagerJSON
   ```
2. Ensure `logo.png` is present in your project folder.
3. Run the application:
   ```bash
   python password_manager_json.py
   ```
4. Use GUI buttons to interact, manage, and organize your passwords securely.

## Technologies Used

- Python 3
- Tkinter for GUI creation
- JSON for structured credential storage
- Pyperclip for clipboard functionality
- Random module for secure password generation

## What I Learned

- Using JSON files for efficient and structured data management.
- Enhancing GUI applications with intuitive and interactive features.
- Securely handling user inputs and file operations.
- Implementing efficient CRUD (Create, Read, Update, Delete) operations.
- Improving usability through clipboard integration and user alerts.

Secure your credentials easily and effectively with the enhanced **Password Manager with JSON**! 🔒✨
