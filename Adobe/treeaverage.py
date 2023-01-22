# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def helper(root):
            if root == None:
                return 0, 0
            leftValue, leftCount = helper(root.left)
            rightValue, rightCount = helper(root.right)
            value = leftValue + rightValue + root.val
            count = leftCount + rightCount + 1
            if value // count == root.val:
                self.result += 1
            return value, count
        s, c = helper(root)
        return self.result
