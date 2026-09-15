'''
Author: Gabriel Venditti
Date: 3/28/2022
'''

# imports
import turtle
import random
import time

# change background color
turtle.Screen().bgcolor("black")

# Draw finish line
pen = turtle.Turtle()
pen.penup()
pen.goto(-200,150)
pen.pendown()
pen.forward(400)


# create racers list
racer_list = []

# make list of colors and names for racers (make sure you have enough for each racer)
colors = ["red", "blue", "green", "brown", "orange", "black"]

# racer setup
for i in range(len(colors)):
  # create a racer
  racer = turtle.Turtle()
  
  # add the racer to our racers list
  racer_list.append(racer)
  
  # set racer color, name, and shape
  racer.color(colors[i])
  racer.name = colors[i]
  racer.shape("turtle")
  
  
  # line up racers
  racer.penup()
  racer.goto(-100 + 25*i, -100)
  racer.setheading(90)

# starting dialogue
print("Alright folks, from left to right we have: ")
print(colors)
time.sleep(2)
print("\nReady racers?")
time.sleep(1)
print("On your mark")
time.sleep(1)
print("Get set")
time.sleep(1)
print("Go!")


######### Race! This code runs the game ##########
finish_place = []
while True: # loop until everyone passes finish line
  for i in range(len(racer_list)):
    racer = racer_list[i]
    if racer.ycor() < pen.ycor(): # if this racer hasn't passed finish line
      racer.forward(random.randint(0, 10))
    else: # if this racer has passed the finish line
      if racer.name not in finish_place:
        finish_place.append(racer.name)
        
  if len(racer_list) == len(finish_place):
    break

        
print("\nCongratulations racers! Here is how you placed:")
print(finish_place)






# Idea to expand on this project: 
# add a counter for how many races each turtle has won. Keep score!
# add more to the race finish screen. Graphics, something more than printing the finish list

