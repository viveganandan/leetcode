# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, c):
            if not root:
                return c
            a = dfs(root.left, c * 10 + root.val)
            b = dfs(root.right, c * 10 + root.val)
            if root.left and root.right:
                return a + b
            if root.left:
                return a
            if root.right:
                return b
            return c * 10 + root.val
        return dfs(root, 0)
