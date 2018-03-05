class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        m = -float('inf')
        cur = 0
        for n in nums:
            temp = cur + n
            if temp > m:
                m = temp
            # n in neg, and there is no pos val big enough on the left
            if temp < 0:
                temp = 0
            cur = temp
        return m
