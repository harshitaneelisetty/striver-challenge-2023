# https://leetcode.com/problems/sort-an-array/description/

#Solution 1:
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        ans = []
        heapq.heapify(heap)
        for i in nums:
            heapq.heappush(heap, i)
        while heap:
            ans.append(heapq.heappop(heap))
        return ans
      
      #used heaps to solve
      
#Solution 2:
class Solution(object):
    def sortArray(self, nums):
        return sorted(nums)
      
      #used builtin function to solve
     
