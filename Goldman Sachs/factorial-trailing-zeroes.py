# https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 1 or n == 0:
            return 0
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        fact = str(fact)[::-1]
        count = 0
        for i in fact:
            if i == '0':
                count += 1
            else:
                return count
        return count
