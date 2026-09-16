def countdown(x):
  if x < 0:
    return

  print(x)
  countdown(x-1)
  
countdown(5)