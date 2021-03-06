from turtle import Turtle
import random

LIMIT = (-280, 280)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.new_position()

    def new_position(self):
        foodX = random.randint(LIMIT[0], LIMIT[1])
        foodY = random.randint(LIMIT[0], LIMIT[1])
        self.goto(foodX, foodY)
