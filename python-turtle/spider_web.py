import turtle

turtle.tracer(100)

# size is the length of a line in the shape
size = 1
angle = 120
for i in range (400) :
  turtle.color("white")
  turtle.forward(size)
  turtle.right(angle)
  size = size + 1  # increase size
 
  turtle.color("black")
  turtle.forward(size)
  turtle.right(angle)
  size = size + 1  # increase size
  
  turtle.color("black")
  turtle.forward(size)
  turtle.right(angle)
  size = size + 1  # increase size
  
  turtle.color("white")
  turtle.forward(size)
  turtle.right(angle)
  size = size + 1  # increase size
  
  turtle.color("red")
  turtle.forward(size)
  turtle.right(angle)
  size = size + 1  # increase size
  
  turtle.color("pink")
  turtle.forward(size)
  turtle.right(90)
  size = size + 1  # increase size