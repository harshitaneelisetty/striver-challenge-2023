# https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        lst = Counter(words)
        heap = [[-val, key] for key, val in lst.items()]
        heapq.heapify(heap)
        frequent_words = []
        count = 0
        while(count < k):
            frequent_words.append(heapq.heappop(heap)[1])
            count += 1
        return frequent_words
      
     #I created a max heap with val and key
    # I keep on poping values until heap contains only k values
