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
        if not root:
            return
        save = root
        queue = [root]
        while queue:
            prev = None
            for _ in range(len(queue)):
                root = queue.pop(0)
                if prev:
                    prev.next = root
                if root.left:
                    queue += [root.left]
                if root.right:
                    queue += [root.right]
                prev = root
