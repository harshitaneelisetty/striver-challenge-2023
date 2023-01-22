# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        sol = []
        def dfs(temp, n, count):
            if (temp > n):
                return
            sol.append(temp)
            if count == k - 1:
                return temp
            count += 1
            dfs(temp * 10, n, count)
            if (temp % 10 != 9):
                dfs(temp + 1, n, count)
        x = dfs(1, n, 0)
