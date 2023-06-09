#https://www.codingninjas.com/codestudio/problems/boundary-traversal-of-binary-tree_8230712?challengeSlug=striver-sde-challenge

def leftBoundary(root, ans):
    if root == None or (root.left == None and root.right == None):
        return

    ans.append(root.data)

    if root.left != None:
        leftBoundary(root.left, ans)
    else:
        leftBoundary(root.right, ans)


def rightBoundary(root, ans):
    if root == None or (root.left == None and root.right == None):
        return

    if root.right != None:
        rightBoundary(root.right, ans)
    else:
        rightBoundary(root.left, ans)

    ans.append(root.data)


def leafNodes(root, ans):
    if root == None:
        return

    if root.left == None and root.right == None:
        ans.append(root.data)
        return

    leafNodes(root.left, ans)
    leafNodes(root.right, ans)


def traverseBoundary(root):
    ans = []

    if root == None:
        return ans

    ans.append(root.data)

    leftBoundary(root.left, ans)
    leafNodes(root.left, ans)
    leafNodes(root.right, ans)
    rightBoundary(root.right, ans)

    return ans
  
  #i created four seperate functions leftBoundary, rightBoundary, leafNodes, and traverseBoundary
  #i created leftBoundary and rightBoundary functions to traverse the left and right boundaries of the tree
  #respectively, by recursively appending the node values
  #i created leafNodes function to recursively collects the leaf nodes of the tree
  #finally in traverseBoundary function i combined all the results of the boundary traversals and leaf nodes
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
