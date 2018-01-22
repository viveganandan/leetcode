# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0
        def dfs(root):
            if root:
                left_sum = dfs(root.left)
                right_sum = dfs(root.right)
                self.tilt += abs(left_sum - right_sum)
                return root.val + left_sum + right_sum
            return 0
        dfs(root)
        return self.tilt
