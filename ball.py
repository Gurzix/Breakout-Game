from turtle import Turtle


STARTING_POSITION = (0, -240)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.y_move = 3
        self.x_move = 3
        self.penup()
        self.goto(STARTING_POSITION)

    def go_right(self):
        self.goto(self.xcor() + 20, self.ycor())
    def go_left(self):
        self.goto(self.xcor() - 20, self.ycor())

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def realistic_bounce(self, player):
        offset = self.xcor() - player.xcor()
        self.x_move = offset / 10
        self.y_move *= -1

    def speed_up(self):
        self.y_move += 2
        self.x_move += 2

    def reset_ball(self):
        self.goto(STARTING_POSITION)
        self.x_move = 3
        self.y_move = 3