# Processing library documentaion:
# py.processing.org/reference/

from processing import *
import random as r

# set runs once at the beginning of the game 
# (the processing library calls it automatically)
def setup():
  # set screen size to 500x500
  size(500, 500)
  
  # load images into processing and save them as global variables
  global birdImage
  birdImage = loadImage("flappy_bird_right-removebg-preview.png")

# draw runs automatically ~30 times per second
def draw():
  background(112, 166, 219)
  
  # ---BIRD---
  # display bird
  # parameters are: image, x, y, width, height
  image(birdImage, 100, 250, 40, 30)
  # NEXT: make a variable for the bird's y coordinate
  # then code bird flapping keyboard controls and physics
  
  


# calling run tells processing to run the program
# leave this at the end
run()
