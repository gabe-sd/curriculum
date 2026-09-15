# Mouse 2D
# Moving the mouse changes the position and size of each box.

from processing import*

def setup():
  size(640, 360)
  noStroke()  # disables drawing outline
  rectMode(CENTER)  # draw rectangles using (x, y) coords as center instead of corner
  
def draw():
  background(50)
  fill(255, 204)
  rect(mouseX, height/2, mouseY/2+10, mouseY/2+10)
  fill(255, 204)
  inverseX = width - mouseX
  inverseY = height - mouseY
  rect(inverseX, height/2, inverseY/2+10, inverseY/2+10)
  
run()