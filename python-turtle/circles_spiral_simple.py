import turtle

turtle.color("green")
turtle.circle(75)
turtle.right(15)
turtle.circle(75)

num_circles = int(input("How many circles would you like in your spiral?"))

for i in range(num_circles):
  turtle.circle(75)
  turtle.right(360/num_circles)