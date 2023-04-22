from turtle import Turtle

class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.score_text = Turtle()
        self.score_text.penup()
        self.score_text.color("white")
        self.score_text.hideturtle()
        self.score_text.sety(250)
        self.score_text.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 12, 'bold'))

    def increase(self):
        self.score_text.clear()
        self.score += 1
        self.score_text.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 12, 'bold'))