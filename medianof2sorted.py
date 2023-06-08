#https://www.codingninjas.com/codestudio/problems/median-of-two-sorted-arrays_8230788?challengeSlug=striver-sde-challenge

def median(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    size1 = len(nums1)
    size2 = len(nums2)
    low = 0
    high = size1

    while low <= high:
        mid = (low + high) // 2
        part = (size1 + size2 + 1) // 2 - mid

        if part > size2:
            low = mid + 1
            continue

        leftMax = 0
        rightMin = float('inf')
        if mid > 0:
            leftMax = max(leftMax, nums1[mid - 1])

        if part > 0:
            leftMax = max(leftMax, nums2[part - 1])

        if mid < size1:
            rightMin = min(rightMin, nums1[mid])

        if part < size2:
            rightMin = min(rightMin, nums2[part])

        if leftMax <= rightMin:
            if (size1 + size2) % 2 == 1:
                return leftMax
            return (leftMax + rightMin) / 2.0

        if nums1[mid] < leftMax:
            low = mid + 1
        else:
            high = mid - 1

    return -1
  
#i used binary search approach to solve
#i searched for the partitioning point in nums1 and nums2 
#such that the elements on the left side are smaller than the elements on the right side
#and then i determined the median based on the maximum of the left side and the minimum of the right side
#i iteratively performed search by adjusting the search range until median is found
  
  
  
  
