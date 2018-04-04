# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            a = dfs(root.left)
            b = dfs(root.right)
            if root.left and (a == 0 or root.left.val != root.val):
                return 0
            if root.right and (b == 0 or root.right.val != root.val):
                return 0
            self.count += 1
            return 1
        self.count = 0
        dfs(root)
        return self.count
