from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("yellow")
        self.shapesize(1, 1)
        self.penup()
        self.refresh()


    def refresh(self):
        x_cor = random.randint(-350, 350)
        y_cor = random.randint(-350, 350)
        self.goto(x_cor, y_cor)