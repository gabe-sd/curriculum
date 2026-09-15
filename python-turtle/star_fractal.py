import turtle as t


t.tracer(50)
  
t.Screen().bgcolor("black")
t.color("cyan")
t.hideturtle()

def star(size):
  if size <= 10: ###
    return
    
  for i in range(5):
    t.forward(size)
    star(size/3) ###
    t.right(144)
    
star(120)

t.update()

































