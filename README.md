# Password Manager
A simple and secure password manager built using Python's `tkinter` library. This application allows you to generate strong passwords, save them securely in a JSON file, and retrieve saved credentials for various websites.

## Features
1. **Password Generator**:
   - Creates strong random passwords using a combination of letters, numbers, and symbols.
   - Automatically copies the generated password to the clipboard.

2. **Save Passwords**:
   - Saves website credentials (website, email, and password) into a JSON file.
   - Ensures no fields are left empty before saving.
   - Updates the saved credentials if a website already exists.

3. **Find Passwords**:
   - Quickly search for saved credentials by entering a website name.
   - Displays the email and password in a message box.
   - Notifies the user if the website or the data file is not found.
