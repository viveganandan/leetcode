class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        i = 0
        m = float('inf')
        for j in range(len(nums)):
            nums[j] += prev
            prev = nums[j]
            if nums[j] >= s:
                while nums[j] - nums[i] >= s:
                    i += 1
                if j - i + 1 < m:
                    m =  j - i + 1
        if m < float('inf'):
            return m
        return 0
