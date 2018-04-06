class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        if digits:
            letters = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
            def combine(i, cur, ans):
                if i < len(digits):
                    if not digits[i] in letters:
                        combine(i + 1, cur, ans)
                    else:
                        for c in letters[digits[i]]:
                            save = cur[:]
                            cur += [c]
                            combine(i + 1, cur, ans)
                            cur = save
                else:
                    if len(cur) == len(digits):
                        ans += [''.join(cur)]
            combine(0, [], ans)
        return ans
