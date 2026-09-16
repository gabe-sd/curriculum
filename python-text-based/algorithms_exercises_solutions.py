"""
Given the list nums, for each nums[i] find out how many numbers
in the array are small than it. That is, for each nums[i] you have to 
count the number of valid j's such that j != i and nums[j] < nums[i]

Return the answer in an array

Example 1:
Input: nums = [8, 1, 2, 2, 3]
Output: [4, 0, 1, 1, 3]
"""
def smallerNumbersCount(nums):
  solution = []
  for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
      if nums[j] < nums[i]:
        count += 1
    solution.append(count)
  return solution
  
assert smallerNumbersCount([]) == []
assert smallerNumbersCount([0]) == [0]
assert smallerNumbersCount([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
print("smalerNumbersCount tests passed")
