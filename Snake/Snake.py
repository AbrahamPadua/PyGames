from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.direction = (20, 0)
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        firstX = self.segments[0].xcor()
        firstY = self.segments[0].ycor()
        self.segments[0].goto(firstX + self.direction[0],
                              firstY + self.direction[1])

    def up(self):
        if self.direction[1] != -20:
            self.direction = (0, 20)

    def down(self):
        if self.direction[1] != 20:
            self.direction = (0, -20)

    def right(self):
        if self.direction[0] != -20:
            self.direction = (20, 0)

    def left(self):
        if self.direction[0] != 20:
            self.direction = (-20, 0)
