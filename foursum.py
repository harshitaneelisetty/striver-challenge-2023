#https://www.codingninjas.com/codestudio/problems/find-four-elements-that-sums-to-a-given-value_8230785?challengeSlug=striver-sde-challenge

def fourSum(nums, target, n):
    nums.sort()
    res = []
    
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            l = j + 1
            r = n - 1
            while l < r:
                foursum = nums[i] + nums[j] + nums[l] + nums[r]
                if foursum < target:
                    l += 1
                elif foursum > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            if len(res) > 0:
                return "Yes"
    
    return "No"
  
#I  found all unique quadruplets in the list whose sum is equal to the target.
# I used bested loops to iterate over all possible combo of four numbers
# I used two pointers l and r to search for target sum









