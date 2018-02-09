class WordDictionary(object):
    class TrieNode(object):
        def __init__(self):
            self.root = [None] * 26
            self.end = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.head
        for w in word:
            j = ord(w) - 97
            if not cur.root[j]:
                cur.root[j] = self.TrieNode()
            cur = cur.root[j]
        cur.end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(start, end, cur):
            if start == end:
                return cur.end
            for i in range(start, end):
                if word[i] == '.':
                    for node in cur.root:
                        if node and dfs(i + 1, end, node):
                            return True
                    # All 26 nodes lead to nowhere
                    return False
                j = ord(word[i]) - 97
                if not cur.root[j]:
                    return False
                cur = cur.root[j]
            return cur.end

        return dfs(0, len(word), self.head)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
