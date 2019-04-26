二进制表示中质数个计算置位
class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        num =[0 for i in range(0,25)]
        for i in range(2,25):
            if num[i] == 0:
                for j in range(i+i,25,i):
                    num[j] =1
        num[0]=1
        num[1] =1
        sum1 = 0
        for i in range(L,R+1):
            sum2=0
            while i:
                i = i &(i-1)
                sum2 +=1
            if num[sum2] ==0:
                sum1 +=1
            
        return sum1
