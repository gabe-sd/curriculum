import turtle
import random
#rember to import rng and turtle


while True:
  var=(random.randint(70, 200))
  print (var)
  #how much it rotates
  
  var2=(random.randint(1, 10))
  print (var2)
  turtle.pensize(var2)
  #pensize
  
  var3=(random.randint(12, 500))
  print (var3)
  
  color_list = ["black", "white", "lime","green","red","blue","yellow","purple"]
  turtle.Screen().bgcolor("gray")
  
  turtle.tracer(var3)
  
  for i in range(1000):
    turtle.color(color_list[i%len(color_list)])
    turtle.forward(i)
    turtle.right(var)
  
        
  turtle.update()
  
  #update and tracer go together
  
  turtle.goto(0, 0)
  turtle.clear()
