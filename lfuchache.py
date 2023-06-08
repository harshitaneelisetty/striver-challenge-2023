#https://www.codingninjas.com/codestudio/problems/lfu-cache_8230851?challengeSlug=striver-sde-challenge

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = self.next = self

class DoubleLinkedList:
    def __init__(self):
        self.rootNode = Node(0, 0) 
        self.rootNode.next = self.rootNode.prev = self.rootNode
        self.currentSize = 0

    def __len__(self):
        return self.currentSize

    def append(self, node):
        node.next = self.rootNode.next
        node.prev = self.rootNode
        node.next.prev = node
        self.rootNode.next = node
        self.currentSize += 1

    def pop(self, node=None):
        if self.currentSize == 0:
            return

        if not node:
            node = self.rootNode.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.currentSize -= 1

        return node

class LFUCache:
    def __init__(self, capacity):
        self.currentSize = 0
        self.capacity = capacity
        self.nodeMap = dict()
        self.freqMap = collections.defaultdict(DoubleLinkedList)
        self.minFreq = 0

    def updateNodeFreq(self, node):
        freq = node.freq
        self.freqMap[freq].pop(node)

        if self.minFreq == freq and not self.freqMap[freq]:
            self.minFreq += 1

        node.freq += 1
        freq = node.freq
        self.freqMap[freq].append(node)

    def get(self, key):
        if key not in self.nodeMap:
            return -1

        node = self.nodeMap[key]
        self.updateNodeFreq(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.updateNodeFreq(node)
            node.value = value
            return

        if self.currentSize == self.capacity:
            node = self.freqMap[self.minFreq].pop()
            del self.nodeMap[node.key]
            self.currentSize -= 1

        node = Node(key, value)
        self.nodeMap[key] = node
        self.freqMap[1].append(node)
        self.minFreq = 1
        self.currentSize += 1
        
#i created node class to represnt a node in the cache. Each node has a key, value, frequency, and references to the previous and next nodes.
#The frequency represents how many times the node has been accessed
#i created DoubleLinkedList class to represents a doubly linked list used to store the nodes. 
#It has methods to append a node at the front of the list and to remove a specified node from the list.
#in init method i initialized cache with a given capacity
#and i created an empty cache with the specified capacity and initialized the node map, frequency map, and minimum frequency
#in updateNodeFreq method i updated the frequency of a given node and i removed the node from its current frequency list, increments its frequency, and appended it to the list with the new frequency  
#If the node had the minimum frequency and the list becomes empty and i updated min feq
#in get method i retrived the valueassociated with a given key from the cache. If the key exists in the cache.
#i updated the node's frequency, moves the node to the list with the new frequency, and returned the value. If the key is not found, it returns -1.
#in put function i inserted key value pair into the cache.
#If the key already exists, i updated the value and updated the node's frequency, and moveed the node to the list with the new frequency





        
        
        
        
        
        
        
        
