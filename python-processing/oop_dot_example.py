from processing import*

class Dot:
  members = []
  
  def __init__(self):
    Dot.members.append(self)
    self.x = random(0, 400)
    self.y = random(0, 400)
    self.vx = random(-7, 7)
    self.vy = random(-7, 7)
    
  def display(self):
    # bounce
    if self.x < 0 or self.x>400:
      self.vx *= -1
    if self.y < 0 or self.y > 400:
      self.vy *= -1
      
    # move
    self.x += self.vx
    self.y += self.vy
    
    # display
    fill(255, 0, 0)
    ellipse(self.x, self.y, 10, 10)

def setup():
  size(400, 400)
  
def draw():
  background(0)
  
  for d in Dot.members:
    d.display()
    
  if frameCount%5==0:
    Dot()
  
run()