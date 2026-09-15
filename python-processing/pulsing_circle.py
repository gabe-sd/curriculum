from processing import *

s = 60
s2 = 0
growth_rate = 5


def setup():
  size(500,500)
  frameRate(30)
  background(0)
    
def draw():
  global s, growth_rate, s2

  fill(200, abs(255-frameCount%510), 0, abs(255-frameCount%510))

  if mousePressed:
    s += growth_rate
    s2 += growth_rate
  
    if s > 85:
      growth_rate = -5
    
    if s < 5:
      growth_rate = 5
    
    ellipse(mouseX, mouseY, s2, s)
    
  

run()