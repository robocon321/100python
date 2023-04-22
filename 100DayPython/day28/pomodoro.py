import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#3B9AE1"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady = 50, bg = YELLOW)

def start():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    long_time_break = LONG_BREAK_MIN * 60
    short_time_break = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        lblTimer.config(text = "Long Break", fg = RED)
        count_down(long_time_break)
    elif reps % 2 == 0:
        lblTimer.config(text = "Short Break", fg = PINK)
        count_down(short_time_break)
    else:
        mark = ""
        work_session = math.floor(reps / 2)
        for i in range(work_session):
            mark += "✓"
        lblCheck.config(text = mark)

        lblTimer.config(text = "Work", fg = GREEN)
        count_down(work_time)

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text = "00:00")
    lblTimer.config(text = "Timer")
    lblCheck.config(text = "")
    global reps
    reps = 0


def count_down(count):
    if(count < 0):
        start()
    else:
        global timer
        minute = math.floor(count / 60)
        second = count % 60
        canvas.itemconfig(canvas_text, text= f"{minute}:{second}")
        timer = window.after(10, count_down, count - 1)

lblTimer = Label()
lblTimer.config(text = "Timer", font = (FONT_NAME, 50, "normal"), fg = GREEN, bg = YELLOW)
lblTimer.grid(row = 1, column = 2)

canvas = Canvas(width = 210, height = 224, bg = YELLOW, highlightthickness = 0)
tomoto_image = PhotoImage(file = "tomato.png")
canvas_image = canvas.create_image(103, 103, image = tomoto_image)
canvas_text = canvas.create_text(103, 130, fill = "white", text = "00:00", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 2, column = 2)

btnStart = Button(text="Start", width = 10, bg = BLUE, fg = "white", highlightthickness= 0, borderwidth = 0, command = start)
btnStart.config(pady = 10)
btnStart.grid(row = 3, column = 1)

btnReset = Button(text="Reset", width = 10, bg = RED, fg = "white", highlightthickness= 0, borderwidth = 0, command = reset)
btnReset.config(pady = 10)
btnReset.grid(row = 3, column = 3)

lblCheck = Label(text = "✓", font = ("Arial", 18, "bold"), fg = GREEN, bg = YELLOW)
lblCheck.grid(row = 4, column = 2)

mainloop()