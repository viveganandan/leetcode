# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            leftmost = None
            prev = None
            while root:
                if root.left:
                    if not leftmost:
                        leftmost = root.left
                    if prev:
                        prev.next = root.left
                    prev = root.left
                if root.right:
                    if not leftmost:
                        leftmost = root.right
                    if prev:
                        prev.next = root.right
                    prev = root.right
                root = root.next
            root = leftmost
