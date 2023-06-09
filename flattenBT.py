#https://www.codingninjas.com/codestudio/problems/flatten-binary-tree-to-linked-list_8230817?challengeSlug=striver-sde-challenge

def flattenBinaryTree(root):
    curr = root
    prev = None
    while curr:
        if curr.left:
            runner = curr.left
            while runner.right:
                runner = runner.right
            runner.right, curr.right, curr.left = curr.right, curr.left, None
        prev = curr
        curr = curr.right
    return prev
  
#i used flattenBinaryTree function to flatten the BT in place by iteratively traversing the tree using a while loop
#i started loops from the root and kept updating the curr node while rearranging the pointers to flatten the tree
#i used prev varibale to keep track of the previously visited node
#and i returned as the new root of the flattened tree







