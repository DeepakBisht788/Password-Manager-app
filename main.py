from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
RED = "#e7305b"
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    epassword.insert(0, password)
    pyperclip.copy(password)

# SAVE PASSWORD
def save():

    website = ewebsite.get()
    email = e_email.get()
    password = epassword.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:

                data = json.load(data_file) #Reading old data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:

            data.update(new_data) #Updating old data with new data

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4) #Saving updated data
        finally:
            ewebsite.delete(0, END)
            epassword.delete(0, END)


# FIND PASSWORD
def find_password():
    website = ewebsite.get()
    try:

        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="file not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message="website not found")



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
ewebsite = Entry(width=35)
ewebsite.grid(row=1, column=1)
ewebsite.focus()
e_email = Entry(width=54)
e_email.grid(row=2, column=1, columnspan=2)
e_email.insert(0, "xyz@gmail.com")
epassword = Entry(width=35)
epassword.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=15, command=find_password,fg=RED)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password,fg=RED,width=15)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()