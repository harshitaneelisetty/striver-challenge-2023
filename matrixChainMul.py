#https://www.codingninjas.com/codestudio/problems/matrix-chain-multiplication_8230769?challengeSlug=striver-sde-challenge

  def helper(i, j, arr, dp):
        if i == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        mini = float('inf')
        for k in range(i, j):
            steps = arr[i - 1] * arr[k] * arr[j] + helper(i, k, arr, dp) + helper(k + 1, j, arr, dp)
            mini = min(steps, mini)
        dp[i][j] = mini
        return dp[i][j]
        
  def matrixMultiplication(arr, N):
    dp = [[-1 for i in range(N)] for j in range(N)]
    return helper(1, N - 1, arr, dp)
  
  #i calculated and returned the minimum number of multiplications needed to multiply the matrices from index i to index j in the arr
  #if i and j are equal it means there is only one matrix so i returned 0
  #if the result for the current indices i and j is already present in the dp array i returned directly
  #i initialized mini as positive infinity
  #i iterated through the range from i to j-1 to consider different partition points for multiplying matrices
  #for each partition point i recursively called helper to calculate the minimum number of multiplications for the left and right subproblems
  #i calculated the num of partitions for the curr partition as arr[i-1] * arr[k] * arr[j]
  #finally i returned minimum number of multiplications for multiplying the matrices from index 1 to N-1
  
  
  
  
  
  
  
  
  
  
  
  
  
