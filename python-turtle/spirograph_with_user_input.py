# 4/19/2022

import turtle

background_color = input("What color would you like the background to be?")
color1 = input("What would you like the first color of the spirographic to be?")
color2 = input("What would you like the second color of the spirographic to be?")


# set background color
turtle.Screen().bgcolor(background_color)

# make a turtle
t = turtle.Turtle()

# set turtle speed to max
t.speed(0)

# make a list of colors so we can alternate the pen color
colors = [color1, color2]

# draw our spirographic
for i in range(400):
  t.forward(i)
  t.right(170) # try changing this number
  
  # alternate colors
  t.pencolor(colors[i%2])