from turtle import Turtle, Screen
import time

screen1 = Screen()
screen1.screensize(1000,1000)
screen1.bgcolor("black")
screen1.title("Snake Game")
screen1.listen()

snake1 = []
#create 3 boxes long snake

x_coordinate = 0
y_coordinate = 0


# Controls
def move_up():
    snake1[0].setheading(90)

def move_left():
    snake1[0].setheading(180)

def move_down():
    snake1[0].setheading(270)

def move_right():
    snake1[0].setheading(0)



for _ in range(0,4):
#Creating 3 units snake
    turtle1 = Turtle()
    turtle1.shape("square")
    turtle1.color("white")
    turtle1.penup()
    turtle1.goto(x_coordinate,y_coordinate)
    snake1.append(turtle1)
    x_coordinate = x_coordinate - 10

#Run Snake
run = True
while run:
    x = 1
    curr_position = snake1[0].pos()
    snake1[0].forward(4)
    while x < len(snake1):
        snake1[x].goto(curr_position)
        x += 1
        screen1.onkey(move_up, 'Up')
        screen1.onkey(move_left, 'Left')
        screen1.onkey(move_down, 'Down')
        screen1.onkey(move_right, 'Right')
        screen1.listen()

# #startGame()
screen1.exitonclick()