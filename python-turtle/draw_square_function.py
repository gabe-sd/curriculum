import turtle

def draw_square(size, x, y):
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  for i in range(4):
    turtle.forward(size)
    turtle.right(90)
    
draw_square(30, 0, 0)

draw_square(100, -50, 150)