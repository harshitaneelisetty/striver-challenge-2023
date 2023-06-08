#https://www.codingninjas.com/codestudio/problems/lru-cache-implementation_8230697?challengeSlug=striver-sde-challenge

class LRUCache:
    def init(self, capacity):
        self.capacity = capacity
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.map = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._insert(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        if key in self.map:
            self._remove(self.map[key])
        if len(self.map) == self.capacity:
            self._remove(self.tail.prev)
        self._insert(self.Node(key, value))

    def _remove(self, node):
        del self.map[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node):
        self.map[node.key] = node
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

  class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
            
  #lru chache means least recently used. i implemented lru chache using double linkedlist
  #i created a two pinters head and tail
  #in get functions i retrived the value from the node if val is present else retuned -1
  #if val is present that node was the recently used node so i removed that node and appened first to the head
  #in put function i appened key and value to head of linkedlist if value is not present else i removed node and appenedto head
  #init function initialises object and capacity
  #in put function if capacity was full i removed tail node and appended new node to head
   
  
  
  
  
  
  
  
