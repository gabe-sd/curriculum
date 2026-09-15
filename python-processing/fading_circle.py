from processing import*

def setup():
  size(400, 400)
  
def draw():
  background(0)
  noStroke()
  fill(50, 100, 200, 255-frameCount*3%255)
  ellipse(200, 200, 50, 50)
  
run()