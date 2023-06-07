#https://www.codingninjas.com/codestudio/problems/unique-paths_8230802?challengeSlug=striver-sde-challenge

def uniquePaths(m, n):
	dp = [[0 for _ in range(n + 1)] for j in range(m + 1)]
	def helper(m, n):
		if dp[m][n]:
			return dp[m][n]
		if m == 1 or n == 1:
			return 1
		dp[m][n] = helper(m - 1, n) + helper(m, n - 1)
		return dp[m][n]
	return helper(m, n)

#I used dp to solve the problem
#I used top down approach converted recursion to memoization solution
#I moved up and left and counted number of ways
