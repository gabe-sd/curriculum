from processing import*

jump_ready = True

def setup():
  global bigfoot_img, bf_y, bf_vy, ground_y
  
  size(500, 300)
  bigfoot_img = loadImage("turtle.png")
 
  bf_vy = 0
  ground_y = height-20
  bf_y = ground_y - 50 
  

def draw():
  global bf_y, bf_vy
  background(50, 20, 200)
  
  # draw ground
  fill(0, 255, 0)
  rect(-10, ground_y, width + 20, 20)
  
  # bigfoot physics
  bf_y += bf_vy
  if jump_ready == False:
    bf_vy += 1
  
  # draw bigfoot
  image(bigfoot_img, 30, bf_y, 50, 50)
  
def keyPressed():
  print("key pressed")
  global bf_vy, jump_ready
  if jump_ready:
    print("yes")
    bf_vy = -10
    jump_ready = False
    

run()