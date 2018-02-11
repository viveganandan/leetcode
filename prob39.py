class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(i, cur, ans, temp):
            for i in range(i, len(candidates)):
                x = cur + candidates[i]
                if x <= target:
                    save = temp + [candidates[i]]
                    if x == target:
                        ans += [save]
                    dfs(i, x, ans, save)
        ans = []
        dfs(0, 0, ans, [])
        return ans
