class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if not nums or not k:
            return
        # Example: 1 2 3 4 5 and k is 3, the result would be 3 4 5 1 2
        # We know that 1 would end up in the 3rd index or kth index
        # So we need to replace [4, 5] with [1, 2]
        # [1, 2] is the "left", but before we can replace save the slice of the array on the right [3, 4, 5]
        left = len(nums) - k
        save = nums[left:]
        nums[k:] = nums[:left]
        nums[:k] = save
