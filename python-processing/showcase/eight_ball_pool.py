from processing import *
import math
import random
width = 500
height = 500
m = 4
ballDiameter = 2.5*m
radius = ballDiameter/2
pocketDiameter = 4.5*m
ballsPocketed = 0
cuePocketed = False
numberBalls = [1,2,3,4,6,7,8,9,10,12,13,14]
redBalls = []

pocketCoordinates = [[(width-39*m)/2,(height-78*m)/2],
                      [(width-39*m)/2+39*m,(height-78*m)/2],
                      [(width-39*m)/2,(height-78*m)/2+78*m],
                      [(width-39*m)/2+39*m,(height-78*m)/2+78*m],
                      [(width-39*m)/2-pocketDiameter/2,(height-78*m)/2+78*m/2],
                      [(width-39*m)/2+39*m+pocketDiameter/2,(height-78*m)/2+78*m/2]]

def drawTable():
  rect((width-54*m)/2,(height-93*m)/2, 54*m,93*m)
  rect((width-39*m)/2,(height-78*m)/2, 39*m,78*m)
  for coordinate in pocketCoordinates:
    ellipse(coordinate[0],coordinate[1],pocketDiameter, pocketDiameter)

#Define 0  as facing right, pi/2 radians as facing up
class Cue:
  def __init__(self, x, y, angle):
    self.x = x
    self.y = y
    self.angle = angle
    self.length = 25*m
    self.retract = 20
    self.power = 0
  
  def drawCue(self):
    if self.retract > 2*balls[0].radius:
      stroke(255, 255-self.retract*255/80, 0)
    else:
      stroke(0,0,0)
    line(self.x-self.retract*math.cos(self.angle),self.y-self.retract*math.sin(self.angle),self.x-(self.length+self.retract)*math.cos(self.angle),self.y-(self.length+self.retract)*math.sin(self.angle))
    stroke(0, 0, 0)
    
  def changeAngle(self):
    if keyPressed == True:
      if key == ("x"):
        self.angle = math.atan((balls[0].y-mouseY)/(balls[0].x-mouseX+0.0001))
        if balls[0].x-mouseX < 0:
          self.angle = math.pi + self.angle
        if self.angle < 0:
          self.angle += 2*math.pi
      

  
  def chargeCue(self):
    if mousePressed:
      if ((lastMY-mouseY)*math.sin(self.angle)+((lastMX-mouseX)*math.cos(self.angle)))/2+balls[0].radius <= 80:
        self.retract = ((lastMY-mouseY)*math.sin(self.angle)+((lastMX-mouseX)*math.cos(self.angle)))/2+balls[0].radius
      if self.retract < balls[0].radius:
        self.retract = balls[0].radius
      self.power = self.retract-2*balls[0].radius
    
    else:
      if self.retract > balls[0].radius:
        self.retract -= 10
      else:
        self.retract = balls[0].radius
      
  def updateCuePosition(self):
    self.x = balls[0].x
    self.y = balls[0].y
  
  def cueStrikeCheck(self):
    if mousePressed == False and self.retract == balls[0].radius and self.power+2*balls[0].radius > 2*balls[0].radius:
      self.cueHit(balls[0])
    
  def cueHit(self, ball):
    ball.vx = self.power/6*math.cos(self.angle)
    ball.vy = self.power/6*math.sin(self.angle)
    self.power = 0

class Ball:
  def __init__(self, x, y , vx, vy, r, color):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    #self.radius = 2.25*m/2
    self.radius = r
    self.pocketed = False
    self.color = color


  def drawBall(self):
    self.x += self.vx
    self.y += self.vy
    self.vx -= self.vx*0.015
    self.vy -= self.vy*0.015
    if abs(self.vx) < 0.01:
      self.vx = 0
    if abs(self.vy) < 0.01:
      self.vy = 0
    
    if self.color == "black":
      fill(0)
    elif self.color == "white":
      fill(255,255,255)
    elif self.color == "red":
      fill(255,0,0)
    else:
      fill(0,255,0)
    
    ellipse(self.x,self.y,self.radius*2,self.radius*2)
    fill(255)
    
  def checkBallBounceTable(self):
    if self.x + self.radius > (width-39*m)/2+39*m: 
      self.vx *=-1
      self.x = (width-39*m)/2+39*m - self.radius
    elif self.x - self.radius < (width-39*m)/2:
      self.vx *= -1
      self.x = (width-39*m)/2 + self.radius
      
    
    if self.y + self.radius > (height-78*m)/2+78*m:
      self.vy *= -1
      self.y = (height-78*m)/2+78*m - self.radius
    elif self.y - self.radius < (height-78*m)/2:
      self.vy *= -1
      self.y = (height-78*m)/2 + self.radius
      
  def checkPocket(self):
    global ballsPocketed
    global cuePocketed

    nearPocket = False
    for pocket in pocketCoordinates:
      distance = ((self.x-pocket[0])**2 + (self.y-pocket[1])**2) 
      if (distance < (self.radius + pocketDiameter/2)**2):
        self.pocketed = True
        if self != balls[0]:
          self.x = 100
          self.y = 100+self.radius*2*ballsPocketed
          ballsPocketed += 1
        else:
          cuePocketed = True
        self.vx = 0
        self.vy = 0
      if (distance < (self.radius + pocketDiameter/1.5)**2):
        nearPocket = True
    if not nearPocket and not self.pocketed:
      self.checkBallBounceTable()
    
