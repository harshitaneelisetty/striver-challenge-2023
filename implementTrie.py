#https://www.codingninjas.com/codestudio/problems/implement-trie_8230696?challengeSlug=striver-sde-challenge


class Node:
    def init(self):
        self.links = [None] * 26
        self.flag = False

    def containKey(self, ch):
        return self.links[ord(ch) - ord('a')] != None

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def setEnd(self):
        self.flag = True

    def isEnd(self):
        return self.flag
    class Trie:
    def init(self):
        self.root = Node()
    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
        node.setEnd()

    def search(self, word):
        node = self.root
        for ch in word:
            if not node.containKey(ch):
                return False
            node = node.get(ch)
        return node.isEnd()

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if not node.containKey(ch):
                return False
            node = node.get(ch)
        return True

#i created a trie class which reprsents a node in a trie. 
#Each node contains an array of links i used to reference to the child nodes for all chracters.
#i used flag value in the node class to indicate end of word
#in insert method i iterated over each char in the word and created a new node if node is not presen
#At the end of the word, i called setEnd method to mark the node as the end of a word.
#in search methid i traversed the trie by following links for each character in word
#i used same approach for startswith method as teh seach method, 
#but it only checks if the given prefix exists in the trie
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      

