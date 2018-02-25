# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(root, sums):
            if not root:
                return 0
            count = 1 if root.val == k else 0
            for i in range(len(sums)):
                sums[i] += root.val
                if sums[i] == k:
                    count += 1
            sums += [root.val]
            return count + dfs(root.left, sums[:]) + dfs(root.right, sums[:])
        return dfs(root, [])
