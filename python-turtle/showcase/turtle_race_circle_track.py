from turtle import *
from random import randint

# Track Construction
track = Turtle()
track.penup()
track.hideturtle()
track.speed(0)

# outer track
track.goto(0,  -260)
track.pendown()
track.color("white")
track.begin_fill()
track.circle(270) 
track.end_fill()

# inner glass
track.penup()
track.goto(0, -100)
track.pendown()
track.color("black")
track.begin_fill()
track.circle(110)
track.end_fill()

# Finish line 
track.right(90)
track.forward(160)
track.penup()

# t1 (lane1 racer )
t1 = Turtle()
t1.color("magenta") 
t1.shape("turtle")
t1.penup()
t1.goto(0, -120)
t1.pendown()

#t2 (lane2 racer)
t2 = Turtle()
t2.color("dodger blue ")
t2.shape("turtle")
t2.penup()
t2.goto(0, -160)
t2.pendown()

#t3 (lane3 racer)
t3 = Turtle()
t3.color("hot pink")
t3.shape ("turtle")
t3.penup()
t3.goto(0, -200)
t3.pendown()

# Race time
for i in range(118):
  t1.circle(130 , randint(1,5))
  t2.circle(170 , randint(1,5))
  t3.circle(210 , randint(1,5))