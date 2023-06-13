#https://www.codingninjas.com/codestudio/problems/minimum-path-sum_8230791?challengeSlug=striver-sde-challenge

   def minSumPath(grid):
        m = len(grid[0])
        n = len(grid)
        dp = [[-1 for j in range(m)] for i in range(n)]
        def helper(row, col, grid, dp):
            if row == 0 and col == 0:
                return grid[row][col]
            if dp[row][col] != -1:
                return dp[row][col]
            if row < 0 or col < 0:
                return float('inf')
            up = grid[row][col] + helper(row - 1, col, grid, dp)
            down = grid[row][col] + helper(row, col - 1, grid, dp)
            dp[row][col] = min(up, down)
            return dp[row][col]
        return helper(n - 1, m - 1, grid, dp)
      
  #i used memoization approach and for each index i explored all the possibilities
  #for one idx there is up and down so i explored both ways and stored the min value at dp
  #i stopped when row or col is 0 and i took this as a base condition 
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
