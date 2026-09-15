from processing import*

score = 0

def button(t, ts, x, y, w, h, color):
  """
  t: text
  ts: text size
  x: top left corner x
  y: top left corner y
  w: width
  h: height
  color: button color
  """
  
  fill(color[0], color[1], color[2])
  rectMode(CORNER)
  rect(x, y, w, h)
  fill(0)
  textSize(12)
  textAlign(CENTER, CENTER)
  text(t, x+w/2, y+h/2)
  if mousePressed:
    if mouseX > x and mouseX < x+w and mouseY > y and mouseY < y+h:
      return True
  else:
    return False

def setup():
  size(500, 500)
  
def draw():
  global score, button1
  
  background(100)
  fill(0)
  text(score, 50, 50)
  if button("click me", 18, 200, 250, 100, 50, [255, 0, 0]):
    score += 1
  
  
run()