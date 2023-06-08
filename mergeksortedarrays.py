#https://www.codingninjas.com/codestudio/problems/merge-k-sorted-arrays_8230770?challengeSlug=striver-sde-challenge

import heapq

def mergeKSortedArrays(arrays, k):
    result = []
    min_heap = []
    for i in range(len(arrays)):
        heapq.heappush(min_heap, (arrays[i][0], i, 0))
    while min_heap:
        curr = heapq.heappop(min_heap)
        value = curr[0]
        array_index = curr[1]
        element_index = curr[2]

        result.append(value)

        if element_index + 1 < len(arrays[array_index]):
            heapq.heappush(min_heap, (arrays[array_index][element_index + 1], array_index, element_index + 1))

    return result
  
  #i started by initialising an empty res array and a min_heap to store the smallest elements from each array.
  #in first loop i pushed the first element from each array into min_hrap along with their corresponding array index and element index.
  #then i iterated unitl min_heap is empty 
  #in each iteration i poped the smallest element from the min_hrap and extracted val, array idx and ele idx
  #i append it into the res
  #if there are more elements in curr array then i pushed the next eleent into min heap and increent elemt idx by 1
 
  
  
  
  
  
  
  
  
  
  
  
