import random

score = random.randint(0, 100)

print("{} points".format(score))

if score > 90:
  print("You got an A!")
  
elif score > 80:
  print("You got a B!")
  
elif score > 70:
  print("You got a C!")
  
else:
  print("Better luck next time!")