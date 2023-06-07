#https://www.codingninjas.com/codestudio/problems/3sum_8230739?challengeSlug=striver-sde-challenge

def findTriplets(nums, target):
    result = []
    nums.sort()
    for i in range(len(nums)):
        remainingTarget = target - nums[i]
        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]

            if sum < remainingTarget:
                left += 1
            elif sum > remainingTarget:
                right -= 1
            else:
                x = nums[left]
                y = nums[right]
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == x:
                    left += 1

                while left < right and nums[right] == y:
                    right -= 1

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

    return result
  
  #first i sorted list in ascending order
  #then i iterated through each number and used a two-pointer approach to find the other two numbers that can form the target sum.\
  #If a triplet is found, I added it to the result list
  
  
  
  
