low = 1
high = 1600

print("Pick a number between {} and {} and remember it.".format(low, high))
input("Press enter to continue")

attempts = 0
while True:
  guess = round((high + low)/2)
  attempts += 1
  print("\nIs your number {}?".format(guess))
  response = input("Enter H if it's too high, L if it's too low, or C if it's correct: ")
  if response == "C":
    print("The computer guessed your number in {} tries".format(attempts))
    break
  elif response == "H":
    high = guess-1
  else:
    low = guess+1
