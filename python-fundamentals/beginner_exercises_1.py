from random import*

# 1
print("Hello!")

# 2 
print("What " * 5)

# 3
number = 10
print(number)

# 4 
number = 96 - 35
print(number)

# 5
number = randint(1, 100)
print(number)

# 6
name = input("What's your name?")
print("Hi " + name + ", it's nice to meet you!")

# 7
number = randint(1, 10)
guess = int(input("Pick a number between 1 and 10"))
if number == guess:
  print("Good job! You guessed right")
else:
  print("Good try but that's not it! The number I was think of was " + str(number))
  
# 8
number = choice([1, 2, 3, 4, 5])
for guesses in range(3):
  guess = int(input("Pick a number between 1 and 5. You have 3 tries to get it right."))
  if guess == number:
    print("Great job! You guessed right!")
    break
  else:
    print("That's not it")
  