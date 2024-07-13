from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.speed('fastest')
        self.color("white")
        self.shapesize(5,0.75, None)
        self.setpos(position)

    def up(self):
        self.goto(self.xcor(),self.ycor()+20)

    def dwn(self):
        self.goto(self.xcor(),self.ycor()-20)