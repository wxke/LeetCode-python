爬楼梯
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 2
        b = 3
        for i in range(3,n):
            a , b = b , a+ b
        return b
