#https://www.codingninjas.com/codestudio/problems/construct-binary-tree-from-inorder-and-postorder-traversal_8230837?challengeSlug=striver-sde-challenge

def buildUtil(inorder, post, inStrt, inEnd, pIndex):
    if inStrt > inEnd:
        return None

    node = TreeNode(post[pIndex[0]])
    pIndex[0] -= 1

    if inStrt == inEnd:
        return node

    iIndex = search(inorder, inStrt, inEnd, node.data)
    node.right = buildUtil(inorder, post, iIndex + 1, inEnd, pIndex)
    node.left = buildUtil(inorder, post, inStrt, iIndex - 1, pIndex)

    return node

def buildTree(inorder, post, n):
    pIndex = [n - 1]
    return buildUtil(inorder, post, 0, n - 1, pIndex)
  
 #i used buildTree to construct the BT from its inorder and postorder traversals
#i used helper function to recursively builds the tree by identifying the root node
#and its left and right subtrees based on the indices in the inorder traversal.
#at last i constructed BT and returned as res

















