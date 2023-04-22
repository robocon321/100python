from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Score import Score
from GameOver import GameOver

screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("Snake game")
screen.colormode(255)
screen.bgcolor("black")
screen.tracer(0)

score = Score()
snake = Snake()
snake.create_snake()
food = Food()

game_is_on = True

screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) <= 15:
        snake.extend()
        food.refresh()
        score.increase()

    if snake.gameOver():
        game_is_on = False
        game_over = GameOver()
        

screen.exitonclick()