#balls leave collision at 90 degree angle
def checkCollision(ball1, ball2):
  if (ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2 <= (ball1.radius+ball2.radius)**2:
    v1 = (ball1.vx**2 + ball1.vy**2)**(1/2)
    phi1 = math.atan(-(ball1.y-ball2.y)/(ball1.x-ball2.x-0.0001))
    theta1 = math.atan(-ball1.vy/(ball1.vx+0.0001))
    if ball1.x - ball2.x > 0:
      phi1 = math.pi + phi1
    if ball1.vx < 0:
      theta1 = math.pi + theta1
    if theta1 < 0:
      theta1 += 2*math.pi
    if phi1 < 0:
      phi1 += 2*math.pi
    v2f = abs(v1*math.cos(phi1-theta1))
    v1fa = (v1*math.sin(phi1-theta1))

    
    v2 = (ball2.vx**2 + ball2.vy**2)**(1/2)
    phi2 = math.atan(-(ball2.y-ball1.y)/(ball2.x-ball1.x-0.0001))
    theta2 = math.atan(-ball2.vy/(ball2.vx+0.0001))
    if ball2.x - ball1.x > 0:
      phi2 = math.pi + phi2
    if ball2.vx < 0:
      theta2 = math.pi + theta2
    if theta2 < 0:
      theta2 += 2*math.pi
    if phi2 < 0:
      phi2 += 2*math.pi
    v1f = abs(v2*math.cos(phi2-theta2))
    v2fa = (v2*math.sin(phi2-theta2))
    
    
    vx2f = v2f * math.cos(phi1) + v2fa * math.sin(phi2)
    vy2f = (v2f) * -math.sin(phi1) + v2fa * math.cos(phi2)
    vx1f = (v1f) * math.cos(phi2) + v1fa * math.sin(phi1)
    vy1f = (v1f) * -math.sin(phi2) + v1fa * math.cos(phi1)

    ball2.vx = vx2f
    ball2.vy = vy2f
    
    ball1.vx = vx1f
    ball1.vy = vy1f
    
#ball coloring
redBalls.append(11)
for i in range(7):
  picked = 11
  while (picked in redBalls):
    picked = numberBalls[random.randint(0,len(numberBalls) - 1)]
  redBalls.append(picked)

colors = ["white", "green", "green", "green", "green", "black", 
        "green", "green", "green", "green", "green", "green", "green", 
        "green", "green", "green"]
    
for redBall in redBalls:
  colors[redBall] = "red"
  
c = Cue(150, 300, 3*math.pi/2) 

balls = []

#cue ball
balls.append(Ball((width-39*m)/2+39*m/2,(height-78*m)/2+78*3*m/4,0,0,radius,colors[len(balls)]))

    
for i in range(5):
  for k in range(i+1):
    balls.append(Ball((width-39*m)/2+39*m/2-(i/2-k)*(ballDiameter+random.randint(5,15)/100),(height-78*m)/2+78*m/4-i*(ballDiameter-random.randint(5,15)/100),0,0,radius,colors[len(balls)]))


def setup():

  size(width, height)
  background(125,125,125)
  drawTable()
  frameRate(100)
  ellipseMode(CENTER)
  
 
noBallsMoving = True
  
def draw():
  global cuePocketed
  
  background(125,125,125)
  text("Hold 'x' to rotate cue", 20, 20, 50, 50)
  text("Pull cue back and release to shoot", 20, 100, 50, 100)
  text("Press 's' to manually move cue ball", 20, 220, 50, 100)
  drawTable()
  noBallsMoving = True
  
  

      
      
  if cuePocketed:
    balls[0].x = mouseX
    balls[0].y = mouseY
    balls[0].checkBallBounceTable()
    noBallsMoving = False
    
    
  for ball in balls:
    if ball.vx != 0 and ball.vy != 0:
      noBallsMoving = False
  if noBallsMoving == True:
    if keyPressed == True:
      if key == ("s"):
        cuePocketed = True
    c.drawCue()
    c.updateCuePosition()
    c.chargeCue()
    c.cueStrikeCheck()
    c.changeAngle()
  for ball in balls:
    ball.checkPocket()
  for i in range(len(balls)):
    for j in range(len(balls)-i-1):
      checkCollision(balls[i], balls[j+1+i])
  for ball in balls:
    ball.drawBall()

lastMX = 0
lastMY = 0

def mousePressed():
  global cuePocketed
  global lastMY
  global lastMX
  lastMX = mouseX
  lastMY = mouseY
  
  if cuePocketed:
    cuePocketed = False
    balls[0].pocketed = False
    
  
  

run()