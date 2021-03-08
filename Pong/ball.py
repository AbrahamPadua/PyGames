from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ms = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def ybounce(self):
        self.y_move *= -1

    def xbounce(self):
        self.ms *= 0.9
        self.x_move *= -1

    def reset_pos(self):
        self.ms = 0.1
        self.goto(0, 0)
        self.x_move *= -1
