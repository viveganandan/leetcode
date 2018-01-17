# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def successor(node):
            """
            Find inorder successor for node
            """
            node = node.left
            while node.right:
                node = node.right
            return node
        if not root:
            return None
        count = 0
        prev = None
        stack = [root]
        # stack performs better
        while stack:
            if stack[-1].left == None:
                node = stack.pop()
                count += 1
                if count == k:
                    return node.val
                prev = node
                if node.right:
                    stack += [node.right]
            else:
                if successor(stack[-1]) == prev:
                    node = stack.pop()
                    count += 1
                    if count == k:
                        return node.val
                    if node.right:
                        stack += [node.right]
                    prev = node
                else:
                    stack += [stack[-1].left]
        return None
