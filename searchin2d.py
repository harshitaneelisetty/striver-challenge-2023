#https://www.codingninjas.com/codestudio/problems/search-in-a-2d-matrix_8230773?challengeSlug=striver-sde-challenge

def searchMatrix(matrix: [[int]], target: int) -> bool:
    low = 0
    high = len(matrix) * len(matrix[0]) - 1
    n = len(matrix[0])
    while low <= high:
        mid = (low + high) // 2
        if matrix[mid // n][mid % n] == target:
            return True
        elif matrix[mid // n][mid % n] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
  #I used binary search
  #I flattened matrix by treating it as a 1D array. 
  #I initialized low and high as the start and end indices of the flattened array and repeatedly calculates the middle index (mid). 
  #I compared the value at the middle index with the target value and adjusts low and high accordingly
  
