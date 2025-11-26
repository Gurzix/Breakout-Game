from turtle import Turtle
import random

colors = ['DeepSkyBlue4','goldenrod','red', 'HotPink4','green', 'blue', 'yellow', 'magenta', 'cyan', 'white','orange',
          'pink', 'brown','purple','indigo']

class Brick(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(colors))
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(x,y)

