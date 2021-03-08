from turtle import Turtle

FONT = ("Courier", 60, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.p1_score = 0
        self.p2_score = 0
        self.update_point()

    def update_point(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=FONT)
