有效的完全平方数
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(1,100000):
            if i**2 == num:
                return True
            if i ** 2> num:
                return False
