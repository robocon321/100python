from turtle import Turtle, Screen
import random as rd

screen = Screen()
screen.colormode(255)

turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color((25, 55, 55))
turtle1.penup()
turtle1.setheading(225)
turtle1.forward(141)
turtle1.setheading(0)

turtle2 = Turtle()
turtle2.shape("turtle")
turtle2.color((25, 80, 200))
turtle2.penup()
turtle2.setheading(207)
turtle2.forward(110)
turtle2.setheading(0)

turtle3 = Turtle()
turtle3.shape("turtle")
turtle3.color((15, 255, 15))
turtle3.penup()
turtle3.setheading(155)
turtle3.forward(110)
turtle3.setheading(0)


turtle4 = Turtle()
turtle4.shape("turtle")
turtle4.color((25, 25, 30))
turtle4.penup()
turtle4.setheading(135)
turtle4.forward(141)
turtle4.setheading(0)

opponents = [turtle1, turtle2, turtle3, turtle4]

is_over = False
while not is_over:
    for index, item in enumerate(opponents):
        step = rd.randint(10, 20)
        item.forward(step)
        if(item.pos()[0] >= 200):
            is_over = True
            print(f"Turtle {index} win!")
            break

screen.exitonclick()