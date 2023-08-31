from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(-350)
right_paddle = Paddle(350)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(fun=right_paddle.paddle_up, key="Up")
screen.onkey(fun=right_paddle.paddle_down, key="Down")
screen.onkey(fun=left_paddle.paddle_up, key="w")
screen.onkey(fun=left_paddle.paddle_down, key="s")




game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.ball_move()

    #Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    
    #Detect collision with pedals
    if ball.xcor() > 330 and ball.distance(right_paddle) < 50:
        ball.x_bounce()
        score.score_update("right")


    elif ball.xcor() < (-330) and ball.distance(left_paddle) < 50:
        ball.x_bounce()
        score.score_update("left")


    #Bounding the ball
    if ball.xcor() > 370:
        ball.ball_reset()
        score.score_update(paddle="left")

    if ball.xcor() < -370:
        ball.ball_reset()
        score.score_update(paddle="right")











screen.exitonclick()
