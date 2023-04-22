from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 100, height = 100)
window.configure(background="white")
window.configure(padx=10, pady=20)

entryMile = Entry(highlightthickness=1)
entryMile.config(highlightbackground="blue", highlightcolor="blue")
entryMile.grid(column = 2, row = 1)

lblMile = Label(text = "Miles", background = "white")
lblMile.grid(column = 3, row = 1)

lblEqual = Label(text = "is equal to", background = "white")
lblEqual.grid(column = 1, row = 2)

lblResult = Label(text = "0", background = "white")
lblResult.grid(column = 2, row = 2)

lblKm = Label(text = "Km", background = "white")
lblKm.grid(column = 3, row = 2)

def calculate():
    input = entryMile.get()
    result = float(input) * 1.609
    lblResult.config(text = result)

btn = Button(text = "Calculate", background = "white", command=calculate)
btn.grid(column = 2, row = 3)

mainloop()