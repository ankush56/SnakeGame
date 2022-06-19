from turtle import Turtle
class Snake(Turtle):
    def __init__(self):
        pass

    def create_segment(self):
        snake_segment = []
        x_coordinate = 0
        y_coordinate = 0
        for _ in range(0, 4):
            # Creating 3 units snake

            turtle1 = Turtle()
            turtle1.shape("square")
            turtle1.color("white")
            turtle1.penup()
            turtle1.goto(x_coordinate, y_coordinate)
            snake_segment.append(turtle1)
            x_coordinate = x_coordinate - 20
        return snake_segment



