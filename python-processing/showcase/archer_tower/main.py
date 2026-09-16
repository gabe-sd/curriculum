from processing import *

def setup():
  size(500, 500)
  
  global archerImage, towerImage, arrowImage, goblinImage
  archerImage = loadImage("archer(1).png")
  arrowImage = loadImage("arrow.png")
  towerImage = loadImage("tower.png")
  goblinImage = loadImage("2D_GOBLIN__Run_000.png")
  
def draw():
  background(135, 206, 235)
  
  # ground
  fill(124, 252, 0)
  noStroke()
  rect(0, 450, 500, 100)
  
  # tower & archer
  image(archerImage, 28, 330, 25, 25)
  image(towerImage, 10, 345, 50, 120)
  
  Enemy.run()
  Arrow.run()
  
def mouseClicked():
  Arrow()
  
class Enemy:
  instances = []
  
  def __init__(self):
    Enemy.instances.append(self)
    
    self.x = 550
    self.y = 430
    self.w = 35
    self.h = 35
    
    self.speed = -0.5
    
  def draw(self):
    # movement
    if self.x > 55:
      self.x += self.speed
    
    # display
    image(goblinImage, self.x, self.y, self.w, self.h)
    
  def run():
    # draw all enemies
    for goblin in Enemy.instances:
      goblin.draw()
      
    # spawn new enemies
    if frameCount%90==0:
      Enemy()
      
class Arrow:
  instances = []
  
  def __init__(self):
    Arrow.instances.append(self)
    
    self.x = 100
    self.y = 430
    self.w = 35
    self.h = 35
    
    self.speed = 2
    
    # math to make the arrows arrow
    d = dist(self.x, self.y, mouseX, mouseY)
    self.vx = (mouseX - self.x)/d * self.speed
    self.vy = (mouseY - self.y)/d * self.speed
    
  def draw(self):
    # move
    self.x += self.vx
    self.y += self.vy
    
    # display
    image(arrowImage, self.x, self.y, self.w, self.h)
    
    # self delete if off screen
    if self.x > 600 or self.x < -100 or self.y < -100 or self.y > 600:
      Arrow.instances.remove(self)
      
  def run():
    for dart in Arrow.instances:
      dart.draw()
    
    
    
  
    

  
run()