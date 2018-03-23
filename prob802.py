class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        def dfs(nodes, i):
            # nodes[i] has not been visited yet
            if nodes[i] < 0:
                nodes[i] = 0
                for j in graph[i]:
                    dfs(nodes, j)
                    # adjacent node is not safe, that means this node is also not safe
                    if nodes[j] == 0:
                        return
                # all ajdacent nodes are safe, that means this node is safe
                nodes[i] = 1
        nodes = [-1] * len(graph)
        safe = []
        for i in range(len(graph)):
            dfs(nodes, i)
            # Only add safe nodes to our safe list
            if nodes[i] == 1:
                safe += [i]
        return safe
