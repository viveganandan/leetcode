class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        j = 0
        i = 1
        while i < len(bits) - 1:
            jump = 1
            if bits[j]:
                jump += 1
            j += jump
            i += jump
        return bits[j] != 1
