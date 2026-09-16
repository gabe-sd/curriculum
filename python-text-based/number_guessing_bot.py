import random
import time

low = 1
high = 10000
attempts = 0

# get number from user with robust input validation
def getNum():
  global num
  
  print("Pick a number between {} and {}".format(low, high))
  try:
    num = int(input("Enter number: "))
  except:
    getNum()
  if num<low or num>high:
    getNum()

getNum()

start_time = time.time()
while True:
  guess = (high+low)//2
  attempts += 1
  
  print("The bot guessed {}".format(guess))
  if guess == num:
    print("The bot guessed your number in {} attempts and {} seconds".format(
      attempts, time.time()-start_time))
    break
  
  if guess > num:
    high = guess-1
  if guess < num:
    low = guess+1
  

  
  
  