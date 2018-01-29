class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = len(nums)
        if maxlen > 1:
            i = 1
            while i < len(nums) and nums[i] == nums[0]:
                i += 1
                maxlen -= 1
            if i < len(nums):
                up = nums[i] > nums[0]
                for i in range(i + 1, len(nums)):
                    # If cur num is same as previous num, or there is no wiggle, discard the previous
                    if nums[i] == nums[i - 1] or up == (nums[i] > nums[i - 1]):
                        maxlen -= 1
                    else:
                        up = not up
        return maxlen
