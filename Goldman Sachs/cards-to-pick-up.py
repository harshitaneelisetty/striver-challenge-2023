# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minPick = float('inf')
        hashMap = {}
        for idx, ele in enumerate(cards):
            if ele in hashMap:
                if idx - hashMap[ele] + 1 <= minPick:
                    minPick = idx - hashMap[ele] + 1
            hashMap[ele] = idx
        return minPick if minPick != float('inf') else -1
      
      # I used sliding window technique
      # I Kept the index of current number , If current number is in hashMap, then I calculated the length from previously seen index
      # and updated if its difference is smaller than minPick   
      # At the end of iteration, if minPick is not updated ie, its value is float('inf') we can return -1
