from processing import*
from copy import deepcopy
import random as r
screen_size = 1000
cell_size = 10
on_ratio = 0.1
next_grid = []
grid = []

def setup():
  global grid, next_grid
     
 
  size(screen_size, screen_size)
  frameRate(1)
  
  #creat grid with all False valus
  for i in range(screen_size//cell_size):
    grid.append([False for i in range(screen_size//cell_size)])
  
# set grid initial values
  for x in range(len(grid)):
    for y in range (len(grid)):
      grid[x][y] = True if r.uniform(0,1) < on_ratio else False
      
 
 
 
 
 
  next_grid =deepcopy(grid)

def draw():
  background(100)
  
  display_grid()
  calculate_next_grid()
  
  # load next grid
  global grid
  grid = deepcopy(next_grid)
  
def display_grid():
  for x in range(len(grid)):
    for y in range (len(grid)):
      #cell on
      if grid[x][y] == True:
        fill(81, 227, 41)
      else:
        #cell off
        fill(18, 17, 17)
      rect(x*cell_size, y*cell_size, cell_size, cell_size)
      
      
def calculate_next_grid():
  #for each cell in grid
  for x in range(len(grid)):
    for y in range(len(grid)):
      # count lving neighbors 
      numLive = 0
      for xx in [x-1, x, x+1]:
        for yy in [y-1, y, y+1]:
        #make sure we dont go out of bounds
          if xx>=0 and yy>=0 and xx<screen_size//cell_size and yy<screen_size//cell_size:
            numLive += grid[xx][yy] #add 1 to numLive counter if cell value is True
          
      #apply rules of the game    
      if grid[x][y] == True: # if current cell is on 
        if numLive < 2:
          next_grid[x][y] = False
        elif numLive== 2 or numLive==3:
          next_grid[x][y] = True
        else: #die by overpop
          next_grid[x][y] = False
      else:# if the current cell is dead
        if numLive==3:
          next_grid[x][y]=True
      #CHECK THIS
      

run()