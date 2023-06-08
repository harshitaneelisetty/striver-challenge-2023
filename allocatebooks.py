#https://www.codingninjas.com/codestudio/problems/allocate-books_8230810?challengeSlug=striver-sde-challenge

def ispossible(arr, N, M, mid):
    studentcount = 1
    pagesum = 0
    for i in range(N):
        if pagesum + arr[i] <= mid:
            pagesum += arr[i]
        else:
            studentcount += 1
            if studentcount > M or arr[i] > mid:
                return False
            pagesum = arr[i]
    return True

def ayushGivesNinjatest(M, N, arr):
    if N < M:
        return -1  
    low = max(arr) 
    high = sum(arr) 
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if ispossible(arr, N, M, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

  #i observed its a kind of min-max problem so i applied binary search to solve the problem
  #I created ispossible function to check if it is possible to allocate the books to M students 
  #in a way that each student reads at most mid pages
  #in the main function i used binary search to find the minimum possible value of mid that satisfies the allocation condition
  
  
  
  

