# https://leetcode.com/problems/top-k-frequent-words/

# Brute force
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        lst = Counter(sorted(words))
        lst = sorted(lst.items(), key = lambda x : x[1], reverse = True)
        return [i[0] for i in lst[ : k]]
      
#simply i used the counter function

#optimized(Using heaps)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        lst = Counter(lst)
        heap = [[-val, key] for key, val in lst.items()]
        heapq.heapify(heap)
        frequentWords = []
        count = 0
        while(count < k):
            frequentWords.append(heapq.heappop(heap)[1])
            count += 1
        return frequentWords
