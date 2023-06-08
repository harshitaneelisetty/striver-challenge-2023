#https://www.codingninjas.com/codestudio/problems/day-29-k-max-sum-combinations_8230768?challengeSlug=striver-sde-challenge

import heapq

def kMaxSumCombination(array1, array2, size, k):
    array1.sort()
    array2.sort()

    maxHeap = []
    heapq.heappush(maxHeap, (array1[size - 1] + array2[size - 1], size - 1, size - 1))

    mySet = set()
    mySet.add((size - 1, size - 1))

    result = []

    while k > 0:
        top = heapq.heappop(maxHeap)

        sum_val = top[0]
        x = top[1]
        y = top[2]

        result.append(sum_val)

        if (x - 1, y) not in mySet:
            heapq.heappush(maxHeap, (array1[x - 1] + array2[y], x - 1, y))
            mySet.add((x - 1, y))
        if (x, y - 1) not in mySet:
            heapq.heappush(maxHeap, (array1[x] + array2[y - 1], x, y - 1))
            mySet.add((x, y - 1))
        k -= 1

    return result
  
  #i sorted the arrays in asending order
  #i used a max heap and i implemented it using heapq to store the pairs of sums and corresponding indices
  #and i used a set to keep track of the indices that have been already processed.
  #i iterated function k times. in each iteration i retrived top element from the max heap which is the max sum
  #i added this sum to the res array
  #and i checked if the indices x-1, y and x, y - 1 are present in the set
  #if nit, i calculated the sums of the corresponding elemnts from array1 and array2
  #and added them to the max-heap with the updated indices and insserted the eindices into the set

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

