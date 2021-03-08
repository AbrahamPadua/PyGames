from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Level: {self.level}", align="center",
                   font=("Courier", 20, "normal"))

    def level_cleared(self):
        self.goto(0, 0)
        self.write(f"Level {self.level} cleared!",
                   align="center", font=("Courier", 30, "normal"))

    def game_over(self):
        self.goto(0, 10)
        self.write("GAME OVER", align="center", font=("Courier", 50, "bold"))
        self.goto(0, -10)
        self.write('Press "R" to restart', align="center",
                   font=("Courier", 20, "normal"))
