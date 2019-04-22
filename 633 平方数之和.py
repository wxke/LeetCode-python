平方数之和
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0:
            return True
        import math
        for i in range(int(math.sqrt(c))+1):
            if math.sqrt(c - i **2) == int(math.sqrt(c - i **2)):
                return True
        return False
