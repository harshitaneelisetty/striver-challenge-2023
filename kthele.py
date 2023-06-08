#https://www.codingninjas.com/codestudio/problems/kth-element-of-two-sorted-arrays_8230824?challengeSlug=striver-sde-challenge

  def ninjaAndLadoos(arr1, arr2, n, m, k):
        pointer1 = 0
        pointer2 = 0
        count = 1
        while pointer1 < n and pointer2 < m:
            if count == k:
                return min(arr1[pointer1], arr2[pointer2])
            if arr1[pointer1] < arr2[pointer2]:
                pointer1 += 1
            else:
                pointer2 += 1
            count += 1
        while pointer1 < n:
            if count == k:
                return arr1[pointer1]
            pointer1 += 1
            count += 1
        while pointer2 < m:
            if count == k:
                return arr2[pointer2]
            pointer2 += 1
            count += 1
     
    #I used two pointer techinque
    #i took 2 pointers ptr1 refers to first arr and ptr2 refers to second arra
    #i compare the value of two arrays at particular point and incremented the value of pointers accordingly
    #i iteratively done the process until count is equal to k or ptr1 or ptr2 exceeds the length
    #after breaking of while loops i searched for arrays seperately
       
      
      
      
      
      
