import operator

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def push_n(stack, n):
            # * and / take precedence, calculate this expression first
            if stack and (stack[-1] == '*' or stack[-1] == '/'):
                n = ops[stack.pop()](stack.pop(), n)
            stack += [n]
        if s:
            stack = []
            ops = {'+':operator.add, '-':operator.sub,
                '*':operator.mul, '/':operator.div}
            j = 0
            for i in range(len(s)):
                if s[i] in ops:
                    push_n(stack, int(s[j : i]))
                    stack += [s[i]]
                    j = i + 1
            push_n(stack, int(s[j : ]))
            # For the rest of the stack, calculate top down (left to right)
            for i in range(0, len(stack) - 1, 2):
                stack[i + 2] = ops[stack[i + 1]](stack[i], stack[i + 2])
            return stack[-1]
        return 0
