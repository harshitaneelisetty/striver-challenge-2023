#https://www.codingninjas.com/codestudio/problems/implement-trie-ll_8230840?challengeSlug=striver-sde-challenge

class Node:
    def __init__(self):
        self.links = [None] * 26
        self.cntEndWith = 0
        self.cntPrefix = 0

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def increaseEnd(self):
        self.cntEndWith += 1

    def increasePrefix(self):
        self.cntPrefix += 1

    def deleteEnd(self):
        self.cntEndWith -= 1

    def reducePrefix(self):
        self.cntPrefix -= 1

    def getEnd(self):
        return self.cntEndWith

    def getPrefix(self):
        return self.cntPrefix


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
            node.increasePrefix()
        node.increaseEnd()

    def countWordsEqualTo(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return 0
        return node.getEnd()

    def countWordsStartingWith(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return 0
        return node.getPrefix()

    def erase(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
                node.reducePrefix()
            else:
                return
        node.deleteEnd()

#I created two classes node and trie
#node class represents a single node in trie and contains an arr of child nodes
#representing the possible characters that can follows the current node
#i used two counts to keep track of node. i used cntEndWith to count the number of words that end at this node
#i used cntPrefix to count the number of words that have this node as a prefix
#i created trie class and created root node as a starting point.
#insert method used to insert word by iterating over each character and created new nodes as needed
#in countWordsEqualto method i counted the number of words in the Trie that are equal to a given word
#i traversed until end of the word and returned count stored in final node
#in countwordsstartingwith method i counted the number of words in the Trie that have a given prefix

        
        
        
        
        
        
        
        
