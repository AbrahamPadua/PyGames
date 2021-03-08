from turtle import Turtle


class Player(Turtle):
    def __init(self):
        self.start_pos = []

    def create_slab(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.start_pos)

    def move_up(self):
        if self.ycor() <= 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() >= -230:
            self.goto(self.xcor(), self.ycor() - 20)


class Player1(Player):
    def __init__(self):
        self.start_pos = (-390, 0)
        self.create_slab()


class Player2(Player):
    def __init__(self):
        self.start_pos = (380, 0)
        self.create_slab()
