位1的个数
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cont = 0
        while n:
            n = n &(n-1)
            cont += 1
        return cont
