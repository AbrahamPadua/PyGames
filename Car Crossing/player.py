from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.penup()
        self.goto(0, -260)
        self.left(90)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 50)

    def move_left(self):
        if self.xcor() > -400:
            self.goto(self.xcor() - 50, self.ycor())

    def move_right(self):
        if self.xcor() < 400:
            self.goto(self.xcor() + 50, self.ycor())
