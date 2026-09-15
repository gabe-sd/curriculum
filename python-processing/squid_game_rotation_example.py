from processing import *
import random
#---sprites---#
def char():
  noStroke()
  fill(89, 135, 124)
  ellipse(cx,cy,20,20)
  
def doll():
  noStroke()
  fill(125, 85, 57)
  ellipse(200,40,30,30)

  pushMatrix()
  translate(200,40)
  rotate(r)
  rect(0,0,20,20)
  popMatrix()

def finish():
  stroke(235, 159, 101)
  strokeWeight(2)
  line(0,40,400,40)

def light(red,green,blue):
  fill(red,green,blue)
  ellipse(30,40,30,30)
  translate(0,0)
  
#---movement---#
def ifColor():
  global redTimer, greenTimer, r, color
  
  if color == 'green':
    light(0,255,0)
    greenTimer += 1
    if greenTimer > 250:
      color = 'yellow'
      greenTimer = 0 
    
  elif color == 'yellow':
    light(255,230,0)
    r += 0.025
    if r >= 7.1:
      color = 'red'
  
  elif color == 'red':
    # light color
    light(255,0,0)
    
    # game over
    if keyPressed:
      fill(255,0,0)
      textSize(40)
      text("You lose!!",125,200)
      exit()
    
    # ifRed()
    redTimer += 1
    if redTimer >= 150:
      r -= 0.025
      if r <= 3.95:
        color = 'green'
        redTimer = 0
  
def setup():
  global cx, cy, r, greenTimer, redTimer, color
  
  size(400,400)
  
  cx = 200                  #x,y for character
  cy = 370
  
  r = 3.95                  #r = 7.1
  greenTimer = 0            #the timer for how long the light should be green
  redTimer = 0              #the timer for how long the light should be red
  
  color = 'green'

def draw():
  background(237, 212, 178)
  char()
  finish()
  doll()
    
  ifColor()
  
  if cy <= 40:
    fill(0,255,0)
    textSize(40)
    text("You win!!",125,200)
    exit()

def keyPressed():
  global cy
  if key == CODED:
    if keyCode == UP:
      cy -= 2
    elif keyCode == DOWN:
      cy += 2

run()