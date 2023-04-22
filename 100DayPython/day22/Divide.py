from turtle import Turtle

class Divide:
    def __init__(self):
        self.divide = Turtle()
        self.divide.shape("square")
        self.divide.color("white")
        self.divide.penup()
        self.divide.shapesize(stretch_len = 0.1, stretch_wid = 0.1)
        self.divide.goto(0, 240)
        self.divide.pendown()
        self.divide.setheading(270)
        self.divide.forward(600)
