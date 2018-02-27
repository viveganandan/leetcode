class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        beg = 0
        end = 0
        n = len(s)
        dp = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and dp[i + 1][j - 1] > -1:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if dp[i][j] > end - beg + 1:
                        beg = i
                        end = j
                else:
                    dp[i][j] = -1
        return s[beg: end + 1]
