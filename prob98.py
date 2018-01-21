# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root, lo, hi):
            if not root:
                return True
            if lo < root.val < hi:
                return dfs(root.left, lo, root.val) and dfs(root.right, root.val, hi)
            return False
        return dfs(root, -float('inf'), float('inf'))
