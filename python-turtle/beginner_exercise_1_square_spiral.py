from turtle import*
from random import*

Screen().bgcolor("yellow")

speed(0)

size = randint(50, 100)
loops = randint(5, 30)

for i in range (loops):
  for i in range(4):
    forward(size)
    left(90)
  
  left(360/loops)
  color(randint(0, 255), randint(0, 255), randint(0, 255))