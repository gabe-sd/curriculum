import turtle

boxsize = 75
boxes_per_row = 3
turn = 0


play_button_x = 0
play_button_y = (boxsize * boxes_per_row) / 2 * -1 - 40

t = turtle.Turtle()

def create_board():
  
  t.hideturtle()

  t.speed(10)
  t.pensize(5)
  
  t.penup()
  t.goto((boxsize * boxes_per_row) / 2,boxsize / 2)
  t.setheading(180)
  t.pendown()
  t.forward(boxsize * boxes_per_row)
  
  t.penup()
  t.goto((boxsize * boxes_per_row) / 2,boxsize / 2 * -1)
  t.setheading(180)
  t.pendown()
  t.forward(boxsize * boxes_per_row)
  
  t.penup()
  t.goto(boxsize / 2 * -1, boxsize * boxes_per_row / 2)
  t.setheading(-90)
  t.pendown()
  t.forward(boxsize * boxes_per_row)

  t.penup()
  t.goto(boxsize / 2, boxsize * boxes_per_row / 2)
  t.setheading(-90)
  t.pendown()
  t.forward(boxsize * boxes_per_row)

def create_reset_game_button():
  #global play_button_x, play_button_y
  t.penup()
  t.goto(play_button_x,play_button_y)
  #move = False
  #align = "center"
  #font = ("Helvetica", 20, "bold")
  t.write("Reset", False, "center", ("Helvetica", 20, "bold"))

def write_x_or_o(mouse_x,mouse_y):
  global turn
  t.penup()
  fontsize = 40
  t.goto(mouse_x,mouse_y - fontsize / 2)
  t.pendown()
  if turn % 2 == 0:
    letter = "X"
  else: 
    letter = "O"
  #x_or_o = "X" if turn % 2 == 0 else "O"
  #move = False
  #align = "center"
  #font = ("Helvetica", fontsize, "bold")
  t.write(letter, False, "center", ("Helvetica", fontsize, "bold"))
  turn += 1

def check_click(mouse_x, mouse_y):
  global turn
  t.penup()
  t.goto(mouse_x,mouse_y)
  if t.distance(play_button_x,play_button_y) < 35:
    turn = 0
    play_game()
  else:
    if turn < 9:
      write_x_or_o(mouse_x,mouse_y)

def write_instructions():
  t.penup()
  t.goto(0,(boxsize * boxes_per_row)/2+20)
  t.write("Tap or click in a box to place the X or O",False,"center",("Helvetica",14,"normal"))

def play_game():
  t.getscreen().reset()
  write_instructions()
  create_board()
  create_reset_game_button()
  #turn = 0
  t.getscreen().onclick(check_click)
  t.getscreen().listen()

play_game()