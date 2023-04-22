from turtle import Turtle, Screen
import random as rd
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
SPEED = 40

class Snake:
    def __init__(self):
        self.segments = []

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            square = Turtle()
            square.shape("square")
            square.color("white")
            square.penup()
            square.goto(pos)
            self.segments.append(square)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head().forward(DISTANCE)

    def up(self):
        if(self.head().heading() == 270):
            return
        self.head().setheading(90)

    def down(self):
        if(self.head().heading() == 90):
            return
        self.head().setheading(270)

    def right(self):
        if(self.head().heading() == 180):
            return
        self.head().setheading(0)

    def left(self):
        if(self.head().heading() == 0):
            return
        self.head().setheading(180)

    def head(self):
        return self.segments[0]

    def headToOwnTail(self):
        for seg in self.segments:
            if seg.distance(self.head()) < 15 and not seg == self.head():
                return True
        return False

    def headToWall(self):
        return self.head().xcor() > 280 or self.head().ycor() > 280 or self.head().xcor() < -280 or self.head().ycor() < -280

    def gameOver(self):
        return  self.headToWall() or self.headToOwnTail()

    def add_segment(self, pos):
        square = Turtle("square")
        square.hideturtle()
        square.color("white")
        square.penup()
        square.goto(pos)
        square.showturtle()
        self.segments.append(square)

    def extend(self):
        self.add_segment(self.segments[-1].position())