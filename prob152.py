class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 1
        neg = 1
        m = -float('inf')
        for n in nums:
            left = cur
            cur *= n
            neg *= n
            if cur > m:
                m = cur
            if cur == 0:
                # 0 breaks the flow, reset cur and neg
                cur = 1
                neg = 1
            elif cur < 0:
                if neg > 0:
                    # Previous negative has been balanced out
                    cur = neg
                    if cur > m:
                        m = cur
                else:
                    # This negative needs to be balanced out in the future
                    cur = 1
                # A new subarray needs to start at this negative
                neg = left * n
        if m > -float('inf'):
            return m
        return 0
