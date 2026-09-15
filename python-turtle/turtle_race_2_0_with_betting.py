'''
Author: Gabriel Venditti
Date: 3/28/2022
'''

# imports
import turtle
import random
import time

# Draw finish line
pen = turtle.Turtle()
pen.penup()
pen.goto(-200,150)
pen.pendown()
pen.forward(400)
# b=pen.bgcolor("red)")

# create racers list
racer_list = []

# make list of colors and names for racers (make sure you have enough for each racer)
colors = ["red", "blue", "green", "brown", "orange", "black"]
names = ['jim', 'jeff', 'jan', 'john', 'jamie']  # get creative here!

# racer setup
for i in range(5):
  # create a racer
  racer = turtle.Turtle()
  
  # add the racer to our racers list
  racer_list.append(racer)
  
  # set racer color, name, and shape
  racer.color(colors[i])
  racer.name = names[i]
  racer.shape("turtle")
  
  
  # line up racers
  racer.penup()
  racer.goto(-100 + 25*i, -100)
  racer.setheading(90)


def race():
  for i in range(len(racer_list)):
    racer = racer_list[i]
    racer.goto(-100 + 25*i, -100)
  
  # starting dialogue
  print("Alright folks, from left to right we have: ")
  print(names)
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
  return finish_place
  
  
game_running = True
coins = 1000

# intro dialogue
print("Welcome to the Turtle Races")
time.sleep(1)


while game_running:
  print("You have {} coins to bet with, or feel free to just watch and enjoy the races!\n".format(coins))
  time.sleep(1)
  answer = input("Would like to place a bet on the next race? [y/n]")
  
  if answer == 'y':
    print('From left to right we have: {}'.format(str(names)))
    time.sleep(1)
    print("Who would you like to bet on? Racer 1 is on the left, racer {} is on the right.".format(str(len(racer_list))))
    bet_racer = int(input("Enter a racer number 1 - {}: ".format(str(len(racer_list)))))
    bet_amount = int(input("How much would you like to bet?: "))
    if bet_amount not in range(coins + 1):
      print("You don't have that much!")
      bet_amount = 1
    
    time.sleep(1)
    print("OK. You've bet {} coins on racer #{}".format(bet_amount, bet_racer))
    time.sleep(1)
    print("The race is starting!\n")
    finishers = race()
    
    if finishers[0] == finishers[bet_racer - 1]:
      print("Wow what a bet! You won {} coins".format(str(bet_amount)))
      coins += bet_amount
    else:
      print("Oh no! The racer you bet on didn't win. Better luck next time.")
      coins -= bet_amount
      
  else:
    race()
    
  time.sleep(1)
  answer = input("\nWould you like to see another race? [y/n]")
  if answer == 'n':
    game_running = False
    print("See you next time!")





# Idea to expand on this project: 
# add a counter for how many races each turtle has won. Keep score!
# add more to the race finish screen. Graphics, something more than printing the finish list

