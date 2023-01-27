# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/description/

class Solution:
    def helper(self, start, end, k, idx, dp):
        if idx == 0:
            if start == end:
                return 1
            return 0
        if abs(end - start) > idx:
            return 0
        if dp[start + 1000][idx] != -1:
            return dp[start + 1000][idx] % (10 ** 9 + 7)
        left = self.helper(start - 1, end, k, idx - 1, dp) 
        right = self.helper(start + 1, end, k, idx - 1, dp)
        dp[start + 1000][idx] = (left + right) % (10 ** 9 + 7)
        return dp[start + 1000][idx]

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        dp = [[-1 for _ in range(k + 2)] for _ in range(5000)]
        return self.helper(startPos, endPos, k, k, dp)
      
      #here i declared 5000 becoz the constraints size is big
      # here just i explored the all possibilites of particular point
      # possibilites -> we can move left or we can move right
