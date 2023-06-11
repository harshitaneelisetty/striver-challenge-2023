#https://www.codingninjas.com/codestudio/problems/ceil-from-bst_8230754?challengeSlug=striver-sde-challenge

def findCeil(root, target):
    ceilVal = float('inf')  
    if root == None:
        return -1
    while root:
        if root.data == target:
            return root.data
        elif root.data < target:
            root = root.right
        else:
            ceilVal = min(ceilVal, root.data)
            root = root.left

    return ceilVal  if ceilVal != float('inf') else -1
  
  #firstly i initialized the ceil value as positive infinity
  #if the target value is found in the tree, it is the ceiling itself
  #if the current node's data is less than the target, i moved to the right subtree
  #if the current node's data is greater than the target, i updated the ceil value
  
  
