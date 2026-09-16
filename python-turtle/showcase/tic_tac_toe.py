import turtle
win = False

y_cor = 0
x_cor = 0
draw = True
player_x = turtle.Turtle()
player_o = turtle.Turtle()
turtle.Screen().bgcolor("lavender")


row_a = [' ',' ',' ']
row_b = [' ',' ',' ']
row_c = [' ',' ',' ']
def setup():
  global player_x,player_o
  player_x.penup()
  player_x.color("blue")
  player_o.penup()
  player_o.color("crimson")
  player_x.goto(0,0)
  player_o.goto(0,0)
  board = turtle.Turtle()
  board.hideturtle()
  board.penup()
  board.goto(-150,50)
  board.pendown()
  for i in range(4):
    board.speed(0)
    board.forward(300)
    board.backward(100)
    board.right(90)
    board.backward(100)
def draw_x(x,y):
  global player_x
  player_x.penup()
  player_x.goto(x,y)
  player_x.pendown()
  player_x.right(45)
  player_x.forward(50)
  player_x.backward(100)
  player_x.forward(50)
  player_x.left(-90)
  player_x.forward(50)
  player_x.backward(100)
  player_x.forward(50)
  player_x.right(-135)
  

  
  
def draw_o(x,y):
  global player_o
  player_o.penup()
  player_o.goto(x,y - 35)
  player_o.pendown()
  player_o.circle(40)

def player_turn(char):
  global row_a, row_b, row_c, draw, x_cor, y_cor
  draw = False
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print(char + " player turn")  
  index = 0
  
  
  player_row = input("What row would you like to select?")
  
  if player_row == "a":
    y_cor = 100
  elif player_row == "b":
    y_cor = 0
  elif player_row == "c":
    y_cor = -100
  else:
    print("Not valid try again.")
    player_turn(char)
  
  player_col = int(input("What colum would you like to select"))
  
  if player_col == 1:
    x_cor = -100
    index = 0
  elif player_col == 2:
    x_cor = 0
    index = 1
  elif player_col == 3:
    x_cor = 100
    index = 2
  else:
    print("Not valid try again.")
    player_turn(char)
  if player_row == "a" and row_a[index] != ' ':
    print("BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO YOU SUCK")
    player_turn(char)
  elif player_row == "b" and row_b[index] != ' ':
    print("BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO YOU SUCK")
    player_turn(char)
  elif player_row == "c" and row_c[index] != ' ':
    print("BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO YOU SUCK")
    player_turn(char)
  
  
  else:
    draw = True
    if player_row == "a":
      row_a[index] = char
    elif player_row == "b":
      row_b[index] = char
    elif player_row == "c":
      row_c[index] = char
   
    print(row_a) 
    print(row_b) 
    print(row_c) 
  
  
def check(char):
  global win,row_a,row_b,row_c
  
  if row_a[0] == char:
    if row_b[0] == char and row_c[0] == char:
      win = True
    elif row_a[1] == char and row_a[2] == char:
      win = True
    elif row_b[1] == char and row_c[2] == char:
      win = True
  elif row_a[1] == char:
    if row_b[1] == char and row_c[1] == char:
      win = True
  elif row_a[2] == char:
    if row_b[2] == char and row_c[2] == char:
      win = True
    elif row_b[1] == char and row_c[0] == char:
      win = True
  elif row_b[0] == char:
    if row_b[1] == char and row_b[2] == char:
      win = True
  elif row_c[0] == char:
    if row_c[1] == char and row_c[2] == char:
      win = True  

def play():
  global draw, x_cor, y_cor, win
  setup()
  
  print('''
        This is the board!
           1    2     3
        a    |    |
          -------------
        b    |    |
          -------------
        c    |    |
  
  ''')  
  for i in range(4):
    player_turn("x")
    if draw == True:
      draw_x(x_cor,y_cor)
    check("x")
    if win == True:
      print(" player x wins lol")
      break
    player_turn("o")
    if draw == True:
      draw_o(x_cor,y_cor)
    check("o")
    if win == True:
      print(" Player o wins lol")
      break

  
  
  
play()  
  
  
