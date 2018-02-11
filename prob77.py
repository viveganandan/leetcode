class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(m, k, i, j, ans, temp):
            """
            m - The range that is available at each level
            k - Number of spots left to fill
            i - The current index for the slot to assign
            j - The range start value
            ans - The resulting list
            temp - The temp list to hold temporary combination
            """
            # All k spots have been filled
            if k == 0:
                ans += [temp]
            else:
                #
                m = m - k + 1
                for j in range(j, j + m):
                    temp[i] = j
                    helper(n - j, k - 1, i + 1, j + 1, ans, temp[:])
        ans = []
        helper(n, k, 0, 1, ans, [0] * k)
        return ans
