# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            """
            There are six sums to consider for a root:
            1. root sum
            2. left sum
            3. right sum
            4. root sum + left sum
            5. root sum + right sum
            6. root sum + left sum + right sum
            """
            if not root:
                return 0
            # Left and right max sum
            a, b = 0, 0
            if root.left:
                a = dfs(root.left)
                if root.val + a > self.m:
                    self.m = root.val + a
                if a > self.m:
                    self.m = a
            if root.right:
                b = dfs(root.right)
                if root.val + b > self.m:
                    self.m = root.val + b
                if b > self.m:
                    self.m = b
            if root.val > self.m:
                self.m = root.val

            if root.val + a + b > self.m:
                self.m = root.val + a + b

            # Determine max of root sum + left sum, root sum + right sum, or root sum
            a += root.val
            b += root.val
            if a > b and a > root.val:
                return a
            if b > root.val:
                return b
            return root.val

        self.m = -float('inf')
        dfs(root)
        return self.m
