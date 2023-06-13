#https://www.codingninjas.com/codestudio/problems/maximum-sum-increasing-subsequence_8230821?challengeSlug=striver-sde-challenge

def solve(arr, n, dp):
    if dp[n] != -1:
        return dp[n]
    
    if n == 0:
        dp[n] = arr[n]
        return dp[n]
    
    res = arr[n]
    for i in range(n):
        if arr[i] < arr[n]:
            res = max(res, solve(arr, i, dp) + arr[n])
    
    dp[n] = res
    return dp[n]

def maxIncreasingDumbbellsSum(rack, n):
    dp = [-1 for _ in range(n)]
    return solve(rack, n - 1, dp)
  
 #in solve function i checked if the result for the current index n is already stored in the dp array before recomputing it
 #i iterated through the range from 0 to n-1 and checked if any element arr[i] is less than arr[n]
 #if arr[i] is less than arr[n] i recursively called 
 #solve with i as the index and addedd arr[n] to the result obtained from the recursive call
 #then res represent max sum of of increasing elements ending at index n
  
  
  
  
  
  
  
  
  
  
