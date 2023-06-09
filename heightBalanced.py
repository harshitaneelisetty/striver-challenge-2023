   #https://www.codingninjas.com/codestudio/problems/is-height-balanced-binary-tree_8230771?challengeSlug=striver-sde-challenge

   def isBalancedBT(root):
        left = -1
        right = -1
        def dfs(root):
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return dfs(root) != -1
  
  #i initialised left and right variable to -1, i used these two variables to store the height of the left and right subtree respectively
  #i defined dfs, first i checked if the current root is None.
  #next i recursively called dfs function for the left and right child nodes of the current root and assigned the returned values to the left and right variables, respectively
  #if either left or right is -1, it means that the subtree is unbalanced
  #if the heights of the left and right subtrees differ by more than 1, i returned -1 indicates an unbalanced tree
  #none of the above conditions are met, i returned 1 plus the maximum of the left and right heights
  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
