from turtle import Turtle

class Maze(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("gold")
        self.penup()

        self.goto(250, 250)