2的幂
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(64):
            j = 2**i
            if j == n:
                return True
            if j >n:
                return False
