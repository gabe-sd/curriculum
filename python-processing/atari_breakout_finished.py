from processing import*
import random as r

bricks_list = []

def setup():
  size(500,500)
  spawn_ball()
  
  for i in range(7): #row
    for j in range(7): #column
      bricks_list.append(Bricks(10 + 70*j, 10 + 30*i))

#Bounce off paddle?
bop = True
  
def draw():
  background(0)
  paddle()
  for brick in bricks_list:
    brick.display()
  ball()
  game_over()

def paddle():
  fill(255)
  rectMode(CENTER)
  rect(mouseX, 470, 60, 10)
  
def ball():
  global bx, by, delta_bx, delta_by, bop
  fill(255)
  bx += delta_bx
  by += delta_by
  ellipse(bx, by, 10, 10)
  #Wall Bounce Physics
  if bx > 490 or bx < 10:
    delta_bx *= -1
  if by < 10:
    delta_by *= -1
  #Paddle Bounce Physics
  if bx >= mouseX - 30 and bx <= mouseX + 30:
    if by >= 470 - 10 and by <= 470 + 10:
      if bop == True: 
        bop = False
        delta_by *= r.uniform(-2,-0.5)
  if by <= 450:
    bop = True
  
def spawn_ball():
  global bx, by, delta_bx, delta_by
  bx = 250
  by = 250
  delta_bx = r.randint(-5,5)
  delta_by = r.randint(3,6)
  
class Bricks: 
  width = 60
  height = 20
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.color = [r.randint(0,255), r.randint(0,255), r.randint(0,255)]
    
  def display(self):
    global bx, by, delta_bx, delta_by
    fill(self.color[0],self.color[1], self.color[2])
    rectMode(CORNER)
    rect(self.x, self.y, Bricks.width, Bricks.height)
    
    #Collision
    if bx + 5 >= self.x and bx - 5 <= self.x + 60:
    #by + 5 >= self.y and by - 5 <= self.y + 20:
      #bricks_list.remove(self)
      if by - 5 <= self.y + 20 and by + 5 >= self.y:
        if bx + 5 <= self.x or bx - 5 >= self.x + 60:
          delta_bx *= r.uniform(-1.5,-0.5)
        if by + 5 >= self.y or by - 5 <= self.y + 20:
          delta_by *= r.uniform(-1.5,-0.5)
        bricks_list.remove(self)

#Game Over
def game_over():
  if by >= 500:
    textSize(40)
    fill(255, 0, 0)
    text("GAME OVER", 120, 250)

run()