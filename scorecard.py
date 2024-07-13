from turtle import Turtle
FONT=('Courier',60,'normal')

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l=0
        self.r=0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(-150,220)
        self.write(self.l, align='center', font=FONT)
        self.goto(150,220)
        self.write(self.r, align='center', font=FONT)
    
    def l_score(self):
        self.l +=1
        self.update_scores()