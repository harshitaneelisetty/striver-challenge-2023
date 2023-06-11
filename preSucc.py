#https://www.codingninjas.com/codestudio/problems/predecessor-and-successor-in-bst_8230742?challengeSlug=striver-sde-challenge

def predecessorSuccessor(root, key):

    predecessor = -1
    successor = -1

    while root.data != key:
        if key > root.data:
            predecessor = root.data
            root = root.right
        else:
            successor = root.data
            root = root.left

    
    rightSubtree = root.right

    while rightSubtree is not None:
        successor = rightSubtree.data
        rightSubtree = rightSubtree.left


    leftSubtree = root.left

    while leftSubtree is not None:
        predecessor = leftSubtree.data
        leftSubtree = leftSubtree.right

    return [predecessor, successor]
  
#I initialized predecessor and successor variable to -1, will store the values of the predecessor and successor
#i iterated over loop until root.data is equal to key
#if it is true it means that the predecessor of the key be the curr node or in right subtrr
#in that case i updadted predecessor variable with the current root.data value
#and moved root to its right child
#if key is less than or equal to the current root.data, it it means that the successor of the key be the curr nide
#or in left subtree. in that case i updated the successor variable with the current root.data
#and moved to left child
#after while lopp i checked if there is a right subtree from the current root
#it means that the successor of the key should be in that right subtree
#i entered another while loop that moves down the leftmost path of the right subtree
#updated successor variable with the curr node 
#similarly i checked for left subtree
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
