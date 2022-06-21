from turtle import Turtle, Screen
import time
from snake import Snake
from snake_screen import Snake_screen
from food import Food
from scoreboard import Scoreboard

SCREEN_SIZE_WIDTH = 600
SCREEN_SIZE_HEIGHT = 600

# Set Play Screen using snake_Screen class.
screen1 = Snake_screen().set_screen(SCREEN_SIZE_WIDTH,SCREEN_SIZE_HEIGHT)

# Turn off animation
screen1.tracer(0)

#Set snake segment- 3 blocks long
snake_segment = Snake()
food = Food()
scoreboard = Scoreboard()

#Set Controls
screen1.onkey(snake_segment.move_up, 'Up')
screen1.onkey(snake_segment.move_left, 'Left')
screen1.onkey(snake_segment.move_down, 'Down')
screen1.onkey(snake_segment.move_right, 'Right')


#Run Snake
# Initializing
run = True

#Turn on screen animation
screen1.update()
time.sleep(1)

scoreboard.update_scoreboard()

while run:
    grow = False
    snake_segment.move()
    screen1.update()
    time.sleep(0.1)

    if snake_segment.head.distance(food) < 15:
        food.refresh()
        snake_segment.grow()
        scoreboard.increase_score()

    # Detect collision with Walls
    if snake_segment.head.xcor() > 280 or snake_segment.head.xcor() < -280 or snake_segment.head.ycor() > 280 or snake_segment.head.ycor() < -280:
        run = False
        scoreboard.game_over()

    collision = snake_segment.check_collision()

    # Detect collision with tail
    if(collision):
        run = False
        scoreboard.game_over()


screen1.listen()
screen1.exitonclick()