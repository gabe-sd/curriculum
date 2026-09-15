from processing import*
import random


def generateStars():  

  for i in range(300):
    x = random.randint(0, width)
    y = random.randint(0, height)
    starlocations.append((x, y))
    
def displayStars():
  for x, y in starlocations:
    ellipse(x, y, 2, 2)

def setup():
  global starlocations, angle
  global earth_x, earth_y
  global moon_x, moon_y
  size(600, 600)
  earth_x = 200
  earth_y = 0
  moon_x = 50
  moon_y = 0
  angle = 0
  starlocations = []
  generateStars()
  noStroke()  # disables drawing outline
  
  
def draw():
  global angle
  background(0)  # grayscale instead of rgb
  fill(150, 175, 255)  # star color
  displayStars()
  
  
  translate(300, 300)
  
  # SUN
  fill(250,250,0)  # set color
  ellipse(0,0,100,100)  # draw circle
  
  # EARTH
  rotate(angle)
  fill(0, 240, 50)  # set color
  ellipse(earth_x, earth_y, 40, 40)  # draw circle
  
  # MOON
  translate(earth_x, earth_y)
  rotate(angle*-2)
  fill(100, 100, 100)
  ellipse(moon_x, moon_y, 15, 15)
  
  angle += 0.02
  

run()








































