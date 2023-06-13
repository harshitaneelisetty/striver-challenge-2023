#https://www.codingninjas.com/codestudio/problems/longest-common-subsequence_8230681?challengeSlug=striver-sde-challenge

def lcs(text1, text2) :
	dp = [[-1 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
	def helper(idx1, idx2, text1, text2, dp):
		if idx1 < 0 or idx2 < 0:
			return 0
		if dp[idx1][idx2] != -1:
			return dp[idx1][idx2]
		if text1[idx1] == text2[idx2]:
			dp[idx1][idx2] = 1 + helper(idx1 - 1, idx2 - 1, text1, text2, dp)
			return dp[idx1][idx2]
		else:
			dp[idx1][idx2] = max(helper(idx1 - 1, idx2, text1, text2, dp), helper(idx1, idx2 - 1, text1, text2, dp))
			return dp[idx1][idx2]
	return helper(len(text1) - 1, len(text2) - 1, text1, text2, dp)

#here i used dp and memoization technique
#i staeted from back and idx1 and idx 2 went less than 0 i returned 0
#if the value is already calculated i returned that value
#if letters at idx1 and idx2 are same i moved to next index
#else there are 2 cases either moving idx1 or idx 2 i considered both cases and returned value

