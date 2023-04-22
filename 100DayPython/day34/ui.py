from tkinter import *
THEME_COLOR = "#375362"

class UI:
    def __init__(self, quiz):
        self.quiz = quiz
        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.lblScore = Label(text = f"Score: {quiz.score}/{quiz.question_number}", bg = THEME_COLOR, fg = "white", font = ("Arial", 15, 'bold'))
        self.lblScore.grid(row = 0, column = 1, padx=20, pady=20)

        self.canvas = Canvas(width = 300, height = 250, bg = "white", highlightthickness=0)
        self.canvas_question = self.canvas.create_text(150, 125, width = 200, text = quiz.current_question.text, font = ("Arial", 15, 'italic'))
        self.canvas.grid(row = 1, column = 0, columnspan = 2, padx=20, pady=20)

        trueImage = PhotoImage(file = "images/true.png")
        falseImage = PhotoImage(file = "images/false.png")

        def choose_true():
            quiz.check_answer('True')
            self.lblScore.config(text=f"Your score: {quiz.score}/{quiz.question_number}")
            self.canvas.itemconfig(self.canvas_question, text=quiz.current_question.text)
            quiz.next_question()

        def choose_false():
            quiz.check_answer('False')
            self.lblScore.config(text=f"Your current score is: {quiz.score}/{quiz.question_number}")
            self.canvas.itemconfig(self.canvas_question, text= quiz.current_question.text)
            quiz.next_question()

        self.btnTrue = Button(image=trueImage, highlightthickness=0, borderwidth=0, command = choose_true)
        self.btnTrue.grid(row = 2, column = 0, padx=20, pady=20)

        self.btnFalse = Button(image=falseImage, highlightthickness=0, borderwidth=0, command = choose_false)
        self.btnFalse.grid(row = 2, column = 1, padx=20, pady=20)

        mainloop()
