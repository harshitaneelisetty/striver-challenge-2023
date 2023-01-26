# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/description/

class Solution:
    def getMaxStreek(self, nums, hashSet):
        longestStreek = 0
        for i in nums:
            if i - 1 not in hashSet:
                currentStreek = 1
                currentNum = i
                while currentNum + 1 in hashSet:
                    currentNum += 1
                    currentStreek += 1
                longestStreek = max(longestStreek, currentStreek)
        return longestStreek

    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        nums = [i for i in range(bottom, top + 1)]
        for i in special:
            nums.remove(i)
        hashSet = set()
        for i in nums:
            hashSet.add(i)
        return self.getMaxStreek(nums, hashSet)
      
      # first created nums and then removed all specials from nums and find longest consecutive streek
