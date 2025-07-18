import turtle
import random

# -------------------- Screen Setup -------------------- #
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# -------------------- Paddle Setup -------------------- #
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)

moving_left = False
moving_right = False

def start_move_left():
    global moving_left
    moving_left = True

def stop_move_left():
    global moving_left
    moving_left = False

def start_move_right():
    global moving_right
    moving_right = True

def stop_move_right():
    global moving_right
    moving_right = False

screen.listen()
screen.onkeypress(start_move_left, "Left")
screen.onkeyrelease(stop_move_left, "Left")
screen.onkeypress(start_move_right, "Right")
screen.onkeyrelease(stop_move_right, "Right")

# -------------------- Ball Setup -------------------- #
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -230)
ball.dx = 5
ball.dy = 5

# -------------------- Brick Setup -------------------- #
bricks = []

def create_bricks():
    colors = ["blue", "green", "orange", "pink", "purple", "yellow"]
    y_start = 250
    for color in colors:
        for x in range(-350, 400, 75):
            brick = turtle.Turtle()
            brick.shape("square")
            brick.color(color)
            brick.shapesize(stretch_wid=1, stretch_len=3)
            brick.penup()
            brick.goto(x, y_start)
            bricks.append(brick)
        y_start -= 30

create_bricks()

# -------------------- Scoreboard -------------------- #
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")
score_display.goto(-370, 260)
score_display.write(f"Score: {score}", align="left", font=("Courier", 16, "normal"))

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="left", font=("Courier", 16, "normal"))

# -------------------- Game Over Display -------------------- #
game_over = turtle.Turtle()
game_over.hideturtle()
game_over.color("white")
game_over.penup()

# -------------------- Game State -------------------- #
game_on = True

# -------------------- Main Game Loop -------------------- #
def game_loop():
    global game_on, score

    if not game_on:
        return

    screen.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Move paddle
    if moving_left and paddle.xcor() > -350:
        paddle.setx(paddle.xcor() - 6)
    if moving_right and paddle.xcor() < 350:
        paddle.setx(paddle.xcor() + 6)

    # Wall collision
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1

    # Paddle collision
    if ball.ycor() < -240 and paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60:
        ball.dy *= -1

    # Ball falls below = Game Over
    if ball.ycor() < -290:
        ball.goto(0, -230)
        paddle.goto(0, -250)
        ball.dy *= -1
        game_over.goto(0, 0)
        game_over.write("Game Over", align="center", font=("Courier", 24, "bold"))
        game_on = False
        return

    # Brick collision
    for brick in bricks:
        if brick.distance(ball) < 35:
            ball.dy *= -1
            brick.goto(1000, 1000)
            bricks.remove(brick)
            score += 1
            update_score()
            break

    # If no bricks are left
    if len(bricks) == 0:
        ball.goto(0, -230)
        paddle.goto(0, -250)
        ball.dy *= -1
        game_over.goto(0, 0)
        game_over.write("You have won!", align="center", font=("Courier", 24, "bold"))
        game_on = False
        return

    # Continue game
    screen.ontimer(game_loop, 10)

# -------------------- Restart Logic -------------------- #
def restart_game(x=None, y=None):
    global score, game_on, moving_left, moving_right

    # Reset game state
    score = 0
    update_score()
    moving_left = False
    moving_right = False
    ball.goto(0, -230)
    paddle.goto(0, -250)
    ball.dx = 5
    ball.dy = 5

    # Clear and recreate bricks
    for b in bricks:
        b.goto(1000, 1000)
    bricks.clear()
    create_bricks()

    # Clear Game Over message
    game_over.clear()

    # Resume game
    game_on = True
    game_loop()  # Restart the loop

# -------------------- Restart Button -------------------- #
restart_btn = turtle.Turtle()
restart_btn.hideturtle()
restart_btn.penup()
restart_btn.goto(200, 270)
restart_btn.color("white")
restart_btn.write("Restart", align="center", font=("Courier", 14, "normal"))
restart_btn.shape("square")
restart_btn.shapesize(stretch_wid=1, stretch_len=5)
restart_btn.goto(300, 280)
restart_btn.showturtle()
restart_btn.onclick(restart_game)

# -------------------- Start Game -------------------- #
game_loop()
screen.mainloop()
