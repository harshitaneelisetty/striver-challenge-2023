#https://www.codingninjas.com/codestudio/problems/symmetric-tree_8230686?challengeSlug=striver-sde-challenge

def isTreeSymmetric(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.data == right.data:
        inRoot = isTreeSymmetric(left.left, right.right)
        outRoot = isTreeSymmetric(left.right, right.left)
        return inRoot and outRoot
    else:
        return False

def isSymmetric(root):
    if root is None:
        return True
    return isTreeSymmetric(root.left, root.right)
  
  #i used isTreeSymmetric function to recursively checks if a binary tree is symmetric by comparing corresponding nodes in the left and right subtrees
  #i used isSymmetric function to handle the case of emplt tree 
  #and called isTreeSymmetric with the left and right child nodes of the root 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
