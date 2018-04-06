# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def issame(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and issame(s.left, t.left) and issame(s.right, t.right)
        def dfs(s, t):
            if not s:
                return False
            if s.val == t.val and issame(s, t):
                return True
            return dfs(s.left, t) or dfs(s.right, t)
        if not s and not t:
            return True
        if not s or not t:
            return False
        return dfs(s, t)
