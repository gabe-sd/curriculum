from processing import*

rect_x = 0
# player_x = 

def setup():
  size(500, 500)
  rectMode(CENTER)
  

def draw():
  global rect_x
  
  background(99, 42, 161)
  rect(rect_x, 100, 25, 25)
  # rect_x += 3
  if rect_x > 500:
    rect_x = 0
    
def mouseClicked():
  global rect_x
  rect_x += 50

run()