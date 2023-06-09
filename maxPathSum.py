#https://www.codingninjas.com/codestudio/problems/maximum-path-sum-between-two-leaves_8230713?challengeSlug=striver-sde-challenge

def helper(root):
    if root is None:
        return -1, 0

    if root.left is None and root.right is None:
        return -1, root.val

    left_max_sum, left_max_leaf = helper(root.left)
    right_max_sum, right_max_leaf = helper(root.right)

    max_sum = max(left_max_sum, right_max_sum)
    max_leaf = max(left_max_leaf, right_max_leaf) + root.val

    if root.left is not None and root.right is not None:
        max_sum = max(max_sum, left_max_leaf + right_max_leaf + root.val)

    return max_sum, max_leaf

def findMaxSumPath(root):
    max_sum, max_path_to_leaf = helper(root)
    return max_sum
  
 #i calculated max sum path in bt by recursively traversing the tree and considering different cases for the maximum path
 #i used a helper function to calculate max path sum and max sum of path to a leaf node
  #and then in main function i called helper function and returnd max path sum
  
  
  
  
  
  
  
