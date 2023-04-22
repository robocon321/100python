from turtle import Turtle

class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.dot(20, "blue")
        self.ball.color("white")
        self.ball.hideturtle()

    def move(self):
        self.ball.pendown()
        self.ball.forward(10)
        self.ball.clear()
        self.ball.dot(20, "blue")

    def moveToBorder(self):
        if self.ball.ycor() > 300 or self.ball.ycor() < -300:
            self.ball.setheading(-self.ball.heading())


    def refresh(self):
        self.ball.clear()
        self.ball = Turtle()
        self.ball.dot(20, "blue")
        self.ball.color("white")
        self.ball.hideturtle()
