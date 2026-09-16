import random as r

def sumrange(start, stop): 
  sum = 0
  for i in range(start, stop+1):
    sum = sum + i
    # print(sum)
    
  print(sum)
  
sumrange(200, 1000)
sumrange(1, 4)
