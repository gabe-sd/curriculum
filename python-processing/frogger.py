from processing import *

def car1():
  fill(0,0,0)
  ellipse(car1x + 45,car1y + 32,15,15)
  ellipse(car1x + 45,car1y,15,15)
  ellipse(car1x + 5,car1y,15,15)
  ellipse(car1x + 5,car1y + 32,15,15)
  fill(0,100,50)
  rect(car1x,car1y,50,30)
  
def car2():
  fill(0,0,0)
  ellipse(car2x + 45,car2y + 32,15,15)
  ellipse(car2x + 45,car2y,15,15)
  ellipse(car2x + 5,car2y,15,15)
  ellipse(car2x + 5,car2y + 32,15,15)
  fill(0,100,50)
  rect(car2x,car2y,50,30)
  
  
def car3():
  fill(0,0,0)
  ellipse(car3x + 45,car3y + 32,15,15)
  ellipse(car3x + 45,car3y,15,15)
  ellipse(car3x + 5,car3y,15,15)
  ellipse(car3x + 5,car3y + 32,15,15)
  fill(0,100,50)
  rect(car3x,car3y,50,30)
  


def roads():
  fill(50,50,50)
  rect(0,50,400,60)
  rect(0,150,400,60)
  rect(0,250,400,60)






def frog():
  stroke(0,0,0)
  line(fx,fy,fx - 20,fy - 20)
  stroke(0,0,0)
  line(fx,fy,fx + 17,fy + 15)
  stroke(0,0,0)
  line(fx,fy,fx - 15,fy + 15)
  stroke(0,0,0)
  line(fx,fy,fx + 15,fy - 20)
  fill(34,139,34)
  noStroke()
  ellipse(fx,fy,18,18)
  ellipse(fx,fy - 10,15,15)
  
def win():
  fill(0, 0, 205)
  textAlign(CENTER, CENTER)
  textSize(70)
  text("YOU WIN", width/2, height/2)
  exit()
  
def loose():
  fill(205, 0, 0)
  textAlign(CENTER, CENTER)
  textSize(70)
  text("YOU LOOSE", width/2, height/2)
  exit()
  
# check if frog collided with a car at x, y
def collision(x, y):
  carLeft = x
  carRight = x + 50
  carTop = y
  carBottom = y + 30
  
  frogTop = fy-15
  frogBottom = fy+5
  frogLeft = fx-8
  frogRight = fx+8
  
  if frogLeft<carRight and frogRight>carLeft and frogBottom>carTop and frogTop<carBottom:
    loose()
  
  
  
  
  # # delete later
  # # drawing dots to mark corners of frog hitbox
  # fill(0)
  # ellipse(fx, fy, 3, 3) # frog x, y
  # ellipse(fx-8, fy-15, 3, 3) # top left
  # ellipse(fx+8, fy-15, 3, 3) # top right
  # ellipse(fx-8, fy+5, 3, 3) # bottom left
  # ellipse(fx+8, fy+5, 3, 3) # bottom right
  
def setup():
  global fx,fy,car1x,car1y,car2x,car2y,car3x,car3y
  fx = 200
  fy = 380
  size(400,400)
  car1x = 20
  car1y = 65
  car2x = 20
  car2y = 165
  car3x = 20
  car3y = 265


def draw():
  global fx,fy,car1x,car1y,car2x,car2y,car3x,car3y
  background(173,255,47)
  roads()
  frog()
  car1()
  car2()
  car3()
  car1x += 5
  if car1x >= 400:
    car1x = 20
  car2x += 4
  if car2x >= 400:
    car2x = 20
  car3x += 3
  if car3x >= 400:
    car3x = 20
  if fy <= 20:
    win()
    
  collision(car1x, car1y)
  collision(car2x, car2y)
  collision(car3x, car3y)
    
    

  
  
  
def keyPressed():
  global fx,fy
  if key == 'w':
    fy -= 5
  if key == 'a':
    fx -= 5
  if key == 's':
    fy += 5
  if key == 'd':
    fx += 5
  
  
  
  
  
run()