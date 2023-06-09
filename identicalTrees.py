#https://www.codingninjas.com/codestudio/problems/check-identical-trees_8230719?challengeSlug=striver-sde-challenge

def identicalTrees(p, q):
    if p == None or q == None:
        return p == q
    return p.data == q.data and identicalTrees(p.left, q.left) and identicalTrees(p.right, q.right)

 #if p is none or q is none i checked if both are none or not
 #then i checked if value of two nodes are same or not then i recursively chcekd the left sub tree and right subtree
