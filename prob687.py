# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.lonpath = 0
        def dfs(root):
            if not root:
                return 0
            a = dfs(root.left)
            b = dfs(root.right)
            if root.left and root.left.val == root.val:
                a += 1
            else:
                a = 0
            if root.right and root.right.val == root.val:
                b += 1
            else:
                b = 0
            if a + b > self.lonpath:
                self.lonpath = a + b
            return max(a, b)
        dfs(root)
        return self.lonpath
