

"""
Modular button for processing gmaes
Just copy/paste the button function
"""

# Parameters: image, x, y, width, height
# Returns true if clicked
def button(img, x, y, w, h):
  # display image
  image(img, x, y, w, h)
  
  # check if mouse over image and mouse clicked
  if mousePressed and x < mouseX < x + w and y < mouseY < y + h:
    return True
