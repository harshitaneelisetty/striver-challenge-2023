# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/


class Solution:
    def getMinBreakPoint(self, nums, mn):
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                mn = min(mn, nums[i])
        return mn
    
    def getMaxBreakPoint(self, nums, mx):
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                mx = max(mx, nums[i])
        return mx
    
    def getIdx1(self, nums, mn):
        n = len(nums)
        for i in range(n):
            if nums[i] > mn:
                idx1 = i
                return idx1
     
    
    def getIdx2(self, nums, mx):
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] < mx:
                idx2 = i
                return idx2

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        mn = float('inf')
        mx = float('-inf')
        mn = self.getMinBreakPoint(nums, mn)
        mx = self.getMaxBreakPoint(nums, mx)
        if mn == float('inf') or mx == float(-inf):
            return 0
        idx1 = self.getIdx1(nums, mn)
        idx2 = self.getIdx2(nums, mx)
        return abs(idx2 - idx1 + 1)
      
      # found the element which is less than the preceding element from left and found element which is greater than the succeding element from right
      #returned the length of that subarray idx2 - idx1 + 1
        
