import turtle as t

t.tracer(100)

t.penup()
t.goto(0, -190)
t.left(90)
t.pendown()




def tree(size, level):
  if level == 0:
    return
  
  t.forward(size)
  
  t.right(35)
  tree(size/2, level-1)
  
  t.left(70)
  tree(size/1.2, level-1)
  
  t.right(35)
  # t.color()
  t.backward(size)
  
tree(100, 15)