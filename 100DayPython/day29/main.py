from tkinter import *
from tkinter import messagebox
import secrets
import string
import pyperclip
import json

def generatePassword():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password
    return password

def generate():
    password = generatePassword()
    entryPwd.delete(first = 0, last = END)
    entryPwd.insert(0, string = password)
    pyperclip.copy(password)

def save():
    website = entryWebsite.get()
    email = entryEmail.get()
    pwd = entryPwd.get()
    new_data = {
        website: {
            "email": email,
            "password": pwd
        }
    }

    if len(website) == 0:
        messagebox.askyesno(title="Message", message="You must enter your website")
        return

    if len(email) == 0:
        messagebox.askyesno(title="Message", message="You must enter your email")
        return

    if len(pwd) == 0:
        messagebox.askyesno(title="Message", message="You must enter your password")

    try:
        with open("test.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("test.json", "w") as file:
            json.dump(new_data, file, indent=2)
    else:
        data.update(new_data)
        with open("test.json", "w") as file:
            json.dump(data, file, indent=2)
    finally:
        entryWebsite.delete(0, END)
        entryEmail.delete(0, END)
        entryPwd.delete(0, END)

def findWebsite():
    website = entryWebsite.get()
    try:
        with open("test.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Message", message = "File was not found")
    else:
        if website in data:
            email = data[website]["email"]
            pwd = data[website]["password"]
            messagebox.showinfo(title = "Message", message = f"Email: {email} \nPassword: {pwd}")
        else:
            messagebox.showinfo(title = "Message", message = "Your account in this website was not found")
window = Tk()
window.title("Password manager")
window.config(padx = 20, pady = 20)
window.minsize(700, 500)
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 1)
window.rowconfigure(3, weight = 1)
window.rowconfigure(4, weight = 1)

canvas = Canvas(width = 200, height = 200)
image = PhotoImage(file = "logo.png")
canvas.create_image(150, 100, image = image)
canvas.grid(row = 0, column = 1, sticky= 'we')


lblWebsite = Label(text = "Website: ")
lblWebsite.configure(padx = 5, pady = 5)
lblWebsite.grid(row = 1, column = 0)

entryWebsite = Entry()
entryWebsite.grid(row = 1, column = 1, sticky = 'we')

btnSearch = Button(text = "Search", command = findWebsite)
btnSearch.grid(row = 1, column = 2, sticky = 'we')


lblEmail = Label(text = "Email/Username: ")
lblEmail.configure(padx = 5, pady = 5)
lblEmail.grid(row = 2, column = 0)

entryEmail = Entry()
entryEmail.grid(row = 2, column = 1, columnspan = 2, sticky = 'we')

lblPwd = Label(text = "Password: ")
lblPwd.configure(padx = 5, pady = 5)
lblPwd.grid(row = 3, column = 0)

entryPwd = Entry()
entryPwd.grid(row = 3, column = 1, sticky = 'we')

btnGenerate = Button(text = "Generate Password", command = generate)
btnGenerate.configure(padx = 5, pady = 5)
btnGenerate.grid(row = 3, column = 2, sticky = 'we')

btnAdd = Button(text = "Add", command = save)
btnAdd.configure(padx = 5, pady = 5)
btnAdd.grid(row = 4, column = 1, columnspan = 2, sticky = 'we')

mainloop()
