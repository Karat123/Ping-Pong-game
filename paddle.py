from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xcord, 0)

    def create_paddle(self, xcord):
        paddle = Turtle()



    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        if self.ycor() > 250:
            self.goto(self.xcor(), 240)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        if self.ycor() < -250:
            self.goto(self.xcor(), -240)
