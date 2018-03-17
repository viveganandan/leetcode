class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        for i in range(len(nums)):
            if i -  2 > -1:
                nums[i] += nums[i -  2]
            if nums[i] > m:
                m = nums[i]
            else:
                nums[i] = m
        return m
