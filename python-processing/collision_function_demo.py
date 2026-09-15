from processing import *

# x, y, width, height of each square object 
# (x, y is coordinate of top left corner)
def collision(x1, y1, w1, h1, x2, y2, w2, h2):
  right = x1 <= x2 + w2 # left side of 1 past right side of 2
  left = x1 + w1 >= x2
  top = y1 + h1 >= y2
  bottom = y1 <= y2 + h2
  collided = right and left and top and bottom
  return collided
  
def setup():
  size(500, 500)
  Obstacle(50, 50, 100, 30)
  Obstacle(200, 300, 100, 100)
  
def draw():
  background(0)
  noStroke()
  Obstacle.run()
  Player.display()

  
class Obstacle:
  instances = []
  def __init__(self, x, y, w, h):
    Obstacle.instances.append(self)
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.color = [150, 150, 150]
    
  def display(self):
    fill(self.color[0], self.color[1], self.color[2])
    rect(self.x, self.y, self.w, self.h)
    
  def run():
    for thing in Obstacle.instances:
      thing.display()
  
  
class Player:
  x = 250
  y = 250
  w = 50
  h = 50
  color = [0, 255, 0]
  
  def display():
    fill(Player.color[0], Player.color[1], Player.color[2])
    Player.x, Player.y = mouseX, mouseY
    
    for thing in Obstacle.instances:
      if collision(Player.x, Player.y, Player.w, Player.h,
                   thing.x, thing.y, thing.w, thing.h):
        Player.color = [255, 0, 0]
        break
      else:
        Player.color = [0, 255, 0]
    
    rect(Player.x, Player.y, Player.w, Player.h)
  
run()
