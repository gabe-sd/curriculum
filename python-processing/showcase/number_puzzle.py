from processing import *
import random as r

#0 is blank space
board = ["", 1, 2, 3, 4, 5, 6, 7, 8]
r.shuffle(board)



def setup():
  size (498, 498)

def draw():
  
  #board background
  background(135, 35, 35)
  rect (166, 0, 1, 498)
  rect (332, 0, 1, 498)
  rect (0, 166, 498, 1)
  rect (0, 332, 498, 1)
  
  #tiles 
  fill(0)
  textSize(100)
  #top left
  text(board[0], 60, 125)
  #top middle
  text(board[1], 225, 125)
  #top right
  text(board[2], 390, 125)
  #middle left
  text(board[3], 60, 285)
  #middle middle
  text(board[4], 225, 285)
  #middle right
  text(board[5], 390, 285)
  #bottom left
  text(board[6], 60, 445)
  #bottom middle
  text(board[7], 225, 445)
  #bottom right
  text(board[8], 390, 445)
  
  win()
  
def mouseClicked():
  empty()


#return cell number clicked
def cellClicked():
  if mouseX < 166 and mouseY < 166: 
    return 0
  if mouseX < 332 and mouseY < 166 and mouseX > 166: 
    return 1
  if mouseX > 332 and mouseY < 166: 
    return 2
  if mouseX < 166 and mouseY < 332 and mouseY > 166: 
    return 3
  if mouseX > 166 and mouseX < 332 and mouseY < 332 and mouseY > 166: 
    return 4
  if mouseX > 332 and mouseY < 332 and mouseY > 166:
    return 5
  if mouseX < 166 and mouseY > 332:
    return 6
  if mouseX > 166 and mouseX < 332 and mouseY > 332:
    return 7
  if mouseX > 332 and mouseY > 332:
    return 8
  
#swaps index a & b in board.
def swap(a, b):
  item_a = board[a]
  item_b = board[b]
  board[b] = item_a
  board[a] = item_b
  
def empty():
  cell = cellClicked()
  if cell == 0:
    if board [1] == "":
      swap(0, 1)
    elif board [3] =="":
      swap(0, 3)
      
  if cell == 1:
    if board[0] == "":
      swap(1, 0)
    elif board[2] == "":
      swap(1, 2)
    elif board[4] == "":
      swap(1, 4)
      
  if cell == 2:
    if board[1] == "":
      swap(2, 1)
    elif board[5] == "":
      swap(2, 5)
      
  if cell == 3:
    if board[0] == "":
      swap(3, 0)
    elif board[4] == "":
      swap(3, 4)
    elif board[6] == "":
      swap(3, 6)
      
  if cell == 4:
    if board[1] == "":
      swap (4, 1)
    if board[3] == "":
      swap(4, 3)
    if board[5] == "":
      swap(4, 5)
    if board[7] == "":
      swap(4, 7)
 
  if cell == 5:
    if board[2] == "":
      swap(5, 2)
    if board[4] == "":
      swap(5, 4)
    if board[8] == "":
      swap(5, 8)
      
  if cell == 6:
    if board[3] == "":
      swap(6, 3)
    if board[7] == "":
      swap(6, 7)
  
  if cell == 7:
    if board[6] == "":
      swap(7, 6)
    if board[4] == "":
      swap(7, 4)
    if board[8] == "":
      swap(7, 8)
      
  if cell == 8:
    if board[7] == "":
      swap(8, 7)
    if board[5] == "":
      swap(8, 5)
      

def win():
  if board == [1, 2, 3, 4, 5, 6, 7, 8, ""] or board == ["", 1, 2, 3, 4, 5, 6, 7, 8]:
    fill (51, 6, 8)
    textSize (50)
    text ("you won", 170, 220)
    exit()
  
  
  
  
  
run()