import turtle
import random

background_color = input("Enter a background color: ")
turtle.Screen().bgcolor(background_color)

angle = int(input("Enter an angle: "))

turtle.speed(10)
length = 1
for i in range(400):
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  turtle.color(r, g, b)
  
  turtle.forward(length)
  turtle.right(angle)
  length += 1
  