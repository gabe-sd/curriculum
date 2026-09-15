from processing import*

def setup():
  size(500, 500)
  rectMode(CENTER)
  # textMode(CENTER)

def draw():
  background(0)
  fill(0, 255, 0)
  rect(width-mouseX, height/2 - 100, mouseY, mouseY)
  fill(255, 0, 0)
  rect(mouseX, height/2 + 100, 500 - mouseY, 500 - mouseY)
  text("This is text on the screen", 50, 50)

run()