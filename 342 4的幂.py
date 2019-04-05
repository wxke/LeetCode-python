4的幂
class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        j = 1
        for i in range(32):
            
            if j == num:
                return True
            elif j > num:
                return False
            j = j * 4
