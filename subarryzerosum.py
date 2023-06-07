#https://www.codingninjas.com/codestudio/problems/longest-subarray-zero-sum_8230747?challengeSlug=striver-sde-challenge

def LongestSubsetWithZeroSum(A):
    mp = {}
    mx = 0
    sum = 0

    for i in range(len(A)):
        sum += A[i]
        if sum == 0:
            mx = i + 1
        else:
            if sum in mp:
                mx = max(mx, i - mp[sum])
            else:
                mp[sum] = i

    return mx
  
  #I used  a dictionary mp to keep track of the cumulative sum encountered so far and its corresponding index
  #I also maintained a variable mx to store the maximum length of the subset.
  #then I iterated  over each element in the list and updates the cumulative sum by adding the current element
  # If the sum becomes zero, it means that the subset from the beginning of the list to the current index has a zero sum. In this case, the length of the subset is updated as i + 1.
  #If the sum is not zero, it checks if the sum exists in the dictionary.
  #If it does, it means that there is a subarray with a zero sum between the previous occurrence of the same sum and the current index
  #n this case, the length of the subset is updated as i - mp[sum].
