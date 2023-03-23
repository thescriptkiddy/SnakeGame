from turtle import Screen
import time
from snake import Snake

# Day 20
# Todo Create snake body
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)

snake = Snake()
screen.listen()
# screen.onkey("Up")
# screen.onkey("Down")
# screen.onkey("Left")
# screen.onkey("Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

# Todo Control the snake


# Day 21
# Todo Detect collision with food
# Todo Create a score board
# Todo Detect collision with wall
# Todo Detect collision with tail


screen.exitonclick()
