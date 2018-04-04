# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root, sums, freq):
            if not root:
                return 0
            x = dfs(root.left, sums, freq) + dfs(root.right, sums, freq) + root.val
            if x in sums:
                sums[x] += 1
            else:
                sums[x] = 1
            if sums[x] > freq[0]:
                freq[0] = sums[x]
            return x
        sums = {}
        freq = [0]
        dfs(root, sums, freq)
        ans = []
        for x,f in sums.iteritems():
            if f == freq[0]:
                ans += [x]
        return ans
