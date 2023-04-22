from turtle import Turtle, Screen
import random as rd

timmy_turtle = Turtle()
timmy_turtle.speed(5)

screen = Screen()
screen.colormode(255)

for i in range(100):
    r = rd.randint(1, 255)
    g = rd.randint(1, 255)
    b = rd.randint(1, 255)
    arc = rd.randrange(0, 361, 90)
    length = rd.randint(20, 50)
    pensize = rd.randint(1, 4)

    timmy_turtle.pensize(pensize)
    timmy_turtle.pencolor((r, g, b))
    timmy_turtle.forward(length)
    timmy_turtle.right(arc)

screen.exitonclick()
