#https://www.codingninjas.com/codestudio/problems/lca-of-binary-tree_8230760?challengeSlug=striver-sde-challenge

def lowestCommonAncestor(root, val1, val2):
    if root is None:
        return -1
    if root.data == val1 or root.data == val2:
        return root.data

    left = lowestCommonAncestor(root.left, val1, val2)
    right = lowestCommonAncestor(root.right, val1, val2)

    if left == -1 and right == -1:
        return -1
    elif left != -1 and right == -1:
        return left
    elif left == -1 and right != -1:
        return right
    else:
        return root.data

#firstly i checked the value of the root, if it is none it means the current subtree is empty so i returned -1
#if the value of root matches either val1 or val2, it means the current node is one of the desired nodes, so i returned the value of root.data
#i recursively called lowestCommonAncestor function for the left and right child nodes of the current root
#and i assigned the returned values to left and right, respectively
#then i checked for various conditions
#if both left and right are -1, it means neither val1 nor val2 was found in the subtree, so i returned -1.
#if left is not -1 and right is -1, it means only val1 was found in the subtree, so i returned left
#if left is -1 and right is not -1, it means only val2 was found in the subtree, so i returned right
#if both left and right are not -1, it means both val1 and val2 were found in different subtrees, so the current root is the lowest common ancestor, and i returned root.data










