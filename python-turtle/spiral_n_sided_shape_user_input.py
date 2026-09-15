import turtle
import random

background_color = input("What color would you like the background to be?")
shape_color = input("What color would you like the shape to be?")
num_sides = int(input("How many sides would you like your shape to have?"))
size = int(input("How big would you like your shape to be?"))
num_shapes = int(input("How many shapes would you like to draw in your spiral?"))

turtle.speed(0)
turtle.Screen().bgcolor(background_color)
turtle.pencolor(shape_color)

def shape(size, num_sides):
  for i in range(num_sides):
    turtle.forward(size)
    turtle.left(360/num_sides)
    
# shape(50, 5)

for i in range(num_shapes):
  shape(size, num_sides)
  turtle.left(360/num_shapes)
