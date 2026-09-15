'''
Draws a flower with random attributes
Remixed from a student's code
3/1/2022
'''


from turtle import*
from random import*

speed(0)

color_list = ["blue","red","green","purple", "orange", "yellow"]

# returns a random color from the color list and removes that color from the list
def color_pop():
  return color_list.pop(randint(0, len(color_list) - 1))

#petal color
petal_color = color_pop()
print(petal_color)

#stem color
stem_color = color_pop()
print(stem_color)

#center color
center_color = color_pop()
print(center_color)

#background color
background_color = color_pop()
print(background_color)

#petal raduis
radius = randint(30,50)
print(radius)

#number of petals
petal_count = randint(3,50)
print(petal_count)

#all colors
all_colors = [petal_color, stem_color, center_color, background_color]


Screen().bgcolor(all_colors[3])

#stem
color(all_colors[1])
pensize(15)
goto(0, -200)
goto(0,0)

  
#petal draw
pensize(1)

def draw_petals(amount,radius): 
  for i in range(amount):
    begin_fill()
    circle(radius,120)
    end_fill()
    goto(0,0)
    begin_fill()
    circle(-radius,120)
    end_fill()
    goto(0,0)
    right(360/amount)



color(all_colors[0])
draw_petals(petal_count,radius)

#center draw
color(center_color)
dot(36)
