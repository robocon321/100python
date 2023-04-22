from turtle import Turtle, Screen
import random as rd

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("purple")
timmy_turtle.speed(15)

screen = Screen()
screen.colormode(255)

for i in range(1,160):
    r = rd.randint(1, 255)
    g = rd.randint(1, 255)
    b = rd.randint(1, 255)
    timmy_turtle.pencolor((r, g, b))
    timmy_turtle.forward(100 * i / 30)
    timmy_turtle.right(90)

screen.exitonclick()