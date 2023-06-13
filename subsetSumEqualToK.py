#https://www.codingninjas.com/codestudio/problems/subset-sum-equal-to-k_8230844?challengeSlug=striver-sde-challenge

def subsetSumToK(n, k, arr):
    dp = [[False for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for j in range(1, k + 1):
        dp[0][j] = False
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i - 1] <= j:
                dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]
    return dp[n][k]
  
#here i used tabulation and used dp
