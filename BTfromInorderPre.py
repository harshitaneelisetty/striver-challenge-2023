#https://www.codingninjas.com/codestudio/problems/construct-binary-tree-from-inorder-and-preorder-traversal_8230759?challengeSlug=striver-sde-challenge

def constructTree(inStart, inEnd, inorder, preorder):
    if inStart > inEnd:
        return None

    rootNode = preorder[constructTree.pIndex]
    constructTree.pIndex += 1
    root = BinaryTreeNode(rootNode)
   
    if inStart == inEnd:
        return root
 
    inIndex = buildBinaryTree.inorderIndex[rootNode]
    root.left = constructTree(inStart, inIndex - 1, inorder, preorder)
    root.right = constructTree(inIndex + 1, inEnd, inorder, preorder)
 
    return root

def buildBinaryTree(preorder, inorder):
    constructTree.pIndex = 0
    buildBinaryTree.inorderIndex = dict()

    for i in range(len(inorder)):
        buildBinaryTree.inorderIndex[inorder[i]] = i

    root = constructTree(0, len(inorder) - 1, inorder, preorder)
    return root
  
  #i used buildBinaryTree to construct a BT using inorder and preorder traversal
  #i used helper function to recursively build the tree by identifying the root node
  #and its left and right subtrees based on the indices in the inorder traversal
  #in function i used dictionary inorderIndex, to store the indices of values in the inorder traversal
  #i constructed the NT and then i returned as the result
  
  
  
  
  
  
  
  
  
  
  
  
  

  
  
