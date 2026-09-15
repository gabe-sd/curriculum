def merge_sort(alist):
  # if more than 1 element in list:
  if len(alist) > 1:
    # split list into left and right halves
    mid = len(alist)//2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]
    
    # recursive calls on left and right half lists
    merge_sort(lefthalf)
    merge_sort(righthalf)
    
    # sorting algorithm
    
    # i = left index
    # j = right index
    # k = alist index
    i, j, k = 0, 0, 0
    
    # until we reach the end of one of the lists
    while i < len(lefthalf) and j < len(righthalf):
      
      # if the next item in the left list is smaller
      if lefthalf[i] < righthalf[j]:
        alist[k] = lefthalf[i]
        i += 1
        
      # if the next item in the right list is smaller or they are equal
      else:
        alist[k] = righthalf[j]
        j += 1
      
      # completed one round of merging, increment alist index
      k += 1
      
    # after merging finished, add remaining items to list
    while i < len(lefthalf):
      alist[k] = lefthalf[i]
      i += 1
      k += 1
      
    while j < len(righthalf):
      alist[k] = righthalf[j]
      j += 1
      k += 1
      
  return alist


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