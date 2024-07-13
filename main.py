from turtle import Screen
from paddles import Paddle
from ball import Ball
from scorecard import Scorecard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

ball=Ball()
sc=Scorecard()

game_on=True
rp=Paddle((380,0))
lp=Paddle((-389,0))

screen.onkeypress(rp.up,'Up')
screen.onkeypress(rp.dwn,'Down')

screen.onkeypress(lp.up,'w')
screen.onkeypress(lp.dwn,'s')

while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

    # bounce ball on collision with top or bottom
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.y*=-1
    
    # bounce ball on collision with top or bottom
    if (ball.distance(rp)<45 and ball.xcor()>345) or (ball.distance(lp)<45 and ball.xcor()<-350):
        ball.x*=-1
        ball.ball_speed*=0.9
    
    if ball.xcor()>380:
        ball.reverse()
        sc.l_score()

    if ball.xcor()<-390:
        ball.reverse()
        sc.r +=1
        sc.update_scores()

screen.exitonclick()