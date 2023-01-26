# https://leetcode.com/problems/strictly-palindromic-number/description/

class Solution:
    def numberToBase(self, n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]

    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            base = self.numberToBase(n, i)
            #print(base)
            if base != base[::-1]:
                return False
        return True
