#https://www.codingninjas.com/codestudio/problems/next-permutation_8230741?challengeSlug=striver-sde-challenge

def nextPermutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i < 0:
        nums.reverse()
    else:
        l = n - 1
        while l >= 0 and nums[i] >= nums[l]:
            l -= 1
        nums[i], nums[l] = nums[l], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])
    return nums

 #I found the next lexicographically greater permutation of a given list of numbers 
 #I searched for a specific pattern and applied swapping and reversing operations on the list.
