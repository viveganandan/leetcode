# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(beg, end):
            # Generate trees, by combining left and right sub trees, with i as the root
            if beg > end:
                return [None]
            trees = []
            for i in range(beg, end + 1):
                left_trees = helper(beg, i - 1)
                right_trees = helper(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees += [root]
            return trees
        if n > 0:
            return helper(1, n)
        return []
