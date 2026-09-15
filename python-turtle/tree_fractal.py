import turtle as pen

# setup
pen.Screen().bgcolor('light blue')
pen.left(90)
pen.penup()
pen.goto(0, -150)
pen.pendown()
# pen.hideturtle()



def tree(size, lvl):   
  # base case
  if lvl <= 0:
    return
  
  # trunk
  pen.forward(size)
  
  # right branch
  pen.right(angle)
  tree(0.8*size, lvl-1)

  # left branch
  pen.left(2 * angle)
  tree(0.8*size, lvl-1)
 
  # reset position
  pen.pencolor(0, 255/lvl, 0)
  pen.right(angle)
  pen.backward(size)



# pen.speed(2)
pen.tracer(10)  # super speed
angle = 30
tree(60, 4)
pen.update()

# imports, setup. move turtle to bottom center of screen

# base case (exit condition)

# trunk

# right brach recursive call

# left branch recursive call

# bring turtle back to start
















