from processing import*
import random as r

width = 500
height = 500
num_balls = 3
ball_list = []
score = 0
num_clicks = 0

class Ball:
  def __init__(self):
    self.x = r.randint(0, width)
    self.y = r.randint(0, height)
    self.radius = 25
    
  def display(self):
    fill(200, 0, 0)
    ellipse(self.x, self.y, 2*self.radius, 2*self.radius)
    
  # returns true if mouse is over this ball
  def is_clicked(self):
    if dist(mouseX, mouseY, self.x, self.y) <= self.radius:
      return True
    else:
      return False


def setup():
  size(width, height)
  ellipseMode(CENTER)
  
  for i in range(num_balls):
    new_ball = Ball()
    ball_list.append(new_ball)
  
def draw():
  background(0)
  
  for b in ball_list:
    b.display()
    
  fill(0, 255, 0)
  textSize(20)
  text("Score: {}".format(score), 15, 25)
    
def mouseClicked():
  global score, num_clicks
  
  num_clicks += 1
  hit = False
  for b in ball_list:
    if b.is_clicked():
      hit = True
      score += 1
      ball_list.remove(b)
      ball_list.append(Ball())
      break
  if not hit:
    score -= 1
      
      
  
run()