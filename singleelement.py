#https://www.codingninjas.com/codestudio/problems/single-element-in-a-sorted-array_8230826?challengeSlug=striver-sde-challenge

def singleNonDuplicate(nums):
    n = len(nums)
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
            left = mid + 1
        else:
            right = mid
    return nums[left]
  
  #i checked if the middle element is equal to its adjacent elements
  #if  mid is odd and nums[mid] is equal to nums[mid-1] 
  #or mid is even and nums[mid] is nums[mid-1] I moved to right
  #else moved to left
