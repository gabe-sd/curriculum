from random import randint

low = 1
high = 10000

print("Pick between {} and {} and remember it".format(low, high))
input("Press enter to continue ")


tries = 0

while True:
  guess = (low+high)//2
  tries += 1
  
  print("Is {} your number?".format(guess))
  response = input("Enter correct, high, or low: ")
  
  if response not in ['correct', 'high', 'low']:
    print("invalid response")
    continue
  
  if response == "correct":
    print("The computer guessed your number in {} tries".format(tries))
    break
  elif response == 'high':
    high = guess - 1
  elif response == 'low':
    low = guess + 1
    

