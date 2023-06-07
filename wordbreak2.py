#https://www.codingninjas.com/codestudio/problems/word-break-ii_8230786?challengeSlug=striver-sde-challenge


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isTerminal = False


def insert(root, word):
    curr = root
    for char in word:
        index = ord(char) - ord('a')
        if curr.children[index] is None:
            curr.children[index] = TrieNode()
        curr = curr.children[index]
    curr.isTerminal = True


def search(root, s, res, temp, pos):
    curr = root
    n = len(s)
    for i in range(pos, n):
        index = ord(s[i]) - ord('a')
        if curr.children[index] is None:
            return
        curr = curr.children[index]
        if curr.isTerminal:
            lastWord = temp + s[pos:i + 1]
            if i == n - 1:
                res.append(lastWord)
            else:
                search(root, s, res, lastWord + " ", i + 1)


def wordBreak(s, dictionary):
    root = TrieNode()
    for word in dictionary:
        insert(root, word)
    res = []
    search(root, s, res, "", 0)
    return res
  
  #I created a trie
  #I recursively searched for valid word combinations in the string and returns a list of all possible word break solutions.
  
  
  
