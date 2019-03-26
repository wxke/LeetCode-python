计数质数
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        li = [0 for i in range(0,n)]
        li[0] = 1
        li[1] = 1
        cont = 0
        for i in range(2,n):
            if li[i] == 0:
                # print(i)
                cont += 1
                for j in range(i+i,n,i):
                    li[j] = 1
        return cont

