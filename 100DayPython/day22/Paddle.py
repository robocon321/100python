from turtle import Turtle

class Paddle:
    def __init__(self, x, y):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, y)

    def up(self):
        new_y = self.paddle.ycor() + 20
        if (new_y > 260):
            return
        self.paddle.sety(new_y)

    def down(self):
        new_y = self.paddle.ycor() - 20
        if (new_y < -240):
            return
        self.paddle.sety(new_y)
