# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        left = None
        right = None
        while root:
            origleft = root.left
            origright = root.right
            root.left = left
            root.right = right
            left = origright
            right = root
            root = origleft
        return right
