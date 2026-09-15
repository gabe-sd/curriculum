# March 2020
# 2 player tic tac toe using text (not graphics)

import random

# empty board to start
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# tracks whose turn it is, random starting player
currentplayer = random.choice(["X", "O"])


# prints board
def printBoard():
  print(board[0] + " | " + board[1] +" | " + board[2])
  print("---------")
  print(board[3] + " | "+ board[4] + " | " + board[5])
  print("---------")
  print(board[6] + " | " + board[7] + " | " + board[8])


# places a player piece on the board
def playerPlace():
  global board
  inp = int(input("input a spot 1-9; \n"))
  if board[inp - 1 ] == "-":
    board[inp - 1] = currentplayer
  else:
    print("there's already a piece there, please pick another spot\n") 
    playerPlace()

    
# this is a helper function for checkBoard
# checks spots a, b, c to see if anyone won
# if someone won, it assigns them to the winner variable
winner = None
def checkSpots(a, b, c):
  # the global keyword tells the computer that we're talking about a variable we made outside of this function
  global winner
  
  # check to see if the 3 spots that were input into this function have a winning combination
  if board[a] == board[b] == board[c] and board[a] != "-":
    # if there's a winner, assign them to the winner variable
    winner = board[a]
    return True
  
  # if we made it here, then there no winner for these 3 spots
  else:
    return False

    
# check the whole board to see if anyone won. Returns true if someone won
def someoneWon():
  # rows
  if checkSpots(0, 1, 2):
    return True
  elif checkSpots(3, 4, 5):
    return True
  elif checkSpots(6, 7, 8):
    return True
    
  # columns
  elif checkSpots(0, 3, 6):
    return True
  elif checkSpots(1, 4, 7):
    return True
  elif checkSpots(2, 5, 8):
    return True
  
  # diagonals
  elif checkSpots(0, 4, 8):
    return True
  elif checkSpots(2, 4, 6):
    return True
    
  # If we made it here without return anything then nobody won yet
  else:
    return False


# change turns
def changeTurns():
  # the global keyword tells the computer that we're talking about a variable we made outside of this function
  global currentplayer
  
  # if it was player X's turn, we change to player O's turn
  if currentplayer == "X":
    currentplayer = "O"
  
  # if it was player O's turn, we change to player X's turn
  elif currentplayer == "O":
    currentplayer = "X"


# this function checks if it's a tie game
# returns True if tie game. False if not a tie game.
def tieGame():
  # if we find any empty spaces then its not a tie game so we return False
  for x in board:
    if x == "-":
      return False
  
  # if we made it here then we didnt find any empty spaces and it's a tie game, 
  # so we return True 
  return True
  
  
# this function asks if they want to play again
gameRunning = True
def playAgain():
  # make sure we're modifying the variables outside of this function
  global board
  global winner
  
  # ask if they want to play again
  playAgain = None # instantiate playAgain to avoid a bug here
    
  # this while loop ensures that the game doesnt break if the player enters something other than y or n
  while playAgain != 'y' and playAgain != 'n':
    playAgain = input("Would you like to play again? [y/n]")
    playAgain = playAgain.lower() # makes input lower case
    
    # if they want to play again, set up a new game
    if playAgain == 'y':
      # empty board to start
      board = ["-","-","-",
                "-","-","-",
                "-","-","-"]
      winner = None
    
    # if they don't want to play again
    elif playAgain == 'n':
        print("Goodbye!")
        gameRunning = False


# This code uses our functions to run the game
while gameRunning:
  # normal gameplay
  printBoard()
  print("\nPlayer " + currentplayer + ", it's your turn")
  playerPlace()
  
  # if someone won, do this
  if someoneWon():
    # congratulations message
    printBoard()
    print("\nCongratulations player " + winner + ", you won!")
    playAgain()
    
  elif tieGame():
    print("Looks like a tie game!\n")
    playAgain()

  # if there is no winner yet, change turns
  else:
    changeTurns()
  






































