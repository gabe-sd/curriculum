from random import*

number = randint(1, 10)
guess = 0
tries = 1

while number != guess:
  guess = int(input("Pick a number from 1 to 10"))
  
  if number == guess:
    print("Good job! You guess the right number in " + str(tries) + " tries!")
    
  if number > guess:
    print("That wasn't it, the number is bigger")
    
  if number < guess:
    print("That wasn't it, the number is smaller")
    
  tries += 1