from turtle import Turtle, Screen

turtle = Turtle()
turtle.speed(20)

def forward():
    turtle.forward(10)

def backward():
    turtle.right(180)

def clear():
    turtle.clear()

def counter_clockwise():
    turtle.left(10)
    turtle.forward(10)

def clockwise():
    turtle.right(10)
    turtle.forward(10)

screen = Screen()
screen.colormode(255)

screen.listen()

screen.onkeypress(key = "w", fun = forward)
screen.onkeypress(key = "s", fun = backward)
screen.onkeypress(key = "a", fun = counter_clockwise)
screen.onkeypress(key = "d", fun = clockwise)
screen.onkeypress(key = "c", fun = clear)

screen.exitonclick()
