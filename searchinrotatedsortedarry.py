#https://www.codingninjas.com/codestudio/problems/search-in-rotated-sorted-array_8230687?challengeSlug=striver-sde-challenge

def search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[start]:
            if nums[start] <= target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[end] >= target >= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1
  
  #i used binary search to find the element
  #i compared the first element and mid element and the last element
  #if mid element is greater than start element and target element lies between start and mid,
  #I moved end to mid - 1 else i moved to right
  #then i compared end element, targer and mid, if target lies between mid and end, i moved to right
  #else i oved to left


