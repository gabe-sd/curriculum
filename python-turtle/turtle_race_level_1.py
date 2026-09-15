'''
Author: Gabriel Venditti
Date: 3/1/2022
'''

import turtle
import random

# Draw finish line
pen = turtle.Turtle()
pen.penup()
pen.goto(-200,150)
pen.pendown()
pen.forward(400)

# create racers list
racers = []

# create racers and add them to the racer list
# (can also make this list manually after creating the racers)
racer1 = turtle.Turtle()
racers.append(racer1)

racer2 = turtle.Turtle()
racers.append(racer2)

racer3 = turtle.Turtle()
racers.append(racer3)

racer4 = turtle.Turtle()
racers.append(racer4)

racer5 = turtle.Turtle()
racers.append(racer5)

# make list of colors for racers (at least as many colors as racers, too many is okay)
colors = ["red", "blue", "green", "brown", "orange", "black"]

# racer setup
number = 0
for racer in racers:
  racer.penup()
  racer.shape("turtle")
  racer.color(colors[number]) 
  racer.goto(-100 + number*25, -100)
  racer.setheading(90)
  number += 1

# Race!
finish_place = []
while max(racer.ycor() for racer in racers) < pen.ycor(): # until a racer passes the finish line
  for racer in racers:
    racer.forward(random.randint(0, 10))
        

# See advanced turtle race for ideas on how to expand on this 
