
# basic function for calculating something
def double_then_square(x):
  x = 2*x
  x = x**x
  print("This will run")
  return x
  print("this wont run")

print("\nRunning double then square")
print(double_then_square(-10))


# iterative countdown function
def iterative_countdown(n):
  x = n
  for i in range(n):
    print(x)
    x = x - 1

print("\nRunning iterative countdown")
iterative_countdown(20)


# recursive countdown
def recursive_countdown(n):
  # base case AKA exit condition
  if n == 0:
    return
  
  # main part
  print(n)
  
  # recursive call
  recursive_countdown(n-1)

print("\nRunning recursive countdown")
recursive_countdown(10)

def test_double_then_square():
  assert double_then_square(0) == 0
  assert double_then_square(-5) == 100
  assert double_then_square(10) == 400
  
test_double_then_square()