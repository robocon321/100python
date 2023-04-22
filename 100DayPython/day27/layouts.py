from tkinter import *

window = Tk()
window.title("Style layouts")
window.minsize(width = 300, height = 400)
# window.config(padx= 50, pady = 50)

## place layout

# label1 = Label()
# label1.config(text = "Place layout")
# label1.place(x = 100, y = 50)
#
# label2 = Label()
# label2.config(text = "Place layout")
# label2.place(x = 50, y = 100)


## grid layout

label1 = Label()
label1.config(text = "Place layout")
label1.grid(column = 2, row = 2)

label2 = Label()
label2.config(text = "Place layout")
label2.grid(column = 2, row = 1)


mainloop()