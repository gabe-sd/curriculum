from processing import *
import random as r
  


class Ball:
  clones = []
  
  # init means initialize (setup)
  def __init__(self, x, y, infected):
    self.x = x
    self.y = y
    self.infected = infected
    
    self.radius = random(1, 5)
    self.vx = random(-1, 1)
    self.vy = random(-1, 1)
    
    # add this new ball to the clones list
    Ball.clones.append(self)
  
  def main(self):
    # for each clone
    
      # move
    self.x += self.vx
    self.y += self.vy

    self.checkBounceEdge()
    self.checkCollision()
      # display
    if self.infected:
      fill(255, 0, 0)
    else:
      fill(255)
    ellipse(self.x, self.y, self.radius, self.radius)
  
  def checkBounceEdge(self):
    if self.x + self.radius >= width or self.x - self.radius <= 0:
      self.vx *= -1
    if self.y + self.radius >= height or self.y - self.radius <= 0:
      self.vy *= -1
  
  def checkCollision(self):
    if self.infected == True:
      for ball in ballList:
        if ball.infected == False:
          distance = dist(self.x, self.y, ball.x, ball.y)
          if distance < self.radius:
            ball.infected = True
            
def setup():
  global ballList, redCount
  size(400, 300)
  ellipseMode(RADIUS)
  ballList = []
  ballList.append(Ball(random(0, width), random(0, height), True))
  for i in range(255):
    ball = Ball(random(0, width), random(0, height), False)
    ballList.append(ball)
    
def draw():
  global ballList, redCount
  background(0, 100, 250)
  redCount = 1
  for i in range(len(ballList)):
    ballList[i].main()
  for ball in ballList:
    if ball.infected:
      redCount += 1
  text("redCount: " + str(redCount), width / 2, height / 2)
run()