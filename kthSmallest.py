#https://www.codingninjas.com/codestudio/problems/kth-smallest-node-in-bst_8230751?challengeSlug=striver-sde-challenge

def kthSmallest(root, k):
    def inorder(root,lis):
        if root == None:
            return
        inorder(root.left,lis)
        lis.append(root.data)
        inorder(root.right,lis)
        return lis
    lis = []
    lis = inorder(root,lis)
    return lis[k - 1]
  
  #i done inorder traversal so in bst inorder list contains elements in asecnding order
  #so i took k - 1th element which is the kth smallest eleent
