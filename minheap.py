#https://www.codingninjas.com/codestudio/problems/min-heap_8230863?challengeSlug=striver-sde-challenge

def get_left_child(k):
    return 2 * k + 1

def get_right_child(k):
    return 2 * k + 2

def get_parent(k):
    return (k - 1) // 2

def heapify(heap, k, size):
    left_child = get_left_child(k)
    right_child = get_right_child(k)
    smallest = k

    if left_child < size and heap[left_child] < heap[k]:
        smallest = left_child

    if right_child < size and heap[right_child] < heap[smallest]:
        smallest = right_child

    if smallest != k:
        heap[k], heap[smallest] = heap[smallest], heap[k]
        heapify(heap, smallest, size)

def insert(heap, val, size):
    heap[size] = val
    i = size
    size += 1

    while i != 0 and heap[get_parent(i)] > heap[i]:
        heap[i], heap[get_parent(i)] = heap[get_parent(i)], heap[i]
        i = get_parent(i)

def extract_min(heap, size):
    if size == 1:
        size -= 1
        return heap[0]

    val = heap[0]
    heap[0] = heap[size - 1]
    size -= 1
    heapify(heap, 0, size)

    return val

def minHeap(n, queries):
    size = 0
    heap = [0] * n
    ans = []

    for i in range(n):
        if queries[i][0] == 0:
            insert(heap, queries[i][1], size)
        else:
            ans.append(extract_min(heap, size))

    return ans

  #in heapify function i took an heap, and a current idx k and the size of heap
  #i compared the value at index k with its left and right child nodes
  #and if necessary i swaped the value to maintain the min-heap property.
  #the i recursively called heapify on the affected child node
  #in insert function i added a new value to the heap
  #i placed value at the end of the heap and updated the size and then i adjusted the position repetedly
  #swapping it with its parent as long as the parent's value is greater.
  #in extract_min function i removed min value from the heap. 
  #i placed root value with the last value in the heap, reduced the size
  #in min heap function i took number of queries and a list of queries
  #i initialized an emapt heap and a list to store the extracted min values
  #for each query if it is an extract operation, the minimum value is extracted using extract_min
  #and added to the result list
  
  
  
  
  






