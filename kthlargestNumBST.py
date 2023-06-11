#https://www.codingninjas.com/codestudio/problems/k-th-largest-number-bst_8230750?challengeSlug=striver-sde-challenge

def inorder(root, inTraversal):
    if root == None:
        return

    inorder(root.left, inTraversal)
    inTraversal.append(root.data)
    inorder(root.right, inTraversal)


def KthLargestNumber(root, k):
    inTraversal = []
    inorder(root, inTraversal)
    n = len(inTraversal)

    if k > n:
        return -1

    return inTraversal[n - k]
  
#i done inorder traversal so elements in list will be in ascending order
#and i took n-kth element which is the kth largest element
