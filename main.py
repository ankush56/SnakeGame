from turtle import Turtle, Screen
import time
from snake import Snake
from snake_screen import Snake_screen
from food import Food

SCREEN_SIZE_WIDTH = 1000
SCREEN_SIZE_HEIGHT = 1000
# Set Play Screen using snake_Screen class.
screen1 = Snake_screen().set_screen(SCREEN_SIZE_WIDTH,SCREEN_SIZE_HEIGHT)

#Set snake segment- 3 blocks long
snake_segment = Snake()
food = Food()

#Set Controls
screen1.onkey(snake_segment.move_up, 'Up')
screen1.onkey(snake_segment.move_left, 'Left')
screen1.onkey(snake_segment.move_down, 'Down')
screen1.onkey(snake_segment.move_right, 'Right')


#Run Snake
# Initializing
run = True
screen1.update()
time.sleep(1)
screen1.tracer(0)

while run:
    grow = False
    screen1.update()
    snake_segment.move()
    if snake_segment.head.distance(food) < 15:
        food.refresh()
        snake_segment.grow()
    screen1.listen()

    if snake_segment.head.xcor() > SCREEN_SIZE_WIDTH/2 -20 or snake_segment.head.xcor() < -SCREEN_SIZE_WIDTH/2 + 10:
        run = False

    if snake_segment.head.ycor() > SCREEN_SIZE_HEIGHT/2 -20 or snake_segment.head.ycor() < -SCREEN_SIZE_HEIGHT/2 + 10:
        run = False

# #startGame()
screen1.exitonclick()