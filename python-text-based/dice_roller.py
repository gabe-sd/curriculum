'''
Dice!
3/30/2022
'''

import random

def make_lines(x):
  for i in range(x):
    print("")


name = input("Hello! What's your name?")

print("Hi " + name + ", it's nice to meet you!")

total = 0

while True:
  
  sides = int(input("\nHow mnay sides to your dice?"))
  how_many = int(input("How many dice?"))
  
  round_total = 0
  
  for i in range(how_many):
    dice = random.randint(1, sides)
    print(dice)
    total += dice
    round_total = round_total + dice
    
  print("Round total: " + str(round_total))
  print("Running total: " + str(total))  
  
  make_lines(10)
