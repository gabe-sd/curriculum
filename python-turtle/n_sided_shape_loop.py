import turtle
import random

turtle.Screen().bgcolor('green')

def shape(size, num_sides):
  for i in range(num_sides):
    turtle.forward(size)
    turtle.left(360/num_sides)
    
# shape(50, 5)

for i in range(10):
  shape(50, 8)
  turtle.left(36)
