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


# This function returns true if every racer has crossed the finish line. Otherwise it returns false.
# This can be written in one line with list comprehension (advanced technique)
def racersFinished():
  # y coorcinate of finish line
  finishY = pen.ycor()
  
  # make a list of all the racers current y coordinate
  racerYList = []
  for racer in racers:
    racerYList.append(racer.ycor())
    
  # get the y coordinate of the last place racer
  lastRacerY = min(racerYList)
  
  # return true if the last place racer has passed the finish line
  # otherwise return false
  if lastRacerY > finishY:
    return True
  else:
    return False
    
    
  # ADVANCED ONE LINER (replaces this function):
  # min(racer.ycor() for racer in racers) < pen.ycor()



###################### Race! This code runs the game
finish_place = []
while not racersFinished(): # loop until everyone passes finish line
  number = 0
  for racer in racers:
    if racer.ycor() < pen.ycor(): # if this racer hasn't passed finish line
      racer.forward(random.randint(0, 10))
    else: # if this racer has passed the finish line
      if not colors[number] in finish_place:
        finish_place.append(colors[number])
    number += 1

# print("race over")
      
# bug fix. While loop doesnt add last place racer to finish_place list
# this for loops adds last place to finisher_place
number = 0
for racer in racers:
  if not colors[number] in finish_place:
    finish_place.append(colors[number])
  number += 1

        
print("Congratulations racers! Here is how you placed:")
print(finish_place)

# Idea to expand on this project: 
# add a counter for how many races each turtle has won. Keep score!
# add more to the race finish screen. Graphics, something more than printing the finish list




