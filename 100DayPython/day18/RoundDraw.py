from turtle import Turtle, Screen
import random as rd

arc = 3
turtle = Turtle()
turtle.speed(80)

screen = Screen()
screen.colormode(255)

for i in range(int(360 / arc)):
    r = rd.randint(1, 255)
    g = rd.randint(1, 255)
    b = rd.randint(1, 255)
    turtle.pencolor((r, g, b))

    turtle.circle(100)
    turtle.right(arc)

screen.exitonclick()