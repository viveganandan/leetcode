class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        def dfs(i, j, k, visited):
            visited[i][j] = 1
            if k == len(word) - 1 and board[i][j] == word[k]:
                return True
            if board[i][j] == word[k]:
                if i > 0 and not visited[i - 1][j] and dfs(i - 1, j, k + 1, visited):
                    visited[i][j] = 0
                    return True
                if j < n - 1 and not visited[i][j + 1] and dfs(i, j + 1, k + 1, visited):
                    visited[i][j] = 0
                    return True
                if i < m - 1 and not visited[i + 1][j] and dfs(i + 1, j, k + 1, visited):
                    visited[i][j] = 0
                    return True
                if j > 0 and not visited[i][j - 1] and dfs(i, j - 1, k + 1, visited):
                    visited[i][j] = 0
                    return True
            visited[i][j] = 0
            return False

        if word:
            visited = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if dfs(i, j, 0, visited):
                        return True
        return False
