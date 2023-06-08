#https://www.codingninjas.com/codestudio/problems/maximum-in-sliding-windows-of-size-k_8230772?challengeSlug=striver-sde-challenge

from collections import deque

def slidingWindowMaximum(nums, k):
    window = deque()
    n = len(nums)
    result = []

    for i in range(k):
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)

    for i in range(k, n):
        result.append(nums[window[0]])
        while window and window[0] <= i - k:
            window.popleft()
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)

    result.append(nums[window[0]])

    return result
  
#I used deque. i firstly initialised empty deque to store indices. and also initialised empty list to store the max values values for each sliding window
#first i iterated from 0 to k and populated initial window. 
#i removed indices from the back of the deque as long as the corresponding values in nums are smaller than or equal to the current value
#then i appended current idx i to the deque
#secondly i iterated loops from k to n - 1.
#i appended the ma val in current window to the res. and i removed indices from the front of the deque if they are outside the current window
#next i removed indices from the back of the deque as long as the corresponding values in nums are smaller than or equal to the current value.
#finally i appended the current id i to deque
#after loop i appended max value in the last window to the res list
  
  
  
  
  
  
  
  
