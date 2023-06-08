#https://www.codingninjas.com/codestudio/problems/matrix-median_8230735?challengeSlug=striver-sde-challenge

def upper_bound(arr, first, last, val):
    low = first
    high = last
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > val:
            high = mid
        else:
            low = mid + 1
    return low


def getMedian(matrix):
    n = len(matrix)
    m = len(matrix[0])
    low = 1
    high = 100000
    while low < high:
        mid = (low + high) // 2
        count = 0
        for i in range(n):
            count += upper_bound(matrix[i], 0, len(matrix[i]), mid)
        if count >= (n * m + 1) // 2:
            high = mid
        else:
            low = mid + 1
    return low
  
#I used binary search algorithm 
#Icreated upper bound function to count the number of elements in the matrix that are less than or equal to a given value
# then i adjusted the search range accordingly i compared count with n * m + 1 // 2
#if count is more then i decreased search space to left of mid else right of mid
  
  
