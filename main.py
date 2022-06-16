from turtle import Turtle, Screen

screen1 = Screen()
screen1.screensize(1000,1000)
screen1.bgcolor("black")
screen1.title("Snake Game")


#create 3 boxes long snake
def createSnake():
    x_coordinate = 0
    y_coordinate = 0
    for _ in range(0,3):
        snake1 = []
        turtle1 = Turtle()
        turtle1.shape("square")
        turtle1.color("white")
        turtle1.goto(x_coordinate,y_coordinate)
        snake1.append(turtle1)
        x_coordinate = x_coordinate - 20

createSnake()
screen1.exitonclick()