#https://www.codingninjas.com/codestudio/problems/kth-largest-element-in-the-unsorted-array_8230740?challengeSlug=striver-sde-challenge

def kthLargest(arr, size, k):
    arr = sorted(arr, reverse=True)
    return arr[k - 1]
  
#just i sorted k-1th element which is the kth largest element in array
