import operator

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def pushn(stack, op, n):
            n = int(n)
            # Use rank to determine if previous equation can be evaluated
            while len(stack) > 1 and rank[op] <= rank[stack[-1]]:
                n = ops[stack.pop()](stack.pop(), n)
            stack += [n, op]
        if s:
            stack = []
            rank = {'+':0, '-':0, '*':1, '/':1, '':-1}
            ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.div}
            j = 0
            for i in range(len(s)):
                if s[i] in ops:
                    pushn(stack, s[i], s[j : i])
                    j = i + 1
            pushn(stack, '', s[j : ])
            return stack[0]
        return 0
