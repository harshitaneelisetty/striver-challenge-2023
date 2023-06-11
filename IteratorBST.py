#https://www.codingninjas.com/codestudio/problems/bst-iterator_8230815?challengeSlug=striver-sde-challenge

class BSTIterator:
    def __init__(self, root):
        self.nodeStack = []
        self.leftMostInorder(root)

    def next(self):
        top = self.nodeStack.pop()
        if top.right is not None:
            self.leftMostInorder(top.right)
        return top.data

    def hasNext(self):
        return len(self.nodeStack) > 0

    def leftMostInorder(self, root):
        while root is not None:
            self.nodeStack.append(root)
            root = root.left

 #i used nodeStack list to serve as the stack for maintaining the nodes during the inorder traversal
 #i initialized nodeStack and performed the leftmost inorder traversal starting from the root
 #in next method i retieved the top node from the stack, pops it, and if the node has a right child, performed the leftmost inorder traversal starting from that child.
 #in hasNext method i checked if the stack is empty or not to determine if there are more nodes to process
 #in leftMostInorder method i performed the leftmost inorder traversal starting from the given root node
  
  
  
  
  
