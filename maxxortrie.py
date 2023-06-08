#https://www.codingninjas.com/codestudio/problems/maximum-xor-with-an-element-from-array_8230839?challengeSlug=striver-sde-challenge

class TrieNode:
    def __init__(self):
        self.children = [None, None]


def insert(root, num):
    node = root

    for i in range(30, -1, -1):
        bit = (num >> i) & 1
        if node.children[bit] is None:
            node.children[bit] = TrieNode()
        node = node.children[bit]


def maxXorQueries(arr, queries):
    n = len(arr)
    m = len(queries)

    result = [-1] * m
    order = list(range(m))

    arr.sort()
    order.sort(key=lambda x: queries[x][1])

    root = TrieNode()
    p = 0

    for i in order:
        query = queries[i]
        while p < n and arr[p] <= query[1]:
            insert(root, arr[p])
            p += 1

        if root.children[0] is None and root.children[1] is None:
            continue

        node = root
        ans = 0

        for j in range(30, -1, -1):
            bit = (query[0] >> j) & 1
            if node.children[1 - bit] is not None:
                node = node.children[1 - bit]
                ans |= (1 << j)
            else:
                node = node.children[bit]

        result[i] = ans

    return result
  
  #i created a trienode class represnts a node in the trie and i created 2 children indicating 0 and 1 bits
  #i created insert function to insert a number into the trie by iterating over its bits
  #from msb to lsb. i created child nodes if necessary and moved down the trie
  #the main func takes an array of numbers and a list of queries. i initialised a res list with -1
  #and an order list kept track of the order of queries
  #i sorted arra and i sorted order list based on upper limit of each query
  #i iterated through each query in sorted order 
  #i inseted number from arr into trie unit the ptr reaches end of the array or the num becomes larger than upper limit
  #If both children of the Trie root are None i ignored
  #else i traversed the trie based on each bit of the query number
  #started from the msb.i checked if the complement bit is present in the trie
  #if it is, i moved to that child updates and variable with the bitwise op operation
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
