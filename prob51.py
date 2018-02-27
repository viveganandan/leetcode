class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(ans, board, used, row):
            if row == n:
                ans += [map(lambda b : ''.join(b), board)]
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
                        board[row][col] = 'Q'
                        dfs(ans, board[:][:], used[:], row + 1)
                        # Reset board and used for next col in row
                        board[row][col] = '.'
                        used[row] = -1
            return ans
        board = [['.' for _ in range(n)] for _ in range(n)]
        used = [-1] * n
        return dfs([], board, used, 0)
