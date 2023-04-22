from turtle import Screen, Turtle
import random as rd

timmy_turtle = Turtle()
timmy_turtle.speed(15)
timmy_turtle.pensize(10)

screen = Screen()
screen.colormode(255)

n_shape = rd.randint(3, 12)
arc = 180 - (n_shape - 2) * 180 / n_shape

while(n_shape > 0):
    r = rd.randint(1, 255)
    g = rd.randint(1, 255)
    b = rd.randint(1, 255)
    timmy_turtle.pencolor((r, g, b))
    timmy_turtle.forward(100)
    timmy_turtle.right(arc)
    n_shape -= 1

screen.exitonclick()