from turtle import *

import bricks
from ball import Ball
from player import Player
from bricks import Brick
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.tracer(0)
screen.title("BREAKOUT GAME")

play_again = False
ball_attached = True
level = 1
position = (0, -280)
score = Scoreboard()
player = Player(position)
ball = Ball()

x = -270
y = 260


def create_bricks_row(start_x, start_y, count, spacing):
    x= start_x
    bricks = []

    for _ in range(count):

        brick = Brick(x,start_y)
        x += spacing
        bricks.append(brick)

    return bricks


def create_bricks_grid(start_x, start_y, rows, cols, spacing_x =60, spacing_y = 30):
    y = start_y
    grid = []

    for _ in range(rows):
        row_bricks = create_bricks_row(start_x, y, cols, spacing_x)
        grid.extend(row_bricks)
        y-= spacing_y
    return grid

wall_of_bricks = create_bricks_grid(x,y,1,10,spacing_x = 60, spacing_y = 20)


screen.listen()

def wait_for_restart():
    global play_again
    message = Turtle()
    message.color("white")
    message.hideturtle()
    score.game_over()
    message.write("Press SPACE to play again", align="center", font=("Courier", 18, "normal"))

    play_again = False
    while not play_again:
        screen.update()

    message.clear()

def restart_game():
    global play_again
    play_again = True

screen.onkey(restart_game, "space")


def game_reset():
    global wall_of_bricks
    ball.reset_ball()
    player.reset_position()
    score.reset_score()

    wall_of_bricks = create_bricks_grid(x,y,1,10,spacing_x = 60, spacing_y = 20)

def move_right():
    player.go_right()
    if ball_attached:
        ball.go_right()

def move_left():
    player.go_left()
    if ball_attached:
        ball.go_left()

def start_ball():
   global ball_attached
   ball_attached = False

screen.onkey(move_right, key= "Right")
screen.onkey(move_left, 'Left')
screen.onkey(start_ball, 'Return')

game_is_on = True
game_is_on = True

while game_is_on:
    screen.update()
    if not ball_attached:
        ball.ball_move()

    # ODBICIE OD ŚCIAN
    if ball.xcor() > 275 or ball.xcor() < -275:
        ball.bounce_x()

    # ODBICIE OD GRACZA
    if ball.distance(player) < 50 and ball.ycor() < -250:
        ball.realistic_bounce(player)

    # ODBICIE OD GÓRY
    if ball.ycor() > 280:
        ball.bounce_y()

    # OGRANICZENIA RUCHU GRACZA
    if player.xcor() < -250:
        player.goto(-250, -280)
    if player.xcor() > 240:
        player.goto(240, -280)

    # PIŁKA SPADŁA NA DÓŁ → RESET
    if ball.ycor() < -270:
        wait_for_restart()
        game_reset()
        ball_attached = True
        continue   # wracamy na początek pętli, NIE wyłączamy gry

    # KOLIZJE Z CEGLAMI
    for brick in wall_of_bricks[:]:
        if ball.distance(brick) < 30:
            brick.hideturtle()
            wall_of_bricks.remove(brick)
            ball.bounce_y()
            score.increase_score()

    # SPRAWDZANIE PRZEJŚCIA POZIOMU
    if len(wall_of_bricks) == 0:
        level += 1
        wall_of_bricks = create_bricks_grid(
            x, y,
            rows = level,
            cols = 10,
            spacing_x = 60,
            spacing_y = 20
        )
        ball.speed_up()
        ball.reset_ball()
        player.reset_position()
        ball_attached = True  # piłka znów startuje z paletką



screen.exitonclick()