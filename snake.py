from turtle import Turtle

X_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.list_of_snakes = []
        self.create_snake()
        self.head = self.list_of_snakes[0]

    def create_snake(self):
        for snake in range(0, 3):
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(x=X_POSITIONS[snake], y=0)
            self.list_of_snakes.append(new_snake)

    def move_snake(self):
        for snake_num in range(len(self.list_of_snakes) - 1, 0, -1):
            new_x = self.list_of_snakes[snake_num - 1].xcor()
            new_y = self.list_of_snakes[snake_num - 1].ycor()
            self.list_of_snakes[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.forwoard(10)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.forwoard(10)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.forwoard(10)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.forwoard(20)
