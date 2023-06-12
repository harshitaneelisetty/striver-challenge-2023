#https://www.codingninjas.com/codestudio/problems/count-distinct-element-in-every-k-size-window_8230749?challengeSlug=striver-sde-challenge

def countDistinctElements(A, k):
    n = len(A)
    ans = []
    mp = {}
    j = 0
    i = 0
    while j < n:
        mp[A[j]] = mp.get(A[j], 0) + 1
        
        if j - i + 1 == k:
            ans.append(len(mp))
            mp[A[i]] -= 1
            if mp[A[i]] == 0:
                del mp[A[i]]
            i += 1
        j += 1
    return ans
  
  #i counted the number of distinct elements in each subarray of A of length k
  #and i stored the count in a list ans
  #i used dictionary mp to keep track of the frequency of each element in the current subarray
  #and i updated it as the subarray slides through the main list
  
  
  
  
  
  
  
  
  
