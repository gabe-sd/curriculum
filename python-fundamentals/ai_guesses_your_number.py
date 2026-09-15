from random import*


x = 1
y = 100
user_input = int(input("Enter a number 1 - 100"))
guesses = 1


for i in range(10):
  ai_guess = int((x + y) / 2)
  if ai_guess == user_input:
    print("Correct")
    print("It took %d guesses." % guesses)
    break
  else:
    if ai_guess > user_input:
      print("Too High")
      y = ai_guess
    else:
      print("Too low")
      x = ai_guess
    guesses += 1
      