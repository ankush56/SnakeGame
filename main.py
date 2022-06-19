from turtle import Turtle, Screen
import time
from snake import Snake
from snake_screen import Snake_screen
from food import Food


# Set Play Screen using snake_Screen class.
screen1 = Snake_screen().set_screen()

#Set snake segment- 3 blocks long
snake_segment = Snake().create_segment()

food = Food()


# Set Controls
def move_up():
    snake_segment[0].setheading(90)

def move_left():
    snake_segment[0].setheading(180)

def move_down():
    snake_segment[0].setheading(270)

def move_right():
    snake_segment[0].setheading(0)


screen1.onkey(move_up, 'Up')
screen1.onkey(move_left, 'Left')
screen1.onkey(move_down, 'Down')
screen1.onkey(move_right, 'Right')





#Run Snake
# Initializing
run = True
screen1.update()
time.sleep(1)
screen1.tracer(0)

while run:
    x = 1
    grow = False
    screen1.update()
    snake_segment[0].forward(2)

    while x < len(snake_segment):
        last_x_coordinate = snake_segment[x - 1].xcor()
        last_y_coordinate = snake_segment[x - 1].ycor()
        if(snake_segment[0].heading() == 0):
            snake_segment[x].goto(last_x_coordinate - 20, last_y_coordinate)
        if(snake_segment[0].heading() == 90):
            snake_segment[x].goto(last_x_coordinate, last_y_coordinate - 20)
        if(snake_segment[0].heading() == 270):
            snake_segment[x].goto(last_x_coordinate, last_y_coordinate + 20)
        if(snake_segment[0].heading() == 180):
            snake_segment[x].goto(last_x_coordinate + 20, last_y_coordinate)

        x += 1

    # grow = True
    # if grow == True:
    #
    #     new_turtle = Turtle()
    #     new_turtle.penup()
    #     new_turtle.shape("square")
    #     new_turtle.color("white")
    #     last_x_coordinate = snake1[-1].xcor()
    #     last_y_coordinate = snake1[-1].ycor()
    #     if(snake1[0].heading() == 0):
    #         new_turtle.goto(last_x_coordinate - 10, last_y_coordinate)
    #     if(snake1[0].heading() == 90):
    #         new_turtle.goto(last_x_coordinate, last_y_coordinate - 10)
    #     if(snake1[0].heading() == 270):
    #         new_turtle.goto(last_x_coordinate, last_y_coordinate + 10)
    #     if(snake1[0].heading() == 180):
    #         new_turtle.goto(last_x_coordinate + 10, last_y_coordinate)
    #
    #     snake1.append(new_turtle)
    #     grow = False
    screen1.listen()

# #startGame()
screen1.exitonclick()