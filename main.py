from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters= random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    random_letters = [random.choice(letters) for _ in range(1, nr_letters + 1)]
    random_symbols = [random.choice(symbols) for _ in range(1, nr_symbols + 1)]
    random_numbers =[random.choice(numbers) for _ in range(1, nr_numbers + 1)]
    password = random_letters + random_symbols + random_numbers
    random.shuffle(password)
    password_entry.insert(END, "".join(password))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website =website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
            }
        }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        return messagebox.showwarning(title="Empty Fields", message="The fields can not be empty!")
    else:                            
        with open("data.json", "r") as file:
            data = json.load(file)
            data.update(new_data)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
            
        website_entry.delete(0, END)
        password_entry.delete(0, END)                          
# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image =PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)
#Webiste label and input
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
#Website Entry
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2, sticky="w")
#Email/Username Label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
#Email/Username Entry
email_entry = Entry(width=35)
email_entry.insert(END, "persianhoplite@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
#Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
#Password Entry
password_entry = Entry(width=30)
password_entry.grid(column=1,row=3, sticky="w")
#Password Generator Button
password_generate_btn = Button(text="Generate Password", command=generate_password)
password_generate_btn.grid(column=2, row=3)
#Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")
window.mainloop()