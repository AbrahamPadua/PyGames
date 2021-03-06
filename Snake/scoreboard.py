from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 10)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -20)
        self.write("Press R to restart", align=ALIGNMENT,
                   font=("Courier", 10, "normal"))
