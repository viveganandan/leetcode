class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.total = 0
        def dfs(used, row):
            if row == n:
                self.total += 1
            else:
                # Figure out the blocked cols for this row
                blocked = [0] * n
                for i in range(n):
                    if used[i] > -1:
                        for k in [-(row - i), 0, row - i]:
                            col = used[i] + k
                            if col > -1 and col < n:
                                blocked[col] = 1
                for col in range(n):
                    # Place your queen on non blocked cols in the current row
                    if not blocked[col]:
                        used[row] = col
                        dfs(used, row + 1)
                        # Reset used for next col in row
                        used[row] = -1
        used = [-1] * n
        dfs(used, 0)
        return self.total
