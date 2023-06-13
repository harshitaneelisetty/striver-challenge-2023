#https://www.codingninjas.com/codestudio/problems/rod-cutting-problem_8230727?challengeSlug=striver-sde-challenge

def helper(price, ind, N, dp):
    if ind == 0:
        return N * price[0]
    
    if dp[ind][N] != -1:
        return dp[ind][N]
    
    notTaken = 0 + helper(price, ind - 1, N, dp)
    
    taken = float('-inf')
    rodLength = ind + 1
    if rodLength <= N:
        taken = price[ind] + helper(price, ind, N - rodLength, dp)
    
    dp[ind][N] = max(notTaken, taken)
    return dp[ind][N]


def cutRod(price, N):
    dp = [[-1 for _ in range(N + 1)] for _ in range(N)]
    return helper(price, N - 1, N, dp)

#if ind is 0, it means there is only one element left in the price list and i returned max value that can be obtained by selling the rod of length N at the given price
#if res of curr idx and N is already calculated i returned directly
#there are two cases for particular indx which is pick and notpick
#if notpick i jsut moved to prev idx without decreasing rod length
#in pick case i added current idx price value and decresed value of idx and rod length
#stored min value of pick and notpick in dp
  
  
  
