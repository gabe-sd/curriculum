import random as r
from processing import*
import time

streak = 0
playerChoice = None
botChoice = None
scoreTallied = False
framesSinceTallied = 0

def button(img, x, y):
  global playerChoice
  
  image(img, x, y, 100, 100)
  
  # click detection
  left=x
  right=x+100
  top=y
  bottom=y+100
  if mousePressed and playerChoice == None:
    if mouseX>left and mouseX<right and mouseY>top and mouseY<bottom:
      playerChoice = img
      
def botTurn():
  global botChoice
  
  if botChoice == None:
    botChoice = r.choice([rock_img, paper_img, scissors_img])

def setup():
  global rock_img, paper_img, scissors_img
  
  size(500, 500)
  
  rock_img = loadImage("turtle.png")
  paper_img = loadImage("cactus.png")
  scissors_img = loadImage("dino (3).png")
  
def draw():
  global streak, playerChoice, botChoice, scoreTallied, framesSinceTallied
  
  background(3, 152, 252)
  
  # streak
  textSize(30)
  text("STREAK: {}".format(streak), 180, 50, 400, 50)
  
  # bottom UI buttons
  button(rock_img, 50, 300)
  button(paper_img, 210, 300)
  button(scissors_img, 350, 300)
  
  # bot turn
  botTurn()
  
  # battle window
  noFill()
  rect(50, 80, 400, 180)
  if playerChoice != None:
    image(playerChoice, 70, 100, 100, 100)
    if botChoice != None:
      image(botChoice, 325, 100, 100, 100)
      
  # streak logic
  if playerChoice!=None and botChoice!=None and scoreTallied==False:
    if playerChoice==rock_img and botChoice==scissors_img:
      streak += 1
    if playerChoice==rock_img and botChoice==paper_img:
      streak = 0
    if playerChoice==paper_img and botChoice==scissors_img:
      streak = 0
    if playerChoice==paper_img and botChoice==rock_img:
      streak += 1
    if playerChoice==scissors_img and botChoice==rock_img:
      streak = 0
    if playerChoice==scissors_img and botChoice==paper_img:
      streak += 1
    scoreTallied=True
    
  if scoreTallied:
    framesSinceTallied += 1
    
    if framesSinceTallied>30:
      # reset
      scoreTallied=False
      framesSinceTallied=0
      playerChoice=None
      botChoice=None
    
  
run()