#https://www.codingninjas.com/codestudio/problems/kth-largest-element-in-a-stream_8230728?challengeSlug=striver-sde-challenge

class KthLargest:
        
    def __init__(self, k, arr):
        self.size = k
        self.pq = []
        heapq.heapify(self.pq)
        
        for item in arr:
            heapq.heappush(self.pq, item)
            
            if len(self.pq) > self.size:
                heapq.heappop(self.pq)
            
    def add(self, num):
        heapq.heappush(self.pq, num)
            
        if len(self.pq) > self.size:
            heapq.heappop(self.pq)
    
    def getKthLargest(self):
        return self.pq[0]
      
 #i initialised a priority queue with a given size k
 #i created priority queue using heapq.heapify() function to maintain the smallest k elements
  #in add() methid i added a new num to the priority queue, ensuring that it remains of size k
  #in getKthLargest() method i returned the smallest element in the priority queue, which represents the kth largest element overall
  
      
  
  
  
  
  
  
  
  
  
  
  
  
