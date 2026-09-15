import random
import string

print("This app helps you pick a username if the one you like is taken")

username = input("Enter a username: ")

numbers = range(0, 10)
symbols = ["!", "@", "#", "", "&", "*", "%"]
letters = string.ascii_lowercase

all_chars = [numbers, symbols, letters]

for i in range(5):
  new_username = username + "-"
  for i in range(5):
    chars = random.choice(all_chars)
    new_username += str(random.choice(chars))
    
  print(new_username)