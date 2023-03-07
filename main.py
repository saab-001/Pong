import time
from turtle import Screen
from screen_designer import ScreenMaker
from scoreboard import ScoreBoard
from pong_ball import PongBall
from paddles import Paddles, PAD_YCOR, XCOR
SCREEN_COLOR = "black"

screen = Screen()
screen.setup(1100, 700)
screen.title("PONG")
screen.colormode(255)
screen.bgcolor(SCREEN_COLOR)
screen.tracer(0)

player1 = screen.textinput("Player Name", "\t controls: up/down \n\tSide: Right\nName of Player1:")
player2 = screen.textinput("Player Name", "\t controls: W/S \n\tSide: Left\nName of Player2:")

if player1 == "None":
    player1 = "Player1"
if player2 == "none":
    player2 = "Player2"

screen.listen()

screen_design = ScreenMaker()
score_maintainer = ScoreBoard()
paddles = Paddles()
pong_ball = PongBall()

screen.onkey(paddles.p1_move_up, "Up")
screen.onkey(paddles.p1_move_down, "Down")
screen.onkey(paddles.p2_move_up, "w")
screen.onkey(paddles.p2_move_down, "s")

screen.update()
time.sleep(1)
game_is_on = True
while game_is_on:
    game_pace = pong_ball.move_speed/2000
    screen.update()
    time.sleep(game_pace)
    score_maintainer.show_score()
    pong_ball.move()
    if pong_ball.distance(paddles.p1) < 10 or (pong_ball.xcor() > 500 and pong_ball.distance(paddles.p1) < 65):
        pong_ball.bounce_p1()
    elif pong_ball.distance(paddles.p2) < 10 or (pong_ball.xcor() < -500 and pong_ball.distance(paddles.p2) < 65):
        pong_ball.bounce_p2()
    if pong_ball.ycor() > 205 or pong_ball.ycor() < -285:
        pong_ball.wall_bounce()
    if pong_ball.xcor() < -525:
        score_maintainer.score_add_p1()
        pong_ball.start()
        screen.update()
        time.sleep(3)
    elif pong_ball.xcor() > 525:
        score_maintainer.score_add_p2()
        pong_ball.start()
        screen.update()
        time.sleep(3)

    if score_maintainer.score_p2 == 3 or score_maintainer.score_p1 == 3:
        game_is_on = False

pong_ball.hideturtle()
paddles.p1.goto(XCOR, PAD_YCOR)
paddles.p2.goto(-XCOR, PAD_YCOR)
score_maintainer.game_over(player1, player2)
screen.update()
screen.exitonclick()
