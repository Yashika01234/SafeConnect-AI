from turtle import Screen, Turtle
from player import Player
from maze import Maze

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("white")
screen.title("Maze Escape Game")

player = Player()
goal = Maze()

screen.listen()

screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

game_on = True

while game_on:
    screen.update()

    if player.distance(goal) < 20:
        winner = Turtle()
        winner.hideturtle()
        winner.penup()
        winner.goto(0, 0)
        winner.write(
            "🎉 YOU ESCAPED THE MAZE! 🎉",
            align="center",
            font=("Arial", 18, "bold")
        )
        game_on = False

screen.mainloop()
