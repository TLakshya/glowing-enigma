from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Acrade Game")
a=0.1
screen.tracer(a)

r_paddle= Paddle((350,0))
l_paddle= Paddle((-350,0))
screen.listen()
screen.onkey(r_paddle.goup,"Up")
screen.onkey(r_paddle.godn,"Down")
screen.onkey(l_paddle.goup, "w")
screen.onkey(l_paddle.godn, "s")


sc=Score()
ball=Ball()
game=True

while game:
    time.sleep(0.1)
    if sc.lscore==5 or sc.rscore==5:
        game=False
        sc.win()

    screen.update()
    ball.move()

    if ball.ycor()> 280 or ball.ycor()<-280:
        ball.bounce()


#detect collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor()>310 or ball.distance(l_paddle)<60 and ball.xcor()<-310:
        ball.bouncex()
        a*=0.9

#detect miss of leftpaddle
    if ball.xcor()>380 :
        ball.reset()
        sc.addl()
        a=0.1

    if ball.xcor()<-380:
        ball.reset()
        sc.addr()
        a=0.9





screen.exitonclick()
