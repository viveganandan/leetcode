import operator

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # map the three operations that will be in input
        operations = {'+':operator.add, '-':operator.sub, '*':operator.mul}
        def compute(beg, end):
            if input[beg : end].isdigit():
                return [int(input[beg : end])]
            res = []
            for i in range(beg, end):
                c = input[i]
                if c in operations:
                    # compute left and right equations of operator
                    for l in compute(beg, i):
                        for r in compute(i + 1, end):
                            res += [operations[c](l, r)]
            return res
        return compute(0, len(input))
