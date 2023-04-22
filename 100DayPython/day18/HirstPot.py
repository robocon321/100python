from turtle import Turtle, Screen
import random as rd
import colorgram

colors_extract = colorgram.extract('../resources/images/hirstpot.jpg', 10)
colors = []

for item in colors_extract:
    r = item.rgb.r
    g = item.rgb.g
    b = item.rgb.b

    new_rgb = (r, g, b)
    colors.append(new_rgb)


turtle = Turtle()
turtle.speed(50)
turtle.hideturtle()

screen = Screen()
screen.colormode(255)

turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

def drawLine():
    length = 400
    while(length >= 0):
        turtle.pendown()
        turtle.dot(10, rd.choice(colors))
        turtle.penup()
        turtle.forward(30)
        length -= 30
    turtle.pendown()
    turtle.dot(10, rd.choice(colors))
    turtle.penup()

def draw2Line():
    drawLine()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    drawLine()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)


draw2Line()
draw2Line()
draw2Line()
draw2Line()
screen.exitonclick()