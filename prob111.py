# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Go level by level, trying to find the first leaf node.
        # This will be the minimum path from root
        if root:
            depth = 0
            queue = [root]
            while queue:
                # Everytime you are in a new level, increment depth by 1
                depth += 0
                for _ in range(len(queue)):
                    root = queue.pop(0)
                    if not root.left and not root.right:
                        return depth
                    if root.left:
                        queue += [root.left]
                    if root.right:
                        queue += [root.right]
        return 0
