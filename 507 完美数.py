完美数
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <2:
            return False
        import math
        q = int(math.sqrt(num))
        # print(q)
        sum1 = 0
        for i in range(1,q+1):
            if num % i ==0:
                # print(i,num//i)
                sum1 += i
                sum1 += num // i
                
        if sum1 - num == num:
            return True
        return False
    
