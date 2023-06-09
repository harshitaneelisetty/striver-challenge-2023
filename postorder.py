#https://www.codingninjas.com/codestudio/problems/postorder-traversal_8230858?challengeSlug=striver-sde-challenge

def getPostOrderTraversal(root):
    order = []
    def postorder(root):
        if root == None:
            return   
        postorder(root.left)
        postorder(root.right)
        order.append(root.data)
    postorder(root)
    return order
  
  #i implemented recursive post order
  #i traversed tree in lrft->right->root fashion
