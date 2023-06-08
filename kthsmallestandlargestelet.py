#https://www.codingninjas.com/codestudio/problems/kth-smallest-and-largest-element-of-array_8230829?challengeSlug=striver-sde-challenge

def kthSmallLarge(arr, n, k):
    arr.sort()
    return [arr[k - 1], arr[n - k]]
  
  #i just sorted and took the k-1th element
