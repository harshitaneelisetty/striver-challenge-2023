#https://www.codingninjas.com/codestudio/problems/preorder-traversal_8230856?challengeSlug=striver-sde-challenge

def getPreOrderTraversal(root):
	order = []
	def preorder(root):
		if root == None:
			return   
		order.append(root.data)
		preorder(root.left)
		preorder(root.right)
	preorder(root)
	return order

#i created recursive preorder solution
#i traversed tree in root->left->right fasion
