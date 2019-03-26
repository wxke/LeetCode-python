阶乘后的零
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 5 !=0:
            n = n - 1
        cont = 0
        while n:
            cont = cont + n //5
            n = n //5 

        return cont
