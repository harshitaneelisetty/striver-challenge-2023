# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/description/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        res = 0
        temp = [nums1[0] - nums2[0] - diff]
        for i in range(1, n):
            idx = bisect.bisect_right(temp, nums1[i] - nums2[i])
            if idx == 0 and temp[0] == nums1[i] - nums2[i]:
                res += 1
            elif idx == n:
                res += n
            elif idx < i and temp[idx] == nums1[i] - nums2[i]:
                res += idx + 1
            else:
                res += idx
            temp.insert(bisect.bisect_left(temp, nums1[i] - nums2[i] - diff), nums1[i] - nums2[i] - diff)
        return res
      
     # I changed given equation as nums1[i] - nums2[i] - diff <= nums2[j] - nums2[j]
     # I took a list temp and appended nums1[i] - nums2[i] - diff
     # Every time I search for nums2[j] - nums2[j] in the temp and count the res
     # and now I inserted nums1[i] - nums1[i] - diff into the temp using insertion step of insertion sort using binary search
