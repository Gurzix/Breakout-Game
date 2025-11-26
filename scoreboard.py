from turtle import Turtle

FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("chartreuse")
        self.hideturtle()
        self.penup()
        self.setposition(-50, 276)
        self.score = 0

        self.write(f"Score: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)


    def game_over(self):
        self.clear()
        self.goto(-200, 276)
        self.color("firebrick1")
        self.write(f"The game is over! Your score was :  {self.score}", align="left", font=FONT)

    def reset_score(self):
        self.clear()
        self.score = 0
        self.goto(-50, 276)
        self.color("chartreuse")
        self.write(f"Score: {self.score}", align="left", font=FONT)

