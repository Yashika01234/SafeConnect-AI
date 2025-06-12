from turtle import Turtle

MOVE_DISTANCE = 20

class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("green")
        self.penup()

        self.goto(-250, -250)

    def move_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)