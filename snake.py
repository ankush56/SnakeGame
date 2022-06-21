from turtle import Turtle
class Snake():
    def __init__(self):
        self.snake_segment = []
        self.create_segment()
        self.head = self.snake_segment[0]
        self.tail = self.snake_segment[-1]

    def create_segment(self):
        x_coordinate = 0
        y_coordinate = 0
        for _ in range(0, 4):
            # Creating 3 units snake
            turtle1 = Turtle()
            turtle1.shape("square")
            turtle1.color("green")
            turtle1.penup()
            turtle1.goto(x_coordinate, y_coordinate)
            self.snake_segment.append(turtle1)
            x_coordinate = x_coordinate - 20

    def move(self):
        for x in range(len(self.snake_segment) -1, 0, -1):
            new_x = self.snake_segment[x - 1].xcor()
            new_y = self.snake_segment[x - 1].ycor()
            self.snake_segment[x].goto(new_x, new_y)
        self.snake_segment[0].forward(20)


    # Set Controls
    def move_up(self):
        if self.snake_segment[0].heading() != 270:
            self.snake_segment[0].setheading(90)

    def move_left(self):
        if self.snake_segment[0].heading() != 0:
            self.snake_segment[0].setheading(180)

    def move_down(self):
        if self.snake_segment[0].heading() != 90:
            self.snake_segment[0].setheading(270)

    def move_right(self):
        if self.snake_segment[0].heading() != 180:
            self.snake_segment[0].setheading(0)

    def grow(self):
        self.new_turtle = Turtle()
        self.new_turtle.penup()
        self.new_turtle.shape("square")
        self.new_turtle.color("green")

        last_x_coordinate = self.snake_segment[-1].xcor()
        last_y_coordinate = self.snake_segment[-1].ycor()

        if(self.head.heading() == 0):
            self.new_turtle.goto(last_x_coordinate - 10, last_y_coordinate)
        if(self.head.heading == 90):
            self.new_turtle.goto(last_x_coordinate, last_y_coordinate - 10)
        if(self.head.heading() == 270):
            self.new_turtle.goto(last_x_coordinate, last_y_coordinate + 10)
        if(self.head.heading() == 180):
            self.new_turtle.goto(last_x_coordinate + 10, last_y_coordinate)

        self.snake_segment.append(self.new_turtle)

    def check_collision(self):
        for x in self.snake_segment[1:]:
            if self.head.distance(x) < 10:
                collision = True
            else:
                collision = False
        return collision
