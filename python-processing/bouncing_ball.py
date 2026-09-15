from processing import*
import random

x, y = 200, 200
vx = random.uniform(-10, 10)
vy = random.uniform(-10, 10)

def setup():
  size(450, 450)
  fill(0, 0, 200)
  
def draw():
  global x, y, vx, vy
  background(120, 250, 100)
  ellipse(x, y, 25, 25)
  x += vx
  y += vy
  
  if x > width or x < 0:
    vx = vx*-1
    
  if y > height or y < 0:
    vy = vy * -1

run()







