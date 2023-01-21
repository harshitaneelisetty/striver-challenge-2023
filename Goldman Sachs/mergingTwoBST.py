# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inOrder(self, root, lst):
            if root == None:
                return
            self.inOrder(root.left, lst)
            lst.append(root.val)
            self.inOrder(root.right, lst)
            return lst

    def mergeSortedArray(self, lst1, lst2):
        ans = []
        n1 = len(lst1)
        n2 = len(lst2)
        p1, p2 = 0, 0
        while p1 < n1 and p2 < n2:
            if lst1[p1] < lst2[p2]:
                ans.append(lst1[p1])
                p1 += 1
            else:
                ans.append(lst2[p2])
                p2 += 1
        while p1 < n1:
            ans.append(lst1[p1])
            p1 += 1
        while p2 < n2:
            ans.append(lst2[p2])
            p2 += 1
        return ans

    def getAllElements(self, root1, root2):
        lst1 = self.inOrder(root1, [])
        lst2 = self.inOrder(root2, [])
        if lst1 and lst2:
            return self.mergeSortedArray(lst1, lst2)
        if lst1:
            return lst1
        if lst2:
            return lst2
       
       # In BST if we do inorder traversal the elements will be in sorted order
      # so I done inorder for 2 roots and then I merged two sorted arrays
