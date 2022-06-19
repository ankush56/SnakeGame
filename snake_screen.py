from turtle import Screen

class Snake_screen():


    def __init__(self):
        pass

    def set_screen(self):
        screen1 = Screen()
        screen1.screensize(800, 600)
        screen1.bgcolor("black")
        screen1.title("Snake Game")
        screen1.listen()
        screen1.tracer(0)
        return screen1
