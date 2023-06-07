#https://www.codingninjas.com/codestudio/problems/reverse-pairs_8230825?challengeSlug=striver-sde-challenge
  
  def merge(nums, low, mid, high):
    count = 0
    j = mid + 1
    for i in range(low, mid + 1):
        while j <= high and nums[i] > 2 * nums[j]:
            j += 1
        count += j - (mid + 1)

    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1

    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= high:
        temp.append(nums[right])
        right += 1

    for i in range(low, high + 1):
        nums[i] = temp[i - low]

    return count


def mergeSort(nums, low, high):
    if low >= high:
        return 0

    mid = (low + high) // 2
    inv = mergeSort(nums, low, mid)
    inv += mergeSort(nums, mid + 1, high)
    inv += merge(nums, low, mid, high)
    return inv


def reversePairs(nums):
    return mergeSort(nums, 0, len(nums) - 1)

 
 
  # I implemented the "Merge Sort" algorithm with an additional step to count the reverse pairs
