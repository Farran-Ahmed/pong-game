#pong_game
import turtle 
import winsound
wn = turtle.Screen()
wn.title("pong by yellow")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#scoreboard
score_a = 0
score_b = 0 

#block A
block_a = turtle.Turtle()
block_a.speed(0)
block_a.shape("square")
block_a.color("white")
block_a.shapesize(stretch_wid=5, stretch_len=1)
block_a.penup()
block_a.goto(-350, 0)
#block B
block_b = turtle.Turtle()
block_b.speed(0)
block_b.shape("square")
block_b.color("white")
block_b.shapesize(stretch_wid=5, stretch_len=1)
block_b.penup()
block_b.goto(+350, 0)
#ball 
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = -.2

# pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="Center", font=("Courtier", 18, "normal"))


#function 
def block_a_up():
    y = block_a.ycor()
    y += 20
    block_a.sety(y)

def block_a_down():
    y = block_a.ycor()
    y -= 20
    block_a.sety(y)
#block b
def block_b_up():
    y = block_b.ycor()
    y += 20
    block_b.sety(y)

def block_b_down():
    y = block_b.ycor()
    y -= 20
    block_b.sety(y)
#keybord bind
wn.listen()
wn.onkeypress(block_a_up, "w")
wn.onkeypress(block_a_down, "s")
wn.onkeypress(block_b_up, "Up")
wn.onkeypress(block_b_down, "Down")

#main loop
while True:
    wn.update()

    #moveing the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border bounce 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="Center", font=("Courtier", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="Center", font=("Courtier", 18, "normal"))

    
    #block and ball hits
    if (ball.xcor() > 340 and ball.xcor() < 350 )and (ball.ycor() < block_b.ycor() + 40 and ball.ycor() > block_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 

    if (ball.xcor() < -340 and ball.xcor() > -350 )and (ball.ycor() < block_a.ycor() + 40 and ball.ycor() > block_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 