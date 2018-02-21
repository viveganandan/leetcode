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
        if not root or not root.left:
            return root
        root.left = self.upsideDownBinaryTree(root.left)
        save = root.left
        suc = root.left
        while suc.right:
            suc = suc.right
        suc.right = root
        suc.left = root.right
        root.left = None
        root.right = None
        return save
