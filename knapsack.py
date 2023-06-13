#https://www.codingninjas.com/codestudio/problems/0-1-knapsack_8230801?challengeSlug=striver-sde-challenge

  def knapsackUtil(wt, val, ind, W, dp):
        if ind == 0:
            if wt[0] <= W:
                return val[0]
            else:
                return 0
        if dp[ind][W] != -1:
            return dp[ind][W]
        notTaken = 0 + knapsackUtil(wt, val, ind-1, W, dp)
        taken = -sys.maxsize
        if wt[ind] <= W:
            taken = val[ind] + knapsackUtil(wt, val, ind-1, W-wt[ind], dp)
        dp[ind][W] = max(notTaken, taken)
        return dp[ind][W]

  def maxProfit(val, wt, n, W):
        dp = [[-1 for j in range(W + 1)] for i in range(n)]
        return knapsackUtil(wt, val, n - 1, W, dp)
      
   #i used knapsackUtil as a helper function to recursively calculate the maximum profit that can be obtained by choosing items from val and wt lists, given a weight capacity W
   #i stored the results in a 2D dp table to avoid redundant computation
   #in maxProfit function i initialized the dp
   #and called the knapsackUtil function to obtain the maximum profit
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
