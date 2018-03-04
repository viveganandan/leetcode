class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = 0
        i = 0
        cur = 1
        for j in range(len(nums)):
            cur *= nums[j]
            while i < j and cur >= k:
                cur /= nums[i]
                i += 1
            if cur < k:
                m += j - i + 1
        return m
