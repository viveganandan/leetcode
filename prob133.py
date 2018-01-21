# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def dfs(node, visited):
            cur = UndirectedGraphNode(node.label)
            visited[cur.label] = cur
            for n in node.neighbors:
                if n.label in visited:
                    cur.neighbors += [visited[n.label]]
                else:
                    cur.neighbors += [dfs(n, visited)]
            return cur
        if node:
            return dfs(node, {})
