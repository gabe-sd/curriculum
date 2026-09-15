from processing import*

cell_size = 10
width = 500
height = 500

grid = [[[0, 0, 0] for i in range(width//cell_size)] for i in range(height//cell_size)]

def setup():
  size(width, height)
  noStroke()
  
def draw():
  background(255)
  
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      cell = grid[x][y]
      
      cell[0] = x*cell_size*(mouseY/height)
      cell[1] = y*cell_size*(mouseX/width)
      cell[2] = (millis()//7)%510
      cell[2] = abs(cell[2]-255)
      # cell[2] *= mouseX/(mouseY+1)
      
      r = cell[0]
      g = cell[1]
      b = cell[2]
      fill(r, g, b)
      rect(x*cell_size, y*cell_size, cell_size, cell_size)
  
run()