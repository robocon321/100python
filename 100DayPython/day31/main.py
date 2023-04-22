from tkinter import *
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("translate.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next():
    if len(to_learn) == 0:
        return

    global current_card

    current_card = rd.choice(to_learn)
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("words_to_learn.csv", index = False)

    canvas.itemconfig(canvas_image, image = front_image)
    canvas.itemconfig(canvas_lang, text = "English")
    canvas.itemconfig(canvas_content, text = current_card["English"])

def flip():
    global current_card
    canvas.itemconfig(canvas_image, image = back_image)
    canvas.itemconfig(canvas_lang, text = "Vietnamese")
    canvas.itemconfig(canvas_content, text = current_card["Vietnamese"])


window = Tk()
window.title("Flash card")
window.minsize(width = 450, height = 300)
window.configure(bg = BACKGROUND_COLOR, pady = 20, padx = 20)

front_image = PhotoImage(file = "images/card_front.png")
back_image = PhotoImage(file = "images/card_back.png")
right_image = PhotoImage(file = "images/right.png")
wrong_image = PhotoImage(file = "images/wrong.png")

canvas = Canvas(width = 800, height = 526, bg =  BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(0, 0, image=front_image, anchor="nw")
canvas_lang = canvas.create_text(400, 150, text = "English", font = ("Arial", 20, "bold"))
canvas_content = canvas.create_text(400, 250, text = "Word", font = ("Arial", 18, "normal"))
canvas.grid(row = 0, column = 0, columnspan = 2)

btnWrong = Button(image = wrong_image, highlightthickness=0, bg = BACKGROUND_COLOR, command = flip)
btnWrong.grid(row = 1, column = 0)

btnRight = Button(image = right_image, highlightthickness=0, bg = BACKGROUND_COLOR, command = next)
btnRight.grid(row = 1, column = 1)

next()


mainloop()