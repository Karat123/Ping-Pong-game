from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(45)
        self.ball_speed = 0.1

    def ball_move(self):
        self.forward(10)

    def y_bounce(self):
        self.setheading(-self.heading())


    def x_bounce(self):
        self.setheading(180 - self.heading())
        self.ball_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.x_bounce()
