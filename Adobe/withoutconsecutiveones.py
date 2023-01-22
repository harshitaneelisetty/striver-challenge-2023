# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/description/

class Solution:
    def findIntegers(self, n: int) -> int:
        first, second = 1, 2
        n = n + 1
        res = 0
        while n:
            if n & 1 and n & 2:
                res = 0
            res += (first * (n & 1))
            n = n >> 1
            #print(n, res)
            first, second = second, first + second
            #print(first, second)
        return res
      
      # used fibocii approach to solve the problem 
