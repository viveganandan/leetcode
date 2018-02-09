class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        lookup = {}
        for i in range(26):
            lookup[chr(97 + i)] = i

        # Define TrieNode
        class TrieNode(object):
            def __init__(self):
                self.root = [0] * 26
                self.word = ''

        # Insert words to form a dictionary
        head = TrieNode()
        for word in words:
            cur = head
            for c in word:
                i = lookup[c]
                if not cur.root[i]:
                    cur.root[i] = TrieNode()
                cur = cur.root[i]
            # Store word at end, so we can grab word easily later on
            cur.word = word

        # Dimensions of board
        m = len(board)
        n = len(board[0])

        def dfs(cur, i, j, visited, ans):
            """
            Depth first search starting at cur point
            """
            visited[i][j] = 1
            d = cur.root[lookup[board[i][j]]]
            if d:
                if d.word:
                    ans.add(d.word)
                if i > 0 and not visited[i - 1][j]:
                    dfs(d, i - 1, j, visited, ans)
                if j < n - 1 and not visited[i][j + 1]:
                    dfs(d, i, j + 1, visited, ans)
                if i < m - 1 and not visited[i + 1][j]:
                    dfs(d, i + 1, j, visited, ans)
                if j > 0 and not visited[i][j - 1]:
                    dfs(d, i, j - 1, visited, ans)
            visited[i][j] = 0

        ans = set()
        # Keep track of visited points
        visited = [[0 for _ in range(n)] for _ in range(m)]

        # For each point in board, dfs
        for i in range(m):
            for j in range(n):
                dfs(head, i, j, visited, ans)
        return list(ans)
