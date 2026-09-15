def merge_sort(alist):
  pass

import random
for i in range(100):
  list = []
  for i in range(random.randint(0, 20)):
    list.append(random.randint(-100, 100))
  solution = list[:]
  solution.sort()
  given_answer = merge_sort(list)
  try:
    assert(given_answer == solution)
  except:
    print("\ntest case failed")
    print("Input list: " + str(list))
    print("Your function returned: " + str(given_answer))
    print("The solution was: " + str(solution))
  
print("All test cases passed")
