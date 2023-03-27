from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

# Day 20
# Todo Create snake body
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SnakeGame")
screen.tracer(0)

snake = Snake()
scoreboard = Score()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

print(scoreboard.num_food)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

    # Todo Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()


# Todo Create a score board

# Todo Detect collision with wall

# Todo Detect collision with tail



screen.exitonclick()
