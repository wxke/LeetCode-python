1比特与2比特字符
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i<len(bits)-1:
            if bits[i] == 1:
                i += 2
            else:
                i = i + 1
        if i == len(bits)-1:
            return True
        else:
            return False
