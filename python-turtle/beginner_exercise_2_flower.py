from turtle import*
from random import*

speed(0)

# draw stem
color("green")
pensize(3)
penup()
goto(0, -150)
pendown()
setheading(90)
forward(150)


size = randint(20, 50)
num_petals = randint(4, 10)

for i in range (num_petals):
  for i in range(4):
    forward(size)
    left(90)
  
  left(360/num_petals)
  color(randint(0, 255), randint(0, 255), randint(0, 255))