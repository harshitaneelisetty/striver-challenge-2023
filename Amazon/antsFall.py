# https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/description/


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left = sorted(left)
        right = sorted(right)
        if len(right) == 0:
            return left[-1]
        if len(left) == 0:
            return n - right[0]
        return max(n - right[0], left[-1])
      
      
