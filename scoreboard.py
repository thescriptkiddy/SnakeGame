from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(y=270, x=0)
        self.hideturtle()
        self.num_food = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.num_food, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.num_food += 1
        self.clear()
        self.update_scoreboard()
