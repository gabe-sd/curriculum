from processing import*
import random as r

groundy = 345
dx = 30
dy = 300
dvy = 0
dw = 50
dh = 50
jumpForce = 17
gravityForce = 1.75
score = 0



def setup():
  global dino_img, cactus1_img
  
  size(960, 540)
  dino_img = loadImage("dino (3).png")
  cactus1_img = loadImage("cactus.png")
  
def draw():
  global dy, dvy
  
  background(255)
  
  # display score
  score = frameCount//6
  textSize(12)
  text("Score: {}".format(score), 20, 20)
  
  
  # draw ground
  fill(0)
  rect(-10, groundy-12, width + 10, 0)
  
  # dino movement and display
  dy += dvy
  image(dino_img, dx, dy, dw, dh)
  
  # gravity
  if not dinoGrounded():
    dvy += gravityForce
  else:
    dvy = 0
    
  # display all obstacles every frame
  for thing in Obstacle.o_list:
    thing.display()
    
  # spawn obstacles
  if frameCount%100==0:
    r.choice([spawn2, spawn3])()
  
def keyPressed():
  global dvy
  if key == CODED:
    if keyCode == UP:
      if dvy == 0 and dinoGrounded():
        dvy -= jumpForce
        
        
def dinoGrounded():
  global dy
  if dy + dh >= groundy:
    dy = groundy - dh  # bring dino to ground if he's below
    return True
  else:
    return False

class Obstacle:
  o_list = []
  vx = -7
  def __init__(self, model, x):
    Obstacle.o_list.append(self)
    
    if model == "cactus1":
      self.img = cactus1_img
      self.x = x
      self.y = groundy-55
      self.w = 50
      self.h = 50
    
    
  def display(self):
    self.x += Obstacle.vx
    image(self.img, self.x, self.y, self.w, self.h)
    
    # delete when off screen
    if self.x < -100:
      Obstacle.o_list.remove(self)
    
    # collision detection
    dright = dx+dw-30
    dleft = dx+20
    dtop = dy+20
    dbottom = dy+dh-15
    oright = self.x+self.w
    oleft = self.x
    otop = self.y
    obottom = self.y+self.h
    
    # if true, dino collided
    if oleft<dright and oright>dleft and dbottom>otop and dtop<obottom:
      gameover()
    
def spawn2():
  Obstacle("cactus1", 1000)
  Obstacle("cactus1", 1150)
  
def spawn3():
  Obstacle("cactus1", 1000)
  Obstacle("cactus1", 1200)
  Obstacle("cactus1", 1350)
  
def gameover():
  textSize(30)
  text("GAME OVER", 400, 250)
  exit()
  
run()