#https://www.codingninjas.com/codestudio/problems/size-of-largest-bst-in-binary-tree_8230743?challengeSlug=striver-sde-challenge

def isBST(root, min_val, max_val):
    if root == None:
        return True

    if root.data < min_val or root.data > max_val:
        return False

    return isBST(root.left, min_val, root.data - 1) and isBST(root.right, root.data + 1, max_val)


def size(root):
    if root == None:
        return 0
    
    return 1 + size(root.left) + size(root.right)


def largestBST(root):
    if isBST(root, -1e9, 1e9) == True:
        return size(root)

    return max(largestBST(root.left), largestBST(root.right))

 #i checked if a binary tree is a valid BST
 #by recursively validating each node's value against the range defined by its ancestors
 #then i found and returned the size of the largest BST
 #within the given binary tree by recursively examinied each subtree 
 #and selected the maximum size among them.
  
  
  
  
  
  
  
  
