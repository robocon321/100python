from turtle import Turtle

class Score:
    def __init__(self):
        self.score = Turtle()
        self.left_score = 0
        self.right_score = 0
        self.score.goto(0, 250)
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.write(f"{self.left_score}:{self.right_score}", move=False, align='center', font=('Arial', 20, 'bold'))

    def refresh(self):
        self.score.clear()
        self.score.write(f"{self.left_score}:{self.right_score}", move=False, align='center', font=('Arial', 20, 'bold'))
