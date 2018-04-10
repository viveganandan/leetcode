class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def findarea(p1, p2, p3):
            # findarea using the shoelace algorithm
            a = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
            b = p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0]
            return float(0.5 * abs(a - b))
        # check all possible triangle areas
        maxarea = -float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    area = findarea(points[i], points[j], points[k])
                    if area > maxarea:
                        maxarea = area
        return maxarea
