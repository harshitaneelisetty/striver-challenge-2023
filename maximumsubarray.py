#https://www.codingninjas.com/codestudio/problems/maximum-subarray-sum_8230694?challengeSlug=striver-sde-challenge

def maxSubarraySum(nums, n) :
    maxi = nums[0]
    sum = nums[0]
    for i in range(1, len(nums)):
        if sum + nums[i] > nums[i]:
            sum += nums[i]
        else:
            sum = nums[i]
        maxi = max(maxi, sum)
    return maxi if maxi > 0 else 0
  
#I used a kadens algoritm
#I found the maximum subarray sum within a given list of numbers
#by iteratively updating the sum of the subarray and keeping track of the maximum sum encountered so far.
#It returns the maximum subarray sum or 0 if all subarray sums are negative.
