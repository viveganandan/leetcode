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
        # Using Morris inorder traversal
        def successor(node):
            """
            Find the inorder successor for node
            If already found, then node's left rightmost node will point to itself
            """
            left = node.left
            while left.right:
                if left.right == node:
                    left.right = None
                    return None
                left = left.right
            return left
        count = 0
        cur = root
        while cur:
            if cur.left:
                s = successor(cur)
                if not s:
                    # "No left"
                    count += 1
                    if count == k:
                        return cur.val
                    cur = cur.right
                else:
                    s.right = cur
                    cur = cur.left
            else:
                # No left
                count += 1
                if count == k:
                    return cur.val
                cur = cur.right
        return None
