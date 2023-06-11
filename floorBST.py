#https://www.codingninjas.com/codestudio/problems/floor-in-bst_8230753?challengeSlug=striver-sde-challenge

def floorInBST(root, X):
    inorder = []
    def getInorder(root):
        if root == None:
            return None 
        getInorder(root.left)
        inorder.append(root.data)
        getInorder(root.right)
    getInorder(root)
    x = bisect.bisect_right(inorder, X)
    return inorder[x - 1]
  
  #i done inorder traversal soo elements will come in sorted order
  #then i done binary seach and found next greater element
