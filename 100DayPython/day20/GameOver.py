from turtle import Turtle

class GameOver:
    def __init__(self):
        self.score = 0
        self.score_text = Turtle()
        self.score_text.penup()
        self.score_text.color("white")
        self.score_text.hideturtle()
        self.score_text.write("GAME OVER", move=False, align="center", font=('Arial', 20, 'bold'))