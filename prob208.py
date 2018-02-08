class Trie(object):
    class TrieNode(object):
        def __init__(self):
            self.root = [None] * 26
            self.end = False

        def setend(self):
            self.end = True

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.TrieNode()

    def getindex(self, char):
        """
        Find ord of char, and return its index in a 26 size list
        """
        return ord(char) - 97

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.head
        for w in word:
            c = self.getindex(w)
            if not cur.root[c]:
                cur.root[c] = self.TrieNode()
            cur = cur.root[c]
        cur.setend()

    def searchprefix(self, prefix):
        """
        Return trienode that contains prefix
        """
        if prefix:
            cur = self.head
            for p in prefix:
                c = self.getindex(p)
                if not cur.root[c]:
                    return None
                cur = cur.root[c]
            return cur

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.searchprefix(word)
        if cur:
            return cur.end
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.searchprefix(prefix)
        return cur != None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
