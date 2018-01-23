class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Take n = 4 as an example and j as 1, 2, n - 1, and n
        # Each j will be considered a root, we will take
        # the possible trees for the left and the possible tress for the right and combine them

        # But first, calculate the number of trees for i = 1, 2, ..., n - 1 and finally n

        # 1 2 3 4 -> 1 is root, left consists of nothing or 0 and right consists of 2-4
        # 1 2 3 4 -> 2 is root, left consists of 1 and right consists of 3-4
        # 1 2 3 4 -> 3 is root, left consists of 1-2 and right consists of 4
        # 1 2 3 4 -> 4 is root, left consists of 1-3 and right consists of 0 or nothing
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
