#https://www.codingninjas.com/codestudio/problems/diameter-of-binary-tree_8230762?challengeSlug=striver-sde-challenge

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameterOfBinaryTree(root):
    if root is None:
        return 0

    option1 = height(root.left) + height(root.right)
    option2 = diameterOfBinaryTree(root.left)
    option3 = diameterOfBinaryTree(root.right)
    return max(option1, max(option2, option3))

  #in diameterOfBinaryTree calculated the diameter of a binary tree, which is defined as the maximum number of nodes between any two leaf nodes
  #option1 represents the diameter passing through the root node 
  #option2 represents the diameter of the left subtree.
  #option3 represents the diameter of the right subtree.
  
