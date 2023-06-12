#https://www.codingninjas.com/codestudio/problems/median-in-a-stream_8230765?challengeSlug=striver-sde-challenge

def findMedian(arr, n):
    medians = []
    lo = PriorityQueue()
    hi = PriorityQueue()

    for i in range(n):
        num = arr[i]
        lo.put(num)
        temp = lo.get()
        hi.put((-temp, temp))

        if lo.qsize() < hi.qsize():
            temp_pair = hi.get()
            lo.put(temp_pair[1])

        median = 0

        if lo.qsize() > hi.qsize():
            median = lo.queue[0]
        else:
            median = (lo.queue[0] + hi.queue[0][1]) // 2

        medians.append(median)

    return medians
  
#i calculated the medians of all subarrays of arr and returned them as a list
#i used two priority queues, lo and hi, to maintain the elements of the subarray
#lo contains the smaller half of the elements
#hi contains larger half of the elements
#i calculated median based on the sizes of lo and hi, and it is added to the list of medians

  
  
  
  
  
  
  
  
  
  
  
