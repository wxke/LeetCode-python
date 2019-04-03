3的幂
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum1 = 1
        for i in range(0,33):
            if sum1 == n:
                return True
            if sum1 > n:
                return False
            sum1 = sum1 * 3
