#https://www.codingninjas.com/codestudio/problems/tree-traversals_8230775?challengeSlug=striver-sde-challenge

def getTreeTraversal(root):
    inorder = []
    def getinorder(root):
        if root == None:
            return   
        getinorder(root.left)
        inorder.append(root.data)
        getinorder(root.right)
    temp = root
    getinorder(temp)
    temp1 = temp
    preorder = []
    def getpreorder(root):
        if root == None:
            return  
        preorder.append(root.data)
        getpreorder(root.left)
        getpreorder(root.right)
    getpreorder(temp1)
    temp2 = temp 
    postorder = []
    def getpostorder(root):
        if root == None:
            return   
        getpostorder(root.left)
        getpostorder(root.right)
        postorder.append(root.data)
    getpostorder(temp2)
    return [inorder, preorder, postorder]
  #i done 3 traversals in one code by writting seperate functions for each traversal
  
  

