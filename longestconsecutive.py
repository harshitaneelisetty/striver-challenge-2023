#https://www.codingninjas.com/codestudio/problems/longest-consecutive-sequence_8230708?challengeSlug=striver-sde-challenge

def lengthOfLongestConsecutiveSequence(nums, n):
    maxLength = 0
    uniqueNums = set(nums)

    for num in nums:
        if num - 1 not in uniqueNums:
            currentLength = 1
            while num + 1 in uniqueNums:
                num += 1
                currentLength += 1
            maxLength = max(maxLength, currentLength)

    return maxLength
  
  #I made a set of all number in list
  #I iterated over each number in the list and checks if the previous number (num - 1) is not in the set
  #If it is not present, I started counting the length of the consecutive sequence by incrementing the number (num + 1) and checked if it exists in the set
  #I updated the max length
