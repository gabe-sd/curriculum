# Last update: 8/24/2022

from processing import*
import random
import time


class Paddle():
  def __init__(self, x, color):
    self.color = color
    self.x = x
    self.y = height/2
    self.width = 20
    self.height = 50
    
  def draw(self, y):
    # move towards ball
    if self.y < ball.y:
      self.y += difficulty
    elif self.y > ball.y:
      self.y -= difficulty
      
    # draw
    fill(self.color[0], self.color[1], self.color[2])
    rect(self.x, self.y, self.width, self.height)
    
  def reset(self):
    self.y = height/2
    
    
class Ball():
  def __init__(self, color):
    self.color = color
    self.size = 15
    self.x = width/2
    self.y = height/2
    self.v = PVector(0, 0)
    
    
  def draw(self):
    global player_score, ai_score
    
    fill(self.color[0], self.color[1], self.color[2])
    
    # top/bottom of screen bounce
    if self.y < 0 or self.y > height:
      self.v.y *= -1
    
    self.x += self.v.x
    self.y += self.v.y
    
    ellipse(self.x, self.y, self.size, self.size)
    
  def reset(self):
    # move ball to middle of screen
    self.x = width/2
    self.y = height/2
    
    # set vx and vy
    # init as random direction then normalize vector and mutiply by difficulty
    self.vx = random.uniform(.2, 1)
    self.vy = random.uniform(.2, 1)
    
    time.sleep(2)
    
    
def draw_score():
  fill(50, 255, 50)
  text("Player Score: {}".format(player_score), 5, 25)
  text("Opponent Score: {}".format(ai_score), 5, 50)

  
def reset():
  ai.reset()
  player.reset()
  ball.reset()


def win_check():
  # ai win
  if ball.x < 0:
    ai_score += 1
    reset()
  # player win
  elif ball.x > width:
    player_score += 1
    reset()
  
  
def setup():
  global player_score, ai_score
  global player, ai, ball
  global difficulty
  
  player_score = 0
  ai_score = 0
  player = Paddle(15, (0, 0, 255))
  ai = Paddle(380, (250, 250, 0))
  ball = Ball((255, 255, 255))
  
  size(400, 400)
  textSize(20)
  # textAlign(RIGHT)
  rectMode(CENTER)
  noStroke()
  
  reset()
  
  
def draw():
  background(0)
  draw_score()
  
  win_check()
  player.draw(mouseY)
  ai.draw(height/2)
  ball.draw()
  
  
run()