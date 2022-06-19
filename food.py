from turtle import Turtle
import random

class Food():
    def __init__(self):

        x_cor = random.randint(-460, 460)
        y_cor = random.randint(-460, 460)

        turtle = Turtle()
        turtle.shape("turtle")
        turtle.color("Green")
        turtle.shapesize(1, 1)
        turtle.penup()
        turtle.goto(x_cor, y_cor)
