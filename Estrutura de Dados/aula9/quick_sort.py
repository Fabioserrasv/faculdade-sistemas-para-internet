def partition(l, r, nums):
  # Last element will be the pivot and the first element the pointer
  pivot, ptr = nums[r], l
  for i in range(l, r):
      if nums[i] <= pivot:
          # Swapping values smaller than the pivot to the front
          nums[i], nums[ptr] = nums[ptr], nums[i]
          ptr += 1
  # Finally swapping the last element with the pointer indexed number
  nums[ptr], nums[r] = nums[r], nums[ptr]
  return ptr

def quick_sort(nums, r, l):
  if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
      return nums
  if l < r:
      pi = partition(l, r, nums)
      quick_sort(l, pi-1, nums)  # Recursively sorting the left values
      quick_sort(pi+1, r, nums)  # Recursively sorting the right values
  return nums