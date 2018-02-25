class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Use union find to help detect cycle
        n = len(edges)
        parents = [i for i in range(n + 1)]
        weights = [1] * (n + 1)

        def findparent(parents, a):
            while parents[a] != a:
                # Compress path for grand children after parent is found
                parents[a] = parents[parents[a]]
                a = parents[a]
            return a

        def connect(parents, weights, a, b):
            pa = findparent(parents, a)
            pb = findparent(parents, b)
            if pa == pb:
                # Cycle found, don't connect
                return False
            if weights[pa] < weights[pb]:
                parents[pa] = pb
                weights[pb] += weights[pa]
            else:
                parents[pb] = pa
                weights[pa] += weights[pb]
            return True

        for edge in edges:
            if not connect(parents, weights, edge[0], edge[1]):
                return edge
        return None
