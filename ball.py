from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x=10
        self.y=10
        self.ball_speed=0.1
        
    def move(self):
        self.goto(self.xcor()+self.x, self.ycor()+self.y)

    def reverse(self):
        self.goto(0,0)
        self.ball_speed=0.1
        self.x*=-1
