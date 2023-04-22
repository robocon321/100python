from turtle import Screen
import random as rd
import time
from Paddle import Paddle
from Score import Score
from Divide import Divide
from Ball import Ball

screen = Screen()
screen.title("Ping pong")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)
score = Score()
divide = Divide()
ball = Ball()

screen.listen()
screen.onkeypress(fun = paddle_right.up, key = "Up")
screen.onkeypress(fun = paddle_right.down, key = "Down")
screen.onkeypress(fun = paddle_left.up, key = "w")
screen.onkeypress(fun = paddle_left.down, key = "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if(paddle_left.paddle.distance(ball.ball) < 50 and ball.ball.xcor() < -320):
        angle = rd.randint(-45, 45)
        ball.ball.setheading(angle)

    if(paddle_right.paddle.distance(ball.ball) < 50 and ball.ball.xcor() > 320):
        angle = rd.randint(135, 205)
        ball.ball.setheading(angle)

    ball.moveToBorder()

    if(ball.ball.xcor() > 390):
        score.left_score += 1
        ball.refresh()
        score.refresh()

    if(ball.ball.xcor() < -390):
        score.right_score += 1
        ball.refresh()
        score.refresh()

screen.exitonclick()