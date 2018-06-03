class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        diff = {0: -1}
        x = 0
        m = 0
        for i in range(len(nums)):
            x += nums[i]
            if x - k in diff:
                d = i - (diff[x - k] + 1) + 1
                if d > m:
                    m = d
            if not x in diff:
                diff[x] = i
        return m
