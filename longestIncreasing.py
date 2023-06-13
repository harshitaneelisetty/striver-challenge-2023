#https://www.codingninjas.com/codestudio/problems/longest-increasing-subsequence_8230689?challengeSlug=striver-sde-challenge

  def longestIncreasingSubsequence(nums, n) :
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect.bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)
      
#i used a dynamic programming approach to efficiently find and update the longest increasing subsequence 
#by iterating over the nums list
#i used bisect.bisect_left() function to perform a binary search to find the appropriate position to insert or replace elements in the sub list
