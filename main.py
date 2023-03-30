from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        return messagebox.showwarning(title="Empty Fields", message="The fields can not be empty!")
                                      
    is_ok = messagebox.askokcancel(f"{website_entry.get()}", message=f"These are the credentials you entered: \nEmail: {email_entry.get()} \nPassword: {password_entry.get()}")
    if is_ok:                               
        with open("data.txt", "a") as file:
            file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
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
password_generate_btn = Button(text="Generate Password")
password_generate_btn.grid(column=2, row=3)
#Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")
window.mainloop()