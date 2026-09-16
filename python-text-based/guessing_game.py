from random import*

num = randint(1,100)
guesses = 1
chances = 6

while guesses < chances:
  user_input = int(input("Enter a number 1 - 100"))
  
  if user_input == num:
    print("Correct")
    print("It took %d guesses." % guesses)
    break
  else:
    if user_input > num:
      print("Too High")
    else:
      print("Too low")
    guesses += 1
      


