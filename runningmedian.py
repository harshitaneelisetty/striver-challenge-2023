#https://www.codingninjas.com/codestudio/problems/running-median_8230682?challengeSlug=striver-sde-challenge

import heapq

def findMedian(arr, n):
    max_heap = []
    min_heap = []
    print()
    for i in range(len(arr)):
        if i == 0:
            heapq.heappush(max_heap, -arr[i])
        else:
            if arr[i] < -max_heap[0]:
                heapq.heappush(max_heap, -arr[i])
            else:
                heapq.heappush(min_heap, arr[i])
        if len(max_heap) - len(min_heap) > 1:
            x = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, x)
        elif len(min_heap) - len(max_heap) > 1:
            x = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -x)

        c = len(max_heap) + len(min_heap)  # count
        if c % 2 == 0:
            median = (-max_heap[0] + min_heap[0]) // 2
            
            print(median, end = " ")
        else:
            if len(max_heap) > len(min_heap):
                median = -max_heap[0]
            else:
                median = min_heap[0]
            print(median, end = " ")
            
            
#i used two heaps a max-heap to store the smaller half of the elements 
#and a min-heap to store the larger half of the elements.
#in each iteration I compared the current element with the top element of max_heap
#if If the current element is smaller, I added it to the max_heap , otherwise, i added it to the min_heap
#then i balanced heaps such that the size diff is atmost 1
#the i calculated median based on the sizes of the heaps
#If the total count of elements is even, the median is the average of the maximum element in max_heap
#and the mini elemnt in min_heap the total count is odd, the median is the maximum element in max_heap if it has more elements
#or the minimum element in min_heap otherwise.












