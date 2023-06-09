#https://www.codingninjas.com/codestudio/problems/inorder-traversal_8230857?challengeSlug=striver-sde-challenge

def getInOrderTraversal(root):
    order = []
    def inorder(root):
        if root == None:
            return  
        inorder(root.left)
        order.append(root.data)
        inorder(root.right)
    inorder(root)
    return order
  
  #here i created recursive inorder solution
  #i iterated tree in left->root->right fashion
