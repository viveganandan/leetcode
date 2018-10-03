# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.x = 0
        def dfs(root, depth):
            if not root:
                return
            if not root.left and not root.right:
                if depth > self.x:
                    self.x = depth
            else:
                dfs(root.left, depth + 1)
                dfs(root.right, depth + 1)
        dfs(root, 1)
        return self.x
