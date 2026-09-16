# =====================================================================
# Showcase: Asteroid Field
# Concepts: classes, images, lives and score, saving a high score to a file
# Student project. Images moved next to the code; the program itself is unchanged.
# =====================================================================

from processing import *

score = 0
lives = 3

# loads highscore from data file
def loadHighscore():
  global highscore
  file = open("data.txt", "r")
  highscore = int(file.read())
  file.close()
  
loadHighscore()

#updates highscore in data file to current highscore
def updateHighscore():
  file = open("data.txt", "w")
  file.write(highscore)
  file.close()

class Player:
  x = 400
  y = 450
  vx = 0
  
  def run():
    Player.x += Player.vx
    
    Player.x = min(Player.x, 750)
    Player.x = max(Player.x, 0)
    
    image(ship_image, Player.x, Player.y, 50, 50)
    
class Asteroid:
  instances = []
  
  def __init__(self):
    self.x = random(0, 750)
    self.y = -100
    self.size = random(20, 100)
    self.speed = random(1, 5)
    Asteroid.instances.append(self)
    
  def display(self):
    global score, highscore, lives
    
    #display asteroids
    image(asteroid_image, self.x, self.y, self.size, self.size)
    
    #movement
    self.y += self.speed
    
    # self deletion and score tracking
    if self.y > 500:
      score += 1
      Asteroid.instances.remove(self)
      
    if score > highscore:
      highscore = score
      updateHighscore()
      
    # asteroid-ship collision detection
    # px, py is the x, y coordinate player middle of the player
    # ax, ay is the x, y coordinate player middle of the asteroid
    px = Player.x + 25
    py = Player.y + 25
    ax = self.x + self.size/2
    ay = self.y + self.size/2
    hitbox_size = 20 + self.size/2
    if dist(px, py, ax, ay) < hitbox_size:
      lives -= 1
      Asteroid.instances.remove(self)

  def run():
    # display all asteroids
    for a in Asteroid.instances:
      a.display()
      
    # spawn asteroids
    if frameCount%50==0:
      Asteroid()
      
class Laser:
  instances = []
  def __init__(self):
    Laser.instances.append(self)
    
    self.x = Player.x
    self.y = Player.y
  
  def display(self):
    global score
    image(laser_image, self.x, self.y, 50, 20)
    self.y -= 5
    if self.y < 0:
      Laser.instances.remove(self)
    
    for i in Asteroid.instances:
    
      lx = self.x + 25
      ly = self.y + 25
      ax = i.x + i.size/2
      ay = i.y + i.size/2
      hitbox_size = 20 + i.size/2
      if dist(lx, ly, ax, ay) < hitbox_size:
        score += 1
        Asteroid.instances.remove(i)
        Laser.instances.remove(self)

def setup():
  global game_state, ship_image, asteroid_image, laser_image
  
  size(800, 500)
  
  game_state = game
  
  ship_image = loadImage("rocketship.gif")
  asteroid_image = loadImage("download-removebg-preview (2).png")
  laser_image = loadImage("pixil-frame-0.png")

def draw():
  game_state()
  
def keyPressed():
  if key==CODED:
    if keyCode == RIGHT:
      Player.vx = 5
    elif keyCode == LEFT:
      Player.vx = -5
  if key == " " and frameCount%2 == 0:
    Laser()
      
def keyReleased():
  if key == CODED:
    if keyCode == RIGHT or keyCode == LEFT:
      Player.vx = 0

def game():
  global game_state
  background(0)
  Player.run()
  Asteroid.run()
  
  # UI
  fill(255) # white
  textSize(20)
  text("lives: " + str(lives), 30, 30)
  
  fill(255)
  textSize(20)
  text("score: " + str(score), 30, 80)
  
  fill(255)
  textSize(20)
  text("high score: " + str(highscore), 30, 55)
  
  for i in Laser.instances:
    i.display()
  
  #game over check
  if lives == 0:
    game_state = menu
  if score == 100:
    game_state = win_screen
    
def menu():
  global game_state, score, lives
  textSize(30)
  text("Game Over! Click to restart.", 250, 375)
  if mousePressed:
    game_state = game
    Asteroid.instances = []
  lives = 3
  score = 0
  Player.x = 400
  
def win_screen():
  global game_state, lives, score
  textSize(30)
  text("You did it! Click to play again.", 250, 375)
  if mousePressed:
    game_state = game
    Asteroid.instances = []
  lives = 3
  score = 0
  Player.x = 400
  
run()