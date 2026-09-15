import turtle
import random

def drawShape():
  sides = random.randint(3, 15)
  size = random.randint(10, 100-3*sides)
  x = random.randint(-100, 100)
  y = random.randint(0, 190)
  
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.color(r, g, b)
  for i in range(sides):
    turtle.forward(size)
    turtle.right(360/sides)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.color(r, g, b)
  turtle.penup()
while True:
  drawShape()