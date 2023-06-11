#https://www.codingninjas.com/codestudio/problems/pair-sum-in-bst_8230756?challengeSlug=striver-sde-challenge

def pairSumBST(root, k):
    start = deque()
    end = deque()

    curr_node = root
    
    while curr_node is not None:
        start.append(curr_node)
        curr_node = curr_node.left

    curr_node = root
    
    while curr_node is not None:
        end.append(curr_node)
        curr_node = curr_node.right

    
    while start[-1] != end[-1]:
        val1 = start[-1].data
        val2 = end[-1].data

        if val1 + val2 == k:
            return True

        if val1 + val2 < k:
            curr_node = start[-1].right
            start.pop()
            
            while curr_node is not None:
                start.append(curr_node)
                curr_node = curr_node.left

        else:
            curr_node = end[-1].left
            end.pop()

            while curr_node is not None:
                end.append(curr_node)
                curr_node = curr_node.right

    return False
  
  #firsy i traversed until left most node of bst and stored in start deque
  #next i traversed unit right node node of bst and stored in end deque
  #next i iterated until the top elements of both start and end deques are the same 
  #i stored to node of start and end deques in val1 and val2
  #if val1 + val2 is equal to the target value k, it means that a pair of nodes with the desired sum exists in the BST
  #if val1 + val2 is less than k, it means that the current sum is smaller than the target so i explored larger values
  #i moved start deque to right
  #if val1 + val2 is greater than k, it means that the current sum is larger than the target so i explored smallee values
  #i moved end deque to left
  
  
  
  
  
  
  
  
