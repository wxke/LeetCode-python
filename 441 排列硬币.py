排列硬币
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = 1
        cont = 0
        
        while q <= n:
            cont += 1
            n = n -q
            q += 1
        return cont
            
            
            
        
