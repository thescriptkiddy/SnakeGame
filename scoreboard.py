from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(y=290, x=0)
        self.hideturtle()
        self.num_food = 0
        self.write(self.num_food)
