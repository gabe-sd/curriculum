'''
By Gabriel Venditti
March 2022

Description: Tic Tac Toe with Turtle Library
'''

# imports
from turtle import*

# set background color
Screen().bgcolor("blue")
speed(0)

# make a board that keeps track of the state of the game
board = [None for i in range(0, 9)]

# draw grid
def grid(): 
  
  penup()
  goto(-150, 50)
  pendown()
  for i in range (4):
    forward (300)
    backward (100)
    right (90)
    backward (100)
 
# place piece helper function
def place(x, y, let):
  penup()
  goto(x, y)
  pendown()
  
  write(let, font=("Arial", 60, "bold")) 

# place piece main function
def turn(piece):
  # user input with validation
  try:
    user_input = int(input("Enter a pos [0-8]:")) 

    # if number is out of bounds, raise exception
    if user_input not in range(0, 8):
      print("Make sure you enter a number 0-8")
      raise Exception
      
    # if space is already taken, raise exception
    if board[user_input] != None:
      print("That spot is already taken!")
      raise Exception
 
    if user_input == 0:
      place(-125, 70, piece)
      board[0] = piece
    elif user_input == 1:
      place(-25, 70, piece)
      board[1] = piece
    elif user_input == 2:
      place(75, 70, piece)
      board[2] = piece
    #
    elif user_input == 3:
      place(-125, -25, piece)
      board[3] = piece
    elif user_input == 4:
      place(-25, -25, piece)
      board[4] = piece
    elif user_input == 5:
      place(75, -25, piece)
      board[5] = piece
    #
    elif user_input == 6:
      place(-125, -125, piece)
      board[6] = piece
    elif user_input == 7:
      place(-25, -125, piece)
      board[7] = piece
    elif user_input == 8:
      place(75, -125, piece)
      board[8] = piece

  except:
    turn(piece)
    

# returns true if there's a winning combination in these places
def check_combo(a, b, c):
  if board[a] == board[b] == board[c] and board[a] != None:
    return True
  else:
    return False

# this function checks if someone won the game
def is_winner():
  # rows
  if check_combo(0, 1, 2):
    return True
  elif check_combo(3, 4, 5):
    return True
  elif check_combo(6, 7, 8):
    return True
    
  # columns
  elif check_combo(0, 3, 6):
    return True
  elif check_combo(1, 4, 7):
    return True
  elif check_combo(2, 5, 8):
    return True
  
  # diagonals
  elif check_combo(0, 4, 8):
    return True
  elif check_combo(2, 4, 6):
    return True
    
  # If we made it here without return anything then nobody won yet
  else:
    return False

def new_round():
  global current_player
  global score
  
  for i in range(9):
    turn(current_player)
    
    if is_winner():
      print("Congratulations " + current_player + ", you win!")
      score[current_player] += 1
      break
    
    # change turns
    if current_player == 'X':
      current_player = 'O'
    else:
      current_player = 'X'
    # TODO Degbug this. Prints tie after every turn  
    print('Tie!')

# draws the gameboard
grid()

# runs the game
current_player = 'X'
score = {'X': 0, 'O': 0}
game_running = True

while game_running:
  print('\n')
  new_round()
  
  print('\nSCORE:')
  print('Player X: ' + str(score['X']))
  print('Player O: ' + str(score['O']))
  
  input = input("Player again? [y/n]")
  if  input == 'n':
    game_running == False


  
  




