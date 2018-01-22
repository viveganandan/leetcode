# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def dfs(root):
            if root:
                if root.val < L:
                    # Keep traversing right, until you find the first node with value >= L
                    while root and root.val < L:
                        root = root.right
                    return dfs(root)
                if root.val > R:
                    # Keep traversing left, until you find the first node with value <= R
                    while root and root.val > R:
                        root = root.left
                    return dfs(root)
                root.left = dfs(root.left)
                root.right = dfs(root.right)
            return root
        return dfs(root)
