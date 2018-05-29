class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        def overlap_area():
            width = 0
            height = 0
            if A <= E <= C:
                width = min(G - E, C - E)
            elif A <= G <= C:
                width = min(G - E, G - A)
            elif E <= A <= G:
                width = min(C - A, G - A)
            elif E <= C <= G:
                width = min(C - A, C - E)
            if B <= F <= D:
                height = min(H - F, D - F)
            elif B <= H <= D:
                height = min(H - F, H - B)
            elif F <= B <= H:
                height = min(D - B, H - B)
            elif F <= D <= H:
                height = min(D - B, D - F)
            return width * height

        # Subtract sum of both rectangles from area of overalp
        return (C - A) * (D - B) + (G - E) * (H - F) - overlap_area()
