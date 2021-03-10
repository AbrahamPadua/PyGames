from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", "r") as hs:
            self.high_score = int(hs.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)
        self.goto(0, 260)
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("highscore.txt", "w") as hs:
                hs.write(f"{self.high_score}")
        self.goto(0, 10)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -10)
        self.write("Press R to restart", align=ALIGNMENT,
                   font=("Courier", 10, "normal"))
        self.goto(0, -30)
        self.write("Press E to reset High Score", align=ALIGNMENT,
                   font=("Courier", 10, "normal"))

    def reset_hs(self):
        with open("highscore.txt", "w") as hs:
            hs.write("0")
