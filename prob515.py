# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        maxes = []
        while queue:
            m = -float('inf')
            for _ in range(len(queue)):
                root = queue.pop(0)
                m = max(m, root.val)
                if root.left:
                    queue += [root.left]
                if root.right:
                    queue += [root.right]
            maxes += [m]
        return maxes
