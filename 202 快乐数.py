快乐数
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = n
        list1 = []
        while True:
            sum1 = 0
            while n:
                sum1 += (n % 10) ** 2
                n = n // 10

            n = sum1
            if sum1 not in list1:
                list1.append(sum1)
            else:
                flag1 = False
                break
            if sum1 == 1:
                flag1 = True
                break
            elif sum1 == flag:
                flag1 = False
                break
            
        return flag1